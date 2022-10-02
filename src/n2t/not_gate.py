from n2t.chip import Chip
from n2t.nand import Nand


class Not(Chip):
    """Not Gate
    """

    def __init__(self) -> None:
        super().__init__()
        self.nand = Nand()
        self.nand.wire('out', self, 'out')
        self.i = 0
        self.out = 0

    def eval(self):
        self.nand.a = self.i
        self.nand.b = self.i
        self.nand.eval()

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


def test_not_gate():
    result = []
    for i in (0, 1):
        chip = Not()
        chip.set('i', i)
        chip.eval()
        result.append(chip.output())
    assert result == [1, 0]


if __name__ == '__main__':
    test_not_gate()
