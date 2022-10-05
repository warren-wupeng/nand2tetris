from n2t.chip import Chip, PinName, Pin, Pins, BitInt
from collections import namedtuple
from enum import Enum

class Nand(Chip):
    """Nand Gate
    """

    pin_a = PinName('a')
    pin_b = PinName('b')
    pin_out = PinName('out')

    in_pins: tuple[PinName] = (pin_a, pin_b)
    out_pins: tuple[PinName] = (pin_out,)

    def __init__(self) -> None:
        super().__init__()

    def eval(self):
        pin_a_value = self.pins[self.pin_a].value
        pin_b_value = self.pins[self.pin_b].value
        self.pins[self.pin_out].value = ~ (pin_a_value & pin_b_value)

    def output(self):
        return self.pins[self.pin_out].value


def run_all_nand_test_cases():
    test_nand(BitInt(0), BitInt(0), BitInt(1))
    test_nand(BitInt(0), BitInt(1), BitInt(1))
    test_nand(BitInt(1), BitInt(0), BitInt(1))
    test_nand(BitInt(1), BitInt(1), BitInt(0))


def test_nand(a: BitInt, b: BitInt, expected_out: BitInt):
    chip = Nand()
    chip.set(Nand.pin_a, a)
    chip.set(Nand.pin_b, b)
    chip.eval()
    assert chip.output() == expected_out


if __name__ == '__main__':
    run_all_nand_test_cases()
