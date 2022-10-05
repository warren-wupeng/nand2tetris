from n2t.and_gate import And
from n2t.chip import BitInt, Chip, PinName, Pins, Pin
from n2t.nand_gate import Nand
from n2t.not_gate import Not


class Or(Chip):
    """Or Gate"""
    pin_a = PinName('a')
    pin_b = PinName('b')
    pin_out = PinName('out')

    in_pins = (pin_a, pin_b)
    out_pins = (pin_out,)

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
    test_or(BitInt(0), BitInt(0), BitInt(0))
    test_or(BitInt(0), BitInt(1), BitInt(1))
    test_or(BitInt(1), BitInt(0), BitInt(1))
    test_or(BitInt(1), BitInt(1), BitInt(1))


def test_or(a: BitInt, b: BitInt, expected_out: BitInt):
    chip = Or()
    chip.set(Or.pin_a, a)
    chip.set(Or.pin_b, b)
    chip.eval()
    assert chip.output()[Or.pin_out] == expected_out


if __name__ == '__main__':
    run_all_or_test_cases()
