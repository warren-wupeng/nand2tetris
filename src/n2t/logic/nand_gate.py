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


def run_all_nand_test_cases():
    nand_test_case(Bit(0), Bit(0), Bit(1))
    nand_test_case(Bit(0), Bit(1), Bit(1))
    nand_test_case(Bit(1), Bit(0), Bit(1))
    nand_test_case(Bit(1), Bit(1), Bit(0))


def nand_test_case(a: Bit, b: Bit, expected_out: Bit):
    chip = Nand()
    chip.set_pin(Nand.pin_a, a)
    chip.set_pin(Nand.pin_b, b)
    chip.eval()
    assert chip.output()[Nand.pin_out.name] == expected_out


if __name__ == '__main__':
    run_all_nand_test_cases()
