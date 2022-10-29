from n2t.chip import Bit, Bits, Chip, Pin, Bus
from n2t.dmux import DMux


class DMux4Way(Chip):

    pin_in = Pin('in')
    bus_sel = Bus('sel', 2)
    pin_a = Pin('a')
    pin_b = Pin('b')
    pin_c = Pin('c')
    pin_d = Pin('d')

    IN = (pin_in, bus_sel)
    OUT = (pin_a, pin_b, pin_c, pin_d)

    def __init__(self):
        super().__init__()
        self.dmux1 = DMux()
        self.dmux2 = DMux()
        self.dmux3 = DMux()

        self.wire_pin(self.pin_in, self.dmux1, DMux.pin_in)
        self.wire_pin(self.bus_sel[1], self.dmux1, DMux.pin_sel)
        self.wire_pin(self.bus_sel[0], self.dmux2, DMux.pin_sel)
        self.wire_pin(self.bus_sel[0], self.dmux3, DMux.pin_sel)

        self.dmux1.wire_pin(DMux.pin_a, self.dmux2, DMux.pin_in)
        self.dmux1.wire_pin(DMux.pin_b, self.dmux3, DMux.pin_in)

        self.dmux2.wire_pin(DMux.pin_a, self, self.pin_a)
        self.dmux2.wire_pin(DMux.pin_b, self, self.pin_b)
        self.dmux3.wire_pin(DMux.pin_a, self, self.pin_c)
        self.dmux3.wire_pin(DMux.pin_b, self, self.pin_d)

    def eval(self):
        self.dmux1.eval()
        self.dmux2.eval()
        self.dmux3.eval()


def dmux4way_test_case(
        i: Bit, sel: Bits, expected_a_out: Bit, expected_b_out: Bit,
        expected_c_out: Bit, expected_d_out: Bit,
):
    chip = DMux4Way()
    chip.set_pin(DMux4Way.pin_in, i)
    chip.set_bus(DMux4Way.bus_sel, sel)
    chip.eval()
    assert chip.output()[DMux4Way.pin_a.name] == expected_a_out
    assert chip.output()[DMux4Way.pin_b.name] == expected_b_out
    assert chip.output()[DMux4Way.pin_c.name] == expected_c_out
    assert chip.output()[DMux4Way.pin_d.name] == expected_d_out


def run_all_test_cases():
    dmux4way_test_case(Bit(0), Bits(0b00, 2), Bit(0), Bit(0), Bit(0), Bit(0))
    dmux4way_test_case(Bit(1), Bits(0b00, 2), Bit(1), Bit(0), Bit(0), Bit(0))
    dmux4way_test_case(Bit(0), Bits(0b01, 2), Bit(0), Bit(0), Bit(0), Bit(0))
    dmux4way_test_case(Bit(1), Bits(0b01, 2), Bit(0), Bit(1), Bit(0), Bit(0))
    dmux4way_test_case(Bit(0), Bits(0b10, 2), Bit(0), Bit(0), Bit(0), Bit(0))
    dmux4way_test_case(Bit(1), Bits(0b10, 2), Bit(0), Bit(0), Bit(1), Bit(0))
    dmux4way_test_case(Bit(0), Bits(0b11, 2), Bit(0), Bit(0), Bit(0), Bit(0))
    dmux4way_test_case(Bit(1), Bits(0b11, 2), Bit(0), Bit(0), Bit(0), Bit(1))


if __name__ == '__main__':
    run_all_test_cases()
