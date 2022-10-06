from clock import ClockedChip
from chip import Bit, PinName


class Dff(ClockedChip):
    """Dff

    """
    pin_in = PinName('in')
    pin_out = PinName('out')

    in_pins = (pin_in,)
    out_pins = (pin_out,)

    def __init__(self) -> None:
        super(Dff, self).__init__()

    def eval(self):
        self.pins[self.pin_out].value = self.pins[self.pin_in].value


def test_dff(
        i: Bit, expected_tick_out: Bit, expected_tock_out: Bit
):
    chip = Dff()
    chip.set(Dff.pin_in, i)
    chip.tick()
    assert chip.output()[Dff.pin_out] == expected_tick_out
    chip.tock()
    assert chip.output()[Dff.pin_out] == expected_tock_out


def run_all_test_cases():
    test_dff(Bit(0), Bit(0), Bit(0))
    test_dff(Bit(1), Bit(0), Bit(1))


if __name__ == '__main__':
    run_all_test_cases()
