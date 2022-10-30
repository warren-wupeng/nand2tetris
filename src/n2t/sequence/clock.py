from abc import ABC

from n2t.chip import Chip, Pin
from n2t.bit import Bit


class ClockedChip(Chip, ABC):

    pin_clk = Pin('clk')

    def __init__(self):
        super().__init__()
        self.time = 0
        self.pin_values[self.pin_clk.name] = Bit(0)
        self.pin_wires[self.pin_clk.name] = []

    @property
    def clk(self):
        return self.pin_values[self.pin_clk.name]

    @clk.setter
    def clk(self, value: Bit):
        self.set_pin(self.pin_clk, value)

    def tick(self):
        # pass
        assert not self.clk
        self.clk = ~ self.clk

    def tock(self):
        assert self.clk
        self.time += 1
        self.eval()
        self.clk = ~ self.clk

    def output(self) -> dict:
        result = super().output() | {
            'time': f'{self.time}{"+" if self.clk else ""}'}
        return result
