from chip import Chip
from clock import Clocked
from dff import Dff


class Bit(Chip, Clocked):
    """Bit

    """

    def __init__(self) -> None:
        self.i = 0
        self.load = 0
        self.dff = Dff()
    
    def tick(self):
        pass

    def tock(self):
        pass

def test_bit():
    chip = Bit()
    chip.set('i', 0)
    chip.set('load', 0)
    chip.tick()
    chip.output()


if __name__ == '__main__':
    from doctest import testmod
    testmod()