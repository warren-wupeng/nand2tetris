from n2t.chip import Chip, Pin
from n2t.bit import Bit
from n2t.logic.and_gate import And
from n2t.logic.not_gate import Not
from n2t.logic.or_gate import Or


class Mux(Chip):
    pin_a = Pin('a')
    pin_b = Pin('b')
    pin_sel = Pin('sel')
    pin_out = Pin('out')

    IN = (pin_a, pin_b, pin_sel)
    OUT = (pin_out,)

    def __init__(self):
        super().__init__()
        self.not_gate = Not()
        self.and_gate1 = And()
        self.and_gate2 = And()
        self.or_gate = Or()

        self.wire_pin(self.pin_a, self.and_gate1, And.pin_a)
        self.wire_pin(self.pin_b, self.and_gate2, And.pin_a)
        self.wire_pin(self.pin_sel, self.not_gate, Not.pin_in)
        self.wire_pin(self.pin_sel, self.and_gate2, And.pin_b)
        self.not_gate.wire_pin(Not.pin_out, self.and_gate1, And.pin_b)
        self.and_gate1.wire_pin(self.pin_out, self.or_gate, Or.pin_a)
        self.and_gate2.wire_pin(self.pin_out, self.or_gate, Or.pin_b)
        self.or_gate.wire_pin(self.pin_out, self, self.pin_out)

    def eval(self):
        self.not_gate.eval()
        self.and_gate1.eval()
        self.and_gate2.eval()
        self.or_gate.eval()


def test_mux(a: Bit, b: Bit, sel: Bit, expected_out: Bit):
    chip = Mux()
    chip.set_pin(Mux.pin_a, a)
    chip.set_pin(Mux.pin_b, b)
    chip.set_pin(Mux.pin_sel, sel)
    chip.eval()
    assert chip.output()[Mux.pin_out.name] == expected_out


def run_all_test_cases():
    test_mux(a=Bit(0), b=Bit(1), sel=Bit(0), expected_out=Bit(0))
    test_mux(a=Bit(0), b=Bit(1), sel=Bit(1), expected_out=Bit(1))
    test_mux(a=Bit(1), b=Bit(0), sel=Bit(1), expected_out=Bit(0))
    test_mux(a=Bit(1), b=Bit(0), sel=Bit(0), expected_out=Bit(1))


if __name__ == '__main__':
    run_all_test_cases()
