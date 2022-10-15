from abc import ABC

from n2t.chip import Chip, Pin


class UnaryOperation(Chip, ABC):
    pin_a = Pin('a')
    pin_b = Pin('b')
    pin_out = Pin('out')

    IN = (pin_a, pin_b)
    OUT = (pin_out,)
