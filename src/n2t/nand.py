from .chip import Chip


class Nand(Chip):
    """Nand Gate
    >>> from itertools import product
    >>> chip = Nand()
    >>> for a, b in product((0,1),(0,1)):
    ...    chip.set('a', a)
    ...    chip.set('b', b)
    ...    chip.eval()
    ...    chip.output()
    1
    1
    1
    0
    """

    def __init__(self) -> None:
        super().__init__()
        self.a = None
        self.b = None
        self.out = None
    
    def eval(self):
        self.out = int(not (self.a and self.b))
    
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


if __name__ == '__main__':
    from doctest import testmod
    testmod()
