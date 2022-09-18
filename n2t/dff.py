from clock import Clock, Clocked



class Dff(Clocked):

    def __init__(self) -> None:
        self.i = False
        self.o = False
        

    def input(self, input: bool):
        self.i = input

    def output(self) -> bool:
        return self.o

    def ontick(self):
        pass

    def ontock(self):
        self.o = self.i


diff = Dff()
diff.input(True)
assert diff.output() is False
diff.ontick()
diff.ontock()
assert diff.output() is True
