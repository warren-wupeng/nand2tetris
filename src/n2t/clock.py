from abc import ABC

# class Clock:

#     def __init__(self) -> None:
#         self.time = 0
#         self._tick = False

#     def tick(self):
#         if not self._tick:
#             self._tick = True
    
#     def tock(self):
#         if self._tick:
#             self.time += 1

class Clocked(ABC):

    def tick(self):
        raise NotImplementedError

    def tock(self):
        raise NotImplementedError