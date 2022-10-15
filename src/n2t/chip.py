import abc
from typing import Any, Union


class Bit:
    def __init__(self, value: int = 0):
        assert value in (0, 1)
        self.value = value

    def __and__(self, other):
        result = Bit(self.value & other.value)
        return result

    def __eq__(self, other):
        return self.value == other.value

    def __invert__(self):
        return Bit(0 if self.value else 1)

    def __repr__(self):
        return f'Bit({self.value})'


def test_bit_int():
    assert Bit(0) & Bit(0) == Bit(0)
    assert Bit(0) & Bit(1) == Bit(0)
    assert Bit(1) & Bit(0) == Bit(0)
    assert Bit(1) & Bit(1) == Bit(1)


class Bits:
    def __init__(self, value: int = 0, size: int = 16):
        assert value < int('1'*size, 2)
        self.value = value
        self.size = size

    def __getitem__(self, index: int):
        digit = (self.value & (1 << index)) >> index
        return Bit(digit)

    def __setitem__(self, index: int, bit: Bit):
        if bit.value:
            self.value = self.value | (1 << index)
        else:
            self.value = self.value & ~ (1 << index)


def get_bit(value: int, size: int = 1):
    if size == 1:
        return Bit(value)
    elif size == 16:
        return Bits(value, 16)
    else:
        raise ValueError()


def test_bit16():
    assert Bits(0b1)[0] == Bit(1)
    assert Bits(0b1)[1] == Bit(0)
    bits = Bits(0b1)
    bits[1] = Bit(1)
    assert bits[1] == Bit(1)
    bits[0] = Bit(0)
    assert bits[0] == Bit(0)


class Pin:

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"Pin(name={self.name})"


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
        return f"Bus(name={self.name}, size={self.size})"


PinOrBus = Union[Pin, Bus]


class Chip(abc.ABC):

    IN: tuple[PinOrBus]
    OUT: tuple[PinOrBus]

    def __init__(self) -> None:
        self.pin_values = dict()
        self.pin_wires = dict()

        for pin_or_bus in self.IN + self.OUT:
            if isinstance(pin_or_bus, Pin):
                self.pin_values[pin_or_bus.name] = Bit()
                self.pin_wires[pin_or_bus.name] = []
            if isinstance(pin_or_bus, Bus):
                for pin in pin_or_bus:
                    self.pin_values[pin.name] = Bit()
                    self.pin_wires[pin.name] = []

    def set_pin(self, pin: Pin, value: Bit):
        self.pin_values[pin.name] = value
        for chip, pin in self.pin_wires[pin.name]:
            chip.set_pin(pin, value)

    def set_bus(self, bus: Bus, value: Bits):
        assert bus.size == value.size
        for i, pin in enumerate(bus):
            self.set_pin(pin, value[i])

    def wire_pin(self, pin: Pin, chip: Any, to_pin: Pin):
        self.pin_wires[pin.name].append((chip, to_pin))

    def wire_bus(self, bus: Bus, chip: Any, to_bus: Bus):
        assert bus.size == to_bus.size
        for i, pin in enumerate(bus):
            self.pin_wires[pin].append((chip, to_bus[i]))

    def eval(self):
        raise NotImplementedError

    def output(self) -> dict[str, Bit]:
        return self.pin_values

    def __repr__(self):
        return f'{self.__class__.__name__}(IN={self.IN}, OUT={self.OUT})'


if __name__ == '__main__':
    test_bit_int()
    test_bit16()
