from abc import ABC

from n2t.chip import Chip, PinName


class UnaryOperation(Chip, ABC):
    pin_a = PinName('a')
    pin_b = PinName('b')
    pin_out = PinName('out')

    in_pins: tuple[PinName] = (pin_a, pin_b)
    out_pins: tuple[PinName] = (pin_out,)
