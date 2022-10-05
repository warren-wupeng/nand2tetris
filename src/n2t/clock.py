from abc import ABC

from n2t.chip import Chip


class ClockedChip(Chip, ABC):

    def __init__(self):
        super().__init__()
        self.time = 0
        self.plus = ''

    def tick(self):
        assert not self.plus
        self.plus = '+'

    def tock(self):
        assert self.plus
        self.eval()
        self.plus = ''

    def output(self) -> dict:
        result = {'time': f'{self.time}{self.plus}'} | super().output()
        return result
