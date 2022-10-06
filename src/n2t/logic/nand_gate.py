from n2t.logic.unary import UnaryOperation
from n2t.chip import Bit


class Nand(UnaryOperation):
    """Nand Gate
    """
    def __init__(self) -> None:
        super().__init__()

    def eval(self):
        pin_a_value = self.pins[self.pin_a].value
        pin_b_value = self.pins[self.pin_b].value
        self.pins[self.pin_out].value = ~ (pin_a_value & pin_b_value)


def run_all_nand_test_cases():
    test_nand(Bit(0), Bit(0), Bit(1))
    test_nand(Bit(0), Bit(1), Bit(1))
    test_nand(Bit(1), Bit(0), Bit(1))
    test_nand(Bit(1), Bit(1), Bit(0))


def test_nand(a: Bit, b: Bit, expected_out: Bit):
    chip = Nand()
    chip.set(Nand.pin_a, a)
    chip.set(Nand.pin_b, b)
    chip.eval()
    assert chip.output()[Nand.pin_out] == expected_out


if __name__ == '__main__':
    run_all_nand_test_cases()
