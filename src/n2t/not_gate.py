from n2t.chip import Chip, BitInt, PinName, Pins, Pin
from n2t.nand_gate import Nand


class Not(Chip):
    """Not Gate
    """
    pin_in = PinName('in')
    pin_out = PinName('out')

    in_pins = (pin_in,)
    out_pins = (pin_out,)

    def __init__(self) -> None:
        super().__init__()
        self.nand = Nand()

        self.wire(self.pin_in, self.nand, Nand.pin_a)
        self.wire(self.pin_in, self.nand, Nand.pin_b)
        self.nand.wire(Nand.pin_out, self, self.pin_out)

    def eval(self):
        self.nand.eval()


def test_not_gate(i: BitInt, expected_out: BitInt):

    chip = Not()
    chip.set(Not.pin_in, i)
    chip.eval()
    assert chip.output()[Not.pin_out] == expected_out


def run_not_gate_test_cases():
    test_not_gate(BitInt(0), BitInt(1))
    test_not_gate(BitInt(1), BitInt(0))


if __name__ == '__main__':
    run_not_gate_test_cases()
