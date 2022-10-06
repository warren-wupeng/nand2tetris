from n2t.chip import Chip, Bit, PinName
from n2t.logic.nand_gate import Nand
from n2t.logic.not_gate import Not
from n2t.logic.unary import UnaryOperation


class Xor(UnaryOperation):
    """Xor gate
    a xor b = (a and not b) or (not a and b)
            = not ((a and not b) and (not a and b))
            = (a and not b) nand (not a and b)
            = (not (not a and b) nand (not (a and not b))
            = ((not a) nand b) nand (a nand (not b))
    """

    def __init__(self):
        super().__init__()
        self.not1 = Not()
        self.not2 = Not()
        self.nand1 = Nand()
        self.nand2 = Nand()
        self.nand3 = Nand()

        self.wire(self.pin_a, self.not1, Not.pin_in)
        self.wire(self.pin_b, self.not2, Not.pin_in)
        self.wire(self.pin_a, self.nand2, Nand.pin_a)
        self.wire(self.pin_b, self.nand1, Nand.pin_b)

        self.not1.wire(Not.pin_out, self.nand1, Nand.pin_a)
        self.not2.wire(Not.pin_out, self.nand2, Nand.pin_b)

        self.nand1.wire(Nand.pin_out, self.nand3, Nand.pin_a)
        self.nand2.wire(Nand.pin_out, self.nand3, Nand.pin_b)

        self.nand3.wire(Nand.pin_out, self, self.pin_out)

    def eval(self):
        self.not1.eval()
        self.not2.eval()
        self.nand1.eval()
        self.nand2.eval()
        self.nand3.eval()


def run_all_xor_test_cases():
    test_xor(Bit(0), Bit(0), Bit(0))
    test_xor(Bit(0), Bit(1), Bit(1))
    test_xor(Bit(1), Bit(0), Bit(1))
    test_xor(Bit(1), Bit(1), Bit(0))


def test_xor(a: Bit, b: Bit, expected_out: Bit):
    chip = Xor()
    chip.set(Xor.pin_a, a)
    chip.set(Xor.pin_b, b)
    chip.eval()
    assert chip.output()[Xor.pin_out] == expected_out


if __name__ == '__main__':
    run_all_xor_test_cases()