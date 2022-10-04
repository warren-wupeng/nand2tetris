from n2t.chip import Chip, PinName, Pin, Pins, BitInt


class Nand(Chip):
    """Nand Gate
    """
    pin_a_name = PinName('a')
    pin_b_name = PinName('b')
    pin_out_name = PinName('out')

    def __init__(self) -> None:
        super().__init__()
        self.in_pins = Pins(Pin(self.pin_a_name), Pin(self.pin_b_name))
        self.out_pins = Pins(Pin(self.pin_out_name))

    def eval(self):
        pin_a_value = self.in_pins[self.pin_a_name].value
        pin_b_value = self.in_pins[self.pin_b_name].value
        self.out_pins[self.pin_out_name].value = ~ (pin_a_value & pin_b_value)

    def output(self):
        return self.out_pins[self.pin_out_name].value


def run_all_nand_test_cases():
    test_nand(BitInt(0), BitInt(0), BitInt(1))
    test_nand(BitInt(0), BitInt(1), BitInt(1))
    test_nand(BitInt(1), BitInt(0), BitInt(1))
    test_nand(BitInt(1), BitInt(1), BitInt(0))


def test_nand(a: BitInt, b: BitInt, expected_out: BitInt):
    chip = Nand()
    chip.set(Nand.pin_a_name, a)
    chip.set(Nand.pin_b_name, b)
    chip.eval()
    assert chip.output() == expected_out


if __name__ == '__main__':
    run_all_nand_test_cases()
