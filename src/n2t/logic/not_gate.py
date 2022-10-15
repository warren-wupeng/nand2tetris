from n2t.chip import Chip, Bit, Pin
from n2t.logic.nand_gate import Nand


class Not(Chip):
    """Not Gate
    not in = in nand in
    """
    pin_in = Pin('in')
    pin_out = Pin('out')

    IN = (pin_in,)
    OUT = (pin_out,)

    def __init__(self) -> None:
        super().__init__()
        self.nand = Nand()

        self.wire_pin(self.pin_in, self.nand, Nand.pin_a)
        self.wire_pin(self.pin_in, self.nand, Nand.pin_b)
        self.nand.wire_pin(Nand.pin_out, self, self.pin_out)

    def eval(self):
        self.nand.eval()


def test_not_gate(i: Bit, expected_out: Bit):

    chip = Not()
    chip.set_pin(Not.pin_in, i)
    chip.eval()
    out = chip.output()[Not.pin_out.name]
    assert out == expected_out, f"{out}!={expected_out}"


def run_not_gate_test_cases():
    test_not_gate(Bit(0), Bit(1))
    test_not_gate(Bit(1), Bit(0))


if __name__ == '__main__':
    run_not_gate_test_cases()
