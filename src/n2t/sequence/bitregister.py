from n2t.chip import Pin, Bit
from n2t.sequence.clock import ClockedChip
from n2t.sequence.dff import Dff
from n2t.mux import Mux


class BitRegister(ClockedChip):
    """Bit
    """

    pin_in = Pin('in')
    pin_load = Pin('load')
    pin_out = Pin('out')

    IN = (pin_in, pin_load)
    OUT = (pin_out,)

    def __init__(self) -> None:
        super().__init__()
        self.mux = Mux()
        self.dff = Dff()
        self.wire_pin(self.pin_clk, self.dff, Dff.pin_clk)
        self.dff.wire_pin(Dff.pin_out, self.mux, Mux.pin_a)
        self.wire_pin(self.pin_in, self.mux, Mux.pin_b)
        self.wire_pin(self.pin_load, self.mux, Mux.pin_sel)
        self.mux.wire_pin(Mux.pin_out, self.dff, Dff.pin_in)
        self.dff.wire_pin(Dff.pin_out, self, self.pin_out)

    def eval(self):
        self.mux.eval()
        self.dff.eval()


def test_bit(
        chip: BitRegister, i: Bit, load: Bit,
        expected_tick_out: Bit, expected_tock_out: Bit
):
    chip.set_pin(BitRegister.pin_in, i)
    chip.set_pin(BitRegister.pin_load, load)
    chip.tick()
    assert chip.clk
    assert chip.output()[BitRegister.pin_out.name] == expected_tick_out
    chip.tock()
    assert not chip.clk
    assert chip.output()[BitRegister.pin_out.name] == expected_tock_out


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
