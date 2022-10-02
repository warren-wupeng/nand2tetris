from clock import Clocked
from chip import Chip



class Dff(Chip, Clocked):
    """Dff
    >>> chip = Dff()
    >>> chip.set('i', 0)
    >>> chip.tick()
    >>> chip.output()
    0
    >>> chip.tock()
    >>> chip.output()
    0
    >>> chip.set('i', 1)
    >>> chip.tick()
    >>> chip.output()
    0
    >>> chip.tock()
    >>> chip.output()
    1
    >>> chip.tick()
    >>> chip.output()
    1
    >>> chip.tock()
    >>> chip.output()
    1
    """

    def __init__(self) -> None:
        self.i = 0
        self.o = 0
        

    def output(self):
        return self.o

    def tick(self):
        pass

    def tock(self):
        self.o = self.i


if __name__ == '__main__':
    from doctest import testmod
    testmod()

