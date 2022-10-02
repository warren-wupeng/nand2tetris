import abc

from collections import defaultdict


class Chip(abc.ABC):

    def __init__(self) -> None:
        self.wires: dict[str, list[tuple[object, str]]] = defaultdict(list)

    def set(self, pin: str, value: int):
        assert value in (0, 1)
        setattr(self, pin, value)
    
    def wire(self, pin: str, to: object, to_pin: str):
        self.wires[pin].append((to, to_pin))

    def eval(self):
        raise NotImplementedError

    def output(self):
        raise NotImplementedError
