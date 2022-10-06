from chip import PinName, Bit
from clock import ClockedChip
from dff import Dff
from n2t.mux import Mux


class BitRegister(ClockedChip):
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
        chip: BitRegister, i: Bit, load: Bit,
        expected_tick_out: Bit, expected_tock_out: Bit
):
    chip.set(BitRegister.pin_in, i)
    chip.set(BitRegister.pin_load, load)
    chip.tick()
    assert chip.plus
    assert chip.output()[BitRegister.pin_out] == expected_tick_out
    chip.tock()
    assert not chip.plus
    assert chip.output()[BitRegister.pin_out] == expected_tock_out


def run_all_test_cases():
    chip = BitRegister()
    test_bit(chip, Bit(0), Bit(0), Bit(0), Bit(0))
    test_bit(chip, Bit(0), Bit(1), Bit(0), Bit(0))
    test_bit(chip, Bit(1), Bit(0), Bit(0), Bit(0))
    test_bit(chip, Bit(1), Bit(1), Bit(0), Bit(1))
    test_bit(chip, Bit(0), Bit(0), Bit(1), Bit(1))
    test_bit(chip, Bit(1), Bit(0), Bit(1), Bit(1))
    test_bit(chip, Bit(0), Bit(1), Bit(1), Bit(0))


if __name__ == '__main__':
    run_all_test_cases()
