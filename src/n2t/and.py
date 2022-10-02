from .chip import Chip
from .not_gate import Not
from .nand import Nand
from itertools import product


class And(Chip):
    """And Gate"""
    def __init__(self) -> None:
        super().__init__()
        self.nand = Nand()
        self.not_gate = Not()
        self.nand.wire('out', self.not_gate, 'i')
        self.not_gate.wire('out', self, 'out')
        self.a = 0
        self.b = 0
        self.out = 0

    def eval(self):
        self.nand.a = self.a
        self.nand.b = self.b
        self.nand.eval()
        self.not_gate.eval()

    def output(self):
        return self.out

    @property
    def out(self):
        return self._out

    @out.setter
    def out(self, value):
        self._out = value
        for chip, pin in self.wires['out']:
            setattr(chip, pin, value)


def test_and():
    chip = And()
    result = []
    for a, b in product((0, 1), (0, 1)):
        chip.set('a', a)
        chip.set('b', b)
        chip.eval()
        result.append(chip.output())
    assert result == [0, 0, 0, 1]


if __name__ == '__main__':
    test_and()
