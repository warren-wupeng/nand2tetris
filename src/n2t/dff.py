from n2t.clock import ClockedChip
from n2t.chip import Bit, Pin
from n2t.logic.nand_gate import Nand
from n2t.logic.not_gate import Not


class Dff(ClockedChip):
    """Dff

    """
    pin_in = Pin('in')
    pin_out = Pin('out')

    IN = (pin_in,)
    OUT = (pin_out,)

    def __init__(self) -> None:
        super().__init__()
        self.not_gate = Not()
        self.nand1 = Nand()
        self.nand2 = Nand()
        self.nand3 = Nand()
        self.nand4 = Nand()

        self.wire_pin(self.pin_in, self.not_gate, Not.pin_in)

        self.wire_pin(self.pin_in, self.nand1, Nand.pin_a)
        self.wire_pin(self.pin_clk, self.nand1, Nand.pin_b)

        self.not_gate.wire_pin(Not.pin_out, self.nand2, Nand.pin_a)
        self.wire_pin(self.pin_clk, self.nand2, Nand.pin_b)

        self.nand1.wire_pin(Nand.pin_out, self.nand3, Nand.pin_a)
        self.nand2.wire_pin(Nand.pin_out, self.nand4, Nand.pin_a)

        self.nand3.wire_pin(Nand.pin_out, self.nand4, Nand.pin_b)
        self.nand4.wire_pin(Nand.pin_out, self.nand3, Nand.pin_b)

        self.nand3.wire_pin(Nand.pin_out, self, self.pin_out)

    def eval(self):
        self.not_gate.eval()
        self.nand1.eval()
        self.nand2.eval()
        self.nand3.eval()
        self.nand4.eval()
        self.nand3.eval()
        self.nand4.eval()


def test_dff(
        chip: Dff, i: Bit, expected_tick_out: Bit, expected_tock_out: Bit
):

    chip.set_pin(Dff.pin_in, i)
    chip.tick()
    assert chip.output()[Dff.pin_out.name] == expected_tick_out
    chip.tock()
    assert chip.output()[Dff.pin_out.name] == expected_tock_out


def run_all_test_cases():
    chip = Dff()
    test_dff(chip, Bit(0), Bit(0), Bit(0))
    test_dff(chip, Bit(1), Bit(0), Bit(1))
    chip.tick()
    chip.tock()
    test_dff(chip, Bit(0), Bit(1), Bit(0))


if __name__ == '__main__':
    run_all_test_cases()
