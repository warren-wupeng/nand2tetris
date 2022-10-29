from n2t.bitregister import BitRegister
from n2t.chip import Bit, Bits, Bus, Pin
from n2t.clock import ClockedChip


class Register(ClockedChip):

    bus_in = Bus('in')
    pin_load = Pin('load')
    bus_out = Bus('out')
    IN = (bus_in, pin_load)
    OUT = (bus_out,)

    def __init__(self):
        super().__init__()
        self.parts = tuple(BitRegister() for _ in range(16))

        for i, bus_in_pin in enumerate(self.bus_in):
            self.wire_pin(bus_in_pin, self.parts[i], BitRegister.pin_in)
            self.wire_pin(self.pin_load, self.parts[i], BitRegister.pin_load)
            self.wire_pin(self.pin_clk, self.parts[i], BitRegister.pin_clk)
            self.parts[i].wire_pin(BitRegister.pin_out, self, self.bus_out[i])

    def eval(self):
        for part in self.parts:
            part.eval()

    def output(self) -> dict[str, Bits]:
        return {'out': self.bus_values[self.bus_out.name]}


def test_bit(
        chip: Register, i: Bits, load: Bit,
        expected_tick_out: Bits, expected_tock_out: Bits
):
    chip.set_bus(Register.bus_in, i)
    chip.set_pin(Register.pin_load, load)
    chip.tick()
    assert chip.clk
    assert chip.output()[Register.bus_out.name] == expected_tick_out
    chip.tock()
    assert not chip.clk
    assert chip.output()[Register.bus_out.name] == expected_tock_out


def run_all_test_cases():
    chip = Register()
    test_bit(chip, Bits(0), Bit(0), Bits(0), Bits(0))
    test_bit(chip, Bits(0), Bit(1), Bits(0), Bits(0))
    test_bit(chip, Bits(1), Bit(0), Bits(0), Bits(0))
    test_bit(chip, Bits(1), Bit(1), Bits(0), Bits(1))
    test_bit(chip, Bits(0), Bit(0), Bits(1), Bits(1))
    test_bit(chip, Bits(1), Bit(0), Bits(1), Bits(1))
    test_bit(chip, Bits(0), Bit(1), Bits(1), Bits(0))
    test_bit(chip, Bits(0b10), Bit(1), Bits(0), Bits(0b10))
    test_bit(chip, Bits(0b11), Bit(1), Bits(0b10), Bits(0b11))


if __name__ == '__main__':
    run_all_test_cases()
