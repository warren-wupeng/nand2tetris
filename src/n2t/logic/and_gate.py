from n2t.chip import Chip, Bit, PinName
from n2t.logic.not_gate import Not
from n2t.logic.nand_gate import Nand
from n2t.logic.unary import UnaryOperation


class And(UnaryOperation):
    """And Gate
    a and b = not (a nand b)
    """

    def __init__(self) -> None:
        super().__init__()
        self.nand = Nand()
        self.not_gate = Not()

        self.wire(self.pin_a, self.nand, Nand.pin_a)
        self.wire(self.pin_b, self.nand, Nand.pin_b)
        self.nand.wire(Nand.pin_out, self.not_gate, Not.pin_in)
        self.not_gate.wire(Not.pin_out, self, self.pin_out)

    def eval(self):
        self.nand.eval()
        self.not_gate.eval()


def test_and(a: Bit, b: Bit, expected_out: Bit):
    chip = And()
    chip.set(And.pin_a, a)
    chip.set(And.pin_b, b)
    chip.eval()
    assert chip.output()[And.pin_out] == expected_out


def run_all_and_test_cases():
    test_and(Bit(0), Bit(0), Bit(0))
    test_and(Bit(0), Bit(1), Bit(0))
    test_and(Bit(1), Bit(0), Bit(0))
    test_and(Bit(1), Bit(1), Bit(1))


if __name__ == '__main__':
    run_all_and_test_cases()
