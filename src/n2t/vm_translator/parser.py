from enum import Enum
import re


class CommandType(Enum):

    C_PUSH = 'push'
    C_POP = 'pop'
    C_ARITHMETIC = 'arithmetic'

    @classmethod
    def getByCmd(cls, cmd: str):
        match cmd:
            case 'push':
                return cls.C_PUSH
            case 'pop':
                return cls.C_POP
            case _:
                return cls.C_ARITHMETIC


class Parser:
    def __init__(self, vm_file: str):
        self.vm_file = vm_file
        self.vm_lines = []
        with open(vm_file, 'r') as f:
            for line in f:
                if re.match(r"(//.*)|^\n", line):
                    continue
                self.vm_lines.append(tuple(line.split()))
        self.current_line_index = -1

    @property
    def hasMoreLines(self):
        return (len(self.vm_lines)-1) > self.current_line_index

    def advance(self):
        self.current_line_index += 1

    @property
    def commandType(self):
        result = CommandType.getByCmd(self.vm_lines[self.current_line_index][0])
        return result

    @property
    def arg1(self) -> str:
        result = self.vm_lines[self.current_line_index][1]
        return result


    @property
    def arg2(self) -> int:
        result = int(self.vm_lines[self.current_line_index][2])
        return result
