from n2t.chip import Chip, BitInt, PinName, Pins, Pin
from n2t.not_gate import Not
from n2t.nand_gate import Nand


class And(Chip):
    """And Gate"""
    pin_a_name = PinName('a')
    pin_b_name = PinName('b')
    pin_out_name = PinName('out')

    def __init__(self) -> None:
        super().__init__()
        self.in_pins = Pins(Pin(self.pin_a_name), Pin(self.pin_b_name))
        self.out_pins = Pins(Pin(self.pin_out_name))

        self.nand = Nand()
        self.not_gate = Not()

        self.wire(self.pin_a_name, self.nand, Nand.pin_a_name)
        self.wire(self.pin_b_name, self.nand, Nand.pin_b_name)
        self.nand.wire(Nand.pin_out_name, self.not_gate, Not.pin_i_name)
        self.not_gate.wire(Not.pin_out_name, self, self.pin_out_name)

    def eval(self):
        self.nand.eval()
        self.not_gate.eval()

    def output(self):
        return self.out_pins[self.pin_out_name].value


def run_all_and_test_cases():
    test_and(BitInt(0), BitInt(0), BitInt(0))
    test_and(BitInt(0), BitInt(1), BitInt(0))
    test_and(BitInt(1), BitInt(0), BitInt(0))
    test_and(BitInt(1), BitInt(1), BitInt(1))


def test_and(a: BitInt, b: BitInt, expected_out: BitInt):
    chip = And()
    chip.set(And.pin_a_name, a)
    chip.set(And.pin_b_name, b)
    chip.eval()
    assert chip.output() == expected_out


if __name__ == '__main__':
    run_all_and_test_cases()
