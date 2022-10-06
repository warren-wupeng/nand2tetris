from n2t.chip import Bit, Chip, PinName
from n2t.logic.nand_gate import Nand
from n2t.logic.not_gate import Not
from n2t.logic.unary import UnaryOperation


class Or(UnaryOperation):
    """Or Gate
    a or b = (not (not a)) or (not (not b))
           = not (not a) and (not b)
           = (not a) nand (not b)
    """

    def __init__(self) -> None:
        super().__init__()
        self.not_gate_a = Not()
        self.not_gate_b = Not()
        self.nand = Nand()

        self.wire(self.pin_a, self.not_gate_a, Not.pin_in)
        self.wire(self.pin_b, self.not_gate_b, Not.pin_in)
        self.not_gate_a.wire(Not.pin_out, self.nand, Nand.pin_a)
        self.not_gate_b.wire(Not.pin_out, self.nand, Nand.pin_b)
        self.nand.wire(Nand.pin_out, self, self.pin_out)

    def eval(self):
        self.not_gate_a.eval()
        self.not_gate_b.eval()
        self.nand.eval()


def run_all_or_test_cases():
    test_or(Bit(0), Bit(0), Bit(0))
    test_or(Bit(0), Bit(1), Bit(1))
    test_or(Bit(1), Bit(0), Bit(1))
    test_or(Bit(1), Bit(1), Bit(1))


def test_or(a: Bit, b: Bit, expected_out: Bit):
    chip = Or()
    chip.set(Or.pin_a, a)
    chip.set(Or.pin_b, b)
    chip.eval()
    assert chip.output()[Or.pin_out] == expected_out


if __name__ == '__main__':
    run_all_or_test_cases()
