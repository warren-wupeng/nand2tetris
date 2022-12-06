from enum import Enum


class InstructionTypes(Enum):
    A_INSTRUCTION = 0
    C_INSTRUCTION = 1
    L_INSTRUCTION = 2


class Instruction:

    @classmethod
    def create(cls, ins: str):
        if ins.startswith('@'):
            return AInstruction(ins)
        elif ins.startswith('('):
            return LInstruction(ins)
        return CInstruction(ins)

    def __init__(self, ins: str):
        self.ins = ins

    @property
    def type(self):
        raise NotImplementedError

    @property
    def symbol(self):
        raise NotImplementedError

    @property
    def dest(self):
        raise NotImplementedError

    @property
    def comp(self):
        raise NotImplementedError

    @property
    def jump(self):
        raise NotImplementedError


class AInstruction(Instruction):

    @property
    def type(self):
        return InstructionTypes.A_INSTRUCTION

    @property
    def symbol(self):
        return self.ins[1:]

    @property
    def dest(self):
        return super().dest

    @property
    def comp(self):
        return super().comp


class LInstruction(Instruction):
    @property
    def type(self):
        return InstructionTypes.L_INSTRUCTION

    @property
    def symbol(self):
        return self.ins[1:-1]

    @property
    def dest(self):
        return super().dest

    @property
    def comp(self):
        return super().comp


class CInstruction(Instruction):

    @property
    def type(self):
        return InstructionTypes.C_INSTRUCTION

    @property
    def symbol(self):
        return super().symbol

    @property
    def dest(self):
        return self.ins[0]

    @property
    def comp(self):
        result = self.ins.split(';')[0][2:]
        return result

    @property
    def jump(self):
        s = self.ins.split(';')
        if len(s) == 2:
            return s[1]
        else:
            return None
