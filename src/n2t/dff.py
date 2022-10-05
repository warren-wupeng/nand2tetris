from clock import Clocked
from chip import Chip, BitInt, PinName, Pins, Pin


class Dff(Chip, Clocked):
    """Dff

    """
    pin_i = PinName('i')
    pin_out = PinName('out')

    in_pins = (pin_i,)
    out_pins = (pin_out,)

    def __init__(self) -> None:
        super().__init__()

    def eval(self):
        self.pins[self.pin_out].value = self.pins[self.pin_i].value

    def output(self):
        return self.pins[self.pin_out].value

    def tick(self):
        pass

    def tock(self):
        self.eval()


def test_dff(i: BitInt, expected_tick_out: BitInt, expected_tock_out: BitInt):
    chip = Dff()
    chip.set(Dff.pin_i, i)
    chip.tick()
    assert chip.output() == expected_tick_out
    chip.tock()
    assert chip.output() == expected_tock_out


def run_all_test_cases():
    test_dff(BitInt(0), BitInt(0), BitInt(0))
    test_dff(BitInt(1), BitInt(0), BitInt(1))


if __name__ == '__main__':
    run_all_test_cases()

