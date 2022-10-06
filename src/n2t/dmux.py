from n2t.chip import Bit, Chip, PinName
from n2t.logic.and_gate import And
from n2t.logic.not_gate import Not


class DMux(Chip):

    pin_in = PinName('in')
    pin_sel = PinName('sel')
    pin_a = PinName('a')
    pin_b = PinName('b')

    in_pins = (pin_in, pin_sel)
    out_pins = (pin_a, pin_b)

    def __init__(self):
        super().__init__()
        self.not_gate = Not()
        self.and_gate1 = And()
        self.and_gate2 = And()

        self.wire(self.pin_in, self.and_gate1, And.pin_a)
        self.wire(self.pin_in, self.and_gate2, And.pin_a)
        self.wire(self.pin_sel, self.not_gate, Not.pin_in)
        self.wire(self.pin_sel, self.and_gate2, And.pin_b)
        self.not_gate.wire(Not.pin_out, self.and_gate1, And.pin_b)
        self.and_gate1.wire(And.pin_out, self, self.pin_a)
        self.and_gate2.wire(And.pin_out, self, self.pin_b)

    def eval(self):
        self.not_gate.eval()
        self.and_gate1.eval()
        self.and_gate2.eval()


def test_dmux(i: Bit, sel: Bit, expected_a_out: Bit, expected_b_out: Bit):
    chip = DMux()
    chip.set(DMux.pin_in, i)
    chip.set(DMux.pin_sel, sel)
    chip.eval()
    assert chip.output()[DMux.pin_a] == expected_a_out
    assert chip.output()[DMux.pin_b] == expected_b_out


def run_all_test_cases():
    test_dmux(Bit(0), Bit(0), Bit(0), Bit(0))
    test_dmux(Bit(0), Bit(1), Bit(0), Bit(0))
    test_dmux(Bit(1), Bit(0), Bit(1), Bit(0))
    test_dmux(Bit(1), Bit(1), Bit(0), Bit(1))


if __name__ == '__main__':
    run_all_test_cases()
