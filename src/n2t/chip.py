import abc
import re
from typing import Any, Union
import unittest

from n2t.bit import Bit


class Bits:
    def __init__(self, value: int = 0, size: int = 16):
        if value < 0 or value > int('1'*size, 2):
            raise ValueError(f"{value}")
        self.value = value
        self.size = size

    def __eq__(self, other):

        return isinstance(other, Bits) and self.value == other.value

    def __getitem__(self, index: int):
        digit = (self.value & (1 << index)) >> index
        return Bit(digit)

    def __setitem__(self, index: int, bit: Bit):
        if bit.value:
            self.value = self.value | (1 << index)
        else:
            self.value = self.value & ~ (1 << index)

    def __repr__(self):
        return f'Bits({self.value:0{self.size}b})'


class TestBits(unittest.TestCase):

    def test_should_not_accept_negative_value(self):
        with self.assertRaises(ValueError):
            Bits(-1)


def test_bits():
    assert Bits(0) == Bits(0)
    assert Bits(1) == Bits(1)
    assert Bits(0b1)[0] == Bit(1)
    assert Bits(0b1)[1] == Bit(0)
    bits = Bits(0b1)
    bits[1] = Bit(1)
    assert bits[1] == Bit(1)
    bits[0] = Bit(0)
    assert bits[0] == Bit(0)
    assert str(Bits(0)) == "Bits(0000000000000000)", str(Bits(0))
    assert str(Bits(1)) == "Bits(0000000000000001)"
    assert str(Bits(2)) == "Bits(0000000000000010)"


class Pin:

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"Pin('{self.name}')"

    def __eq__(self, other):
        return isinstance(other, Pin) and self.name == other.name


def test_pin():
    assert str(Pin('a')) == "Pin('a')"


class Bus:
    def __init__(self, name: str, size: int = 16):
        self.name = name
        self.size = size

    def __getitem__(self, item):
        if isinstance(item, slice):
            return tuple(
                Pin(self.name+f"[{x}]") for x in range(item.start, item.stop)
            )
        elif isinstance(item, int):
            assert 0 <= item < self.size
            return Pin(self.name+f"[{item}]")
        else:
            raise ValueError(f"{item}")

    def __iter__(self):
        for i in range(self.size):
            yield Pin(self.name+f"[{i}]")

    def __repr__(self):
        return f"Bus('{self.name}', {self.size})"


def test_bus():
    assert Bus('a')[0] == Pin('a[0]')
    assert Bus('a')[1] == Pin('a[1]')
    assert str(Bus('a')) == "Bus('a', 16)"


PinOrBus = Union[Pin, Bus]


class Chip(abc.ABC):

    IN: tuple[PinOrBus]
    OUT: tuple[PinOrBus]

    def __init__(self) -> None:
        self.pin_values = dict()
        self.pin_wires = dict()
        self.bus_values = dict()

        for pin_or_bus in self.IN + self.OUT:
            if isinstance(pin_or_bus, Pin):
                self.pin_values[pin_or_bus.name] = Bit()
                self.pin_wires[pin_or_bus.name] = []
            if isinstance(pin_or_bus, Bus):
                self.bus_values[pin_or_bus.name] = Bits()
                for pin in pin_or_bus:
                    self.pin_wires[pin.name] = []

    def set_pin(self, pin: Pin, value: Bit):

        if pin.name in self.pin_values:

            self.pin_values[pin.name] = value

        elif m := re.match(r"([a-z]+)\[(\d+)\]", pin.name):
            self.bus_values[m.groups()[0]][int(m.groups()[1])] = value
        else:
            raise KeyError(f"{pin=}")

        for chip, pin in self.pin_wires[pin.name]:
            chip.set_pin(pin, value)

    def set_bus(self, bus: Bus, value: Bits):
        assert bus.size == value.size
        self.bus_values[bus.name] = value
        for index, pin in enumerate(bus):
            for chip, to_pin in self.pin_wires[pin.name]:
                chip.set_pin(to_pin, value[index])

    def wire_pin(self, pin: Pin, chip: Any, to_pin: Pin):
        self.pin_wires[pin.name].append((chip, to_pin))

    def wire_bus(self, bus: Bus, chip: Any, to_bus: Bus):
        assert bus.size == to_bus.size
        for i, pin in enumerate(bus):
            self.pin_wires[pin].append((chip, to_bus[i]))

    def eval(self):
        raise NotImplementedError

    def output(self) -> dict[str, Bit]:
        return self.pin_values | self.bus_values

    def __repr__(self):
        return f"{self.pin_values | self.bus_values}"


if __name__ == '__main__':
    test_bits()
    test_pin()
    test_bus()
    unittest.main()
