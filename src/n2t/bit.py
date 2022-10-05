from chip import Chip, PinName, BitInt
from clock import ClockedChip
from dff import Dff
from n2t.mux import Mux


class Bit(ClockedChip):
    """Bit
    """

    pin_in = PinName('in')
    pin_load = PinName('load')
    pin_out = PinName('out')

    in_pins = (pin_in, pin_load)
    out_pins = (pin_out,)

    def __init__(self) -> None:
        super().__init__()
        self.mux = Mux()
        self.dff = Dff()
        self.dff.wire(Dff.pin_out, self.mux, Mux.pin_a)
        self.wire(self.pin_in, self.mux, Mux.pin_b)
        self.wire(self.pin_load, self.mux, Mux.pin_sel)
        self.mux.wire(Mux.pin_out, self.dff, Dff.pin_in)
        self.dff.wire(Dff.pin_out, self, self.pin_out)

    def eval(self):
        self.mux.eval()
        self.dff.eval()


def test_bit(
        chip: Bit, i: BitInt, load: BitInt,
        expected_tick_out: BitInt, expected_tock_out: BitInt
):
    chip.set(Bit.pin_in, i)
    chip.set(Bit.pin_load, load)
    chip.tick()
    assert chip.output()[Bit.pin_out] == expected_tick_out
    chip.tock()
    assert chip.output()[Bit.pin_out] == expected_tock_out


def run_all_test_cases():
    chip = Bit()
    test_bit(chip, BitInt(0), BitInt(0), BitInt(0), BitInt(0))
    test_bit(chip, BitInt(0), BitInt(1), BitInt(0), BitInt(0))
    test_bit(chip, BitInt(1), BitInt(0), BitInt(0), BitInt(0))
    test_bit(chip, BitInt(1), BitInt(1), BitInt(0), BitInt(1))


if __name__ == '__main__':
    run_all_test_cases()
