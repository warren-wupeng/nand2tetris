import abc

from typing import NewType, Any, Optional

PinName = NewType('PinName', str)


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
        return f'BinaryBit({self.value})'


def test_bit_int():
    assert Bit(0) & Bit(0) == Bit(0)
    assert Bit(0) & Bit(1) == Bit(0)
    assert Bit(1) & Bit(0) == Bit(0)
    assert Bit(1) & Bit(1) == Bit(1)


class Pin:

    def __init__(self, name: PinName):
        self.name = name
        self._value: Bit = Bit()
        self.wired_pins: list[tuple[Any, PinName]] = []

    @property
    def value(self) -> Bit:
        return self._value

    @value.setter
    def value(self, value: Bit):
        self._value = value
        for chip, pin_name in self.wired_pins:
            chip.set(pin_name, value)

    def __repr__(self):
        return f"Pin(name={self.name}, value={self.value})"


class Pins:

    def __init__(self, *args: Pin):
        self._data = {p.name: p for p in args}

    def get(self, pin: PinName) -> Optional[Pin]:
        return self._data.get(pin)

    def __getitem__(self, pin: PinName) -> Pin:
        result = self._data.get(pin)
        if not result:
            raise KeyError(f'{pin} not exit')
        else:
            return result

    def __iter__(self):
        for pin in self._data.values():
            yield pin

    def set(self, pin: PinName, value: Bit):
        self._data[pin].value = value

    def __repr__(self):
        return f'{[p for p in self]}'


class PinNames:
    in_pins = ('a', 'b')
    out_pins = ('out',)


class Chip(abc.ABC):

    in_pins: tuple[PinName]
    out_pins: tuple[PinName]
    pins: Pins

    def __init__(self) -> None:
        all_pins = (Pin(x) for x in self.in_pins+self.out_pins)
        self.pins = Pins(*all_pins)

    def set(self, pin_name: PinName, value: Bit):
        if pin := self.pins.get(pin_name):
            pin.value = value
        else:
            raise ValueError('pin not found')

    def wire(self, pin_name: PinName, chip: Any, to_pin: PinName):
        if pin := self.pins.get(pin_name):
            pin.wired_pins.append((chip, to_pin))
        else:
            raise ValueError('pin not found')

    def eval(self):
        raise NotImplementedError

    def output(self) -> dict[PinName, Bit]:
        return {p.name: p.value for p in self.pins}

    def __repr__(self):
        return f'{self.__class__.__name__}' \
               f'(in_pins={self.in_pins}, out_pins={self.out_pins})'


if __name__ == '__main__':
    test_bit_int()
