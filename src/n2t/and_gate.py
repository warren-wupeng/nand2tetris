from n2t.chip import Chip, BinaryBit, PinName, Pins, Pin
from n2t.not_gate import Not
from n2t.nand_gate import Nand


class And(Chip):
    """And Gate"""
    pin_a = PinName('a')
    pin_b = PinName('b')
    pin_out = PinName('out')

    in_pins = (pin_a, pin_b)
    out_pins = (pin_out,)

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


def test_and(a: BinaryBit, b: BinaryBit, expected_out: BinaryBit):
    chip = And()
    chip.set(And.pin_a, a)
    chip.set(And.pin_b, b)
    chip.eval()
    assert chip.output()[And.pin_out] == expected_out


def run_all_and_test_cases():
    test_and(BinaryBit(0), BinaryBit(0), BinaryBit(0))
    test_and(BinaryBit(0), BinaryBit(1), BinaryBit(0))
    test_and(BinaryBit(1), BinaryBit(0), BinaryBit(0))
    test_and(BinaryBit(1), BinaryBit(1), BinaryBit(1))


if __name__ == '__main__':
    run_all_and_test_cases()
