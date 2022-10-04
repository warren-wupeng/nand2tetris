from n2t.chip import Chip, BitInt, PinName, Pins, Pin
from n2t.nand import Nand


class Not(Chip):
    """Not Gate
    """
    pin_i_name = PinName('i')
    pin_out_name = PinName('out')

    def __init__(self) -> None:
        super().__init__()
        self.in_pins = Pins(Pin(self.pin_i_name))
        self.out_pins = Pins(Pin(self.pin_out_name))
        self.nand = Nand()
        self.wire(self.pin_i_name, self.nand, Nand.pin_a_name)
        self.wire(self.pin_i_name, self.nand, Nand.pin_b_name)
        self.nand.wire(Nand.pin_out_name, self, self.pin_out_name)

    def eval(self):
        self.nand.eval()

    def output(self):
        return self.out_pins[self.pin_out_name].value


def test_not_gate(i: BitInt, expected_out: BitInt):

    chip = Not()
    chip.set(Not.pin_i_name, i)
    chip.eval()
    assert chip.output() == expected_out


def run_not_gate_test_cases():
    test_not_gate(BitInt(0), BitInt(1))
    test_not_gate(BitInt(1), BitInt(0))


if __name__ == '__main__':
    run_not_gate_test_cases()
