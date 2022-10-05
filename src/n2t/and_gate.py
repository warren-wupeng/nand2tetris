from n2t.chip import Chip, BitInt, PinName, Pins, Pin
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
        self.nand.wire(Nand.pin_out, self.not_gate, Not.pin_i)
        self.not_gate.wire(Not.pin_out, self, self.pin_out)

    def eval(self):
        self.nand.eval()
        self.not_gate.eval()

    def output(self):
        return self.pins[self.pin_out].value


def test_and(a: BitInt, b: BitInt, expected_out: BitInt):
    chip = And()
    chip.set(And.pin_a, a)
    chip.set(And.pin_b, b)
    chip.eval()
    assert chip.output() == expected_out


def run_all_and_test_cases():
    test_and(BitInt(0), BitInt(0), BitInt(0))
    test_and(BitInt(0), BitInt(1), BitInt(0))
    test_and(BitInt(1), BitInt(0), BitInt(0))
    test_and(BitInt(1), BitInt(1), BitInt(1))


if __name__ == '__main__':
    run_all_and_test_cases()
