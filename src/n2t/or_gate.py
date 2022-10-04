from n2t.and_gate import And
from n2t.chip import BitInt, Chip, PinName, Pins, Pin
from n2t.nand_gate import Nand
from n2t.not_gate import Not


class Or(Chip):
    """Or Gate"""
    pin_a_name = PinName('a')
    pin_b_name = PinName('b')
    pin_out_name = PinName('out')

    def __init__(self) -> None:
        super().__init__()
        self.in_pins = Pins(Pin(self.pin_a_name), Pin(self.pin_b_name))
        self.out_pins = Pins(Pin(self.pin_out_name))

        self.not_gate_a = Not()
        self.not_gate_b = Not()
        self.nand = Nand()

        self.wire(self.pin_a_name, self.not_gate_a, Not.pin_i_name)
        self.wire(self.pin_b_name, self.not_gate_b, Not.pin_i_name)
        self.not_gate_a.wire(Not.pin_out_name, self.nand, Nand.pin_a_name)
        self.not_gate_b.wire(Not.pin_out_name, self.nand, Nand.pin_b_name)
        self.nand.wire(Nand.pin_out_name, self, self.pin_out_name)

    def eval(self):
        self.not_gate_a.eval()
        self.not_gate_b.eval()
        self.nand.eval()

    def output(self):
        return self.out_pins[self.pin_out_name].value


def run_all_or_test_cases():
    test_or(BitInt(0), BitInt(0), BitInt(0))
    test_or(BitInt(0), BitInt(1), BitInt(1))
    test_or(BitInt(1), BitInt(0), BitInt(1))
    test_or(BitInt(1), BitInt(1), BitInt(1))


def test_or(a: BitInt, b: BitInt, expected_out: BitInt):
    chip = Or()
    chip.set(Or.pin_a_name, a)
    chip.set(Or.pin_b_name, b)
    chip.eval()
    assert chip.output() == expected_out


if __name__ == '__main__':
    run_all_or_test_cases()
