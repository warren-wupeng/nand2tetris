import unittest

from n2t.logic.unary import UnaryOperation
from n2t.bit import Bit


class Nand(UnaryOperation):
    """Nand Gate
    """
    def __init__(self) -> None:
        super().__init__()

    def eval(self):
        pin_a_value = self.pin_values[self.pin_a.name]
        pin_b_value = self.pin_values[self.pin_b.name]
        self.set_pin(self.pin_out, ~ (pin_a_value & pin_b_value))


class TestNand(unittest.TestCase):

    def test_should_output_1_given_0_and_0(self):
        self.nand_test_case(Bit(0), Bit(0), Bit(1))

    def test_should_output_1_given_0_and_1(self):
        self.nand_test_case(Bit(0), Bit(1), Bit(1))

    def test_should_output_1_given_1_and_0(self):
        self.nand_test_case(Bit(1), Bit(0), Bit(1))

    def test_should_output_0_given_1_and_1(self):
        self.nand_test_case(Bit(1), Bit(1), Bit(0))

    def nand_test_case(self, a: Bit, b: Bit, expected_out: Bit):
        chip = Nand()
        chip.set_pin(Nand.pin_a, a)
        chip.set_pin(Nand.pin_b, b)
        chip.eval()
        self.assertEqual(chip.output()[Nand.pin_out.name], expected_out)


if __name__ == '__main__':
    unittest.main()
