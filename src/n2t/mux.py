from n2t.and_gate import And
from n2t.chip import BitInt, Chip, PinName, Pins, Pin
from n2t.not_gate import Not
from n2t.or_gate import Or


class Mux(Chip):
    pin_a = PinName('a')
    pin_b = PinName('b')
    pin_sel = PinName('sel')
    pin_out = PinName('out')

    in_pins = (pin_a, pin_b, pin_sel)
    out_pins = (pin_out,)

    def __init__(self):
        super().__init__()
        self.not_gate = Not()
        self.and_gate1 = And()
        self.and_gate2 = And()
        self.or_gate = Or()

        self.wire(self.pin_sel, self.not_gate, Not.pin_out)
        self.wire(self.pin_a, self.and_gate1, And.pin_a)
        self.not_gate.wire(Not.pin_out, self.and_gate1, And.pin_out)
        self.wire(self.pin_b, self.and_gate2, And.pin_a)
        self.wire(self.pin_sel, self.and_gate2, And.pin_b)
        self.and_gate1.wire(self.pin_out, self.or_gate, Or.pin_a)
        self.and_gate2.wire(self.pin_out, self.or_gate, Or.pin_b)
        self.or_gate.wire(self.pin_out, self, self.pin_out)

    def eval(self):
        self.not_gate.eval()
        self.and_gate1.eval()
        self.and_gate2.eval()
        self.or_gate.eval()


def test_mux(a: BitInt, b: BitInt, sel: BitInt, expected_out: BitInt):
    chip = Mux()
    chip.set(Mux.pin_a, a)
    chip.set(Mux.pin_b, b)
    chip.set(Mux.pin_sel, sel)
    chip.eval()
    assert chip.output()[Mux.pin_out] == expected_out


def run_all_test_cases():
    test_mux(a=BitInt(0), b=BitInt(1), sel=BitInt(0), expected_out=BitInt(0))
    test_mux(a=BitInt(0), b=BitInt(1), sel=BitInt(1), expected_out=BitInt(1))


if __name__ == '__main__':
    run_all_test_cases()
