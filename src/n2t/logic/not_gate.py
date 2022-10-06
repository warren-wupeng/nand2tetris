from n2t.chip import Chip, Bit, PinName
from n2t.logic.nand_gate import Nand


class Not(Chip):
    """Not Gate
    not in = in nand in
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


def test_not_gate(i: Bit, expected_out: Bit):

    chip = Not()
    chip.set(Not.pin_in, i)
    chip.eval()
    assert chip.output()[Not.pin_out] == expected_out


def run_not_gate_test_cases():
    test_not_gate(Bit(0), Bit(1))
    test_not_gate(Bit(1), Bit(0))


if __name__ == '__main__':
    run_not_gate_test_cases()
