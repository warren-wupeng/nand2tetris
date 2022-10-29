from n2t.chip import Bit, Chip, Pin
from n2t.logic.and_gate import And
from n2t.logic.not_gate import Not


class DMux(Chip):

    pin_in = Pin('in')
    pin_sel = Pin('sel')
    pin_a = Pin('a')
    pin_b = Pin('b')

    IN = (pin_in, pin_sel)
    OUT = (pin_a, pin_b)

    def __init__(self):
        super().__init__()
        self.not_gate = Not()
        self.and_gate1 = And()
        self.and_gate2 = And()

        self.wire_pin(self.pin_in, self.and_gate1, And.pin_a)
        self.wire_pin(self.pin_in, self.and_gate2, And.pin_a)
        self.wire_pin(self.pin_sel, self.not_gate, Not.pin_in)
        self.wire_pin(self.pin_sel, self.and_gate2, And.pin_b)
        self.not_gate.wire_pin(Not.pin_out, self.and_gate1, And.pin_b)
        self.and_gate1.wire_pin(And.pin_out, self, self.pin_a)
        self.and_gate2.wire_pin(And.pin_out, self, self.pin_b)

    def eval(self):
        self.not_gate.eval()
        self.and_gate1.eval()
        self.and_gate2.eval()


def dmux_test_case(i: Bit, sel: Bit, expected_a_out: Bit, expected_b_out: Bit):
    chip = DMux()
    chip.set_pin(DMux.pin_in, i)
    chip.set_pin(DMux.pin_sel, sel)
    chip.eval()
    assert chip.output()[DMux.pin_a.name] == expected_a_out
    assert chip.output()[DMux.pin_b.name] == expected_b_out


def run_all_test_cases():
    dmux_test_case(Bit(0), Bit(0), Bit(0), Bit(0))
    dmux_test_case(Bit(0), Bit(1), Bit(0), Bit(0))
    dmux_test_case(Bit(1), Bit(0), Bit(1), Bit(0))
    dmux_test_case(Bit(1), Bit(1), Bit(0), Bit(1))


if __name__ == '__main__':
    run_all_test_cases()
