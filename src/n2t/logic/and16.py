from n2t.chip import Chip, Bus, Bits
from n2t.logic.and_gate import And


class And16(Chip):

    bus_a = Bus('a', 16)
    bus_b = Bus('b', 16)
    bus_out = Bus('out', 16)

    IN = (bus_a, bus_b)
    OUT = (bus_out,)

    def __init__(self):
        super().__init__()
        self.parts = (And(),)*16

        for i, (bus_a_pin, bus_b_pin) in enumerate(zip(self.bus_a, self.bus_b)):
            self.wire_pin(bus_a_pin, self.parts[i], And.pin_a)
            self.wire_pin(bus_b_pin, self.parts[i], And.pin_b)

    def eval(self):
        for part in self.parts:
            part.eval()


def test_and16(a: Bits, b: Bits, expected_out: Bits):
    chip = And16()
    chip.set_bus(And16.bus_a, a)
    chip.set_bus(And16.bus_b, b)
    chip.eval()
    assert chip.output()[And.pin_out] == expected_out


def run_all_test_cases():
    test_and16(Bits(0), Bits(0), Bits(0))
    test_and16(Bits(0), Bits(0b1111111111111111), Bits(0))
    test_and16(
        Bits(0b1111111111111111), Bits(0b1111111111111111),
        Bits(0b1111111111111111)
    )


if __name__ == '__main__':
    run_all_test_cases()
