from n2t.vm_translator.parser import CommandType


class CodeWriter:

    def __init__(self, asm_file: str):
        self._f = open(asm_file, 'w')

    def __del__(self):
        print("closing file")
        self._f.close()

    def writeArithmetic(self, command):
        pass

    def writePushPop(self, command: CommandType, segment: str, index: int):
        if command not in [CommandType.C_PUSH, CommandType.C_POP]:
            raise ValueError('only push and pop command are allowed')
        match command, segment:
            case CommandType.C_PUSH, 'constant':
                instructions = self.instructinsForPushConstant(command, segment, index)

            case CommandType.C_PUSH, _:
                instructions = self.instructionsForPush(segment, index)

            case CommandType.C_POP, _:
                instructions = self.instructionsForPop(command, segment, index)

            case _:
                raise ValueError('invalid command')

        self._f.writelines(instructions)

    def instructionsForPop(self, command, segment, index):
        return [
                    f'// {command.value} {segment} {index}\n',
                    f'// addr = {segment} + {index}\n',
                    f'  @{index}\n',
                    '  D=A\n',
                    f'  @{segment}\n',
                    '  D=D+M\n',
                    '  @addr\n',
                    '  M=D\n',
                    '// SP--\n',
                    '  @SP\n',
                    '  M=M-1\n',
                    '// RAM[addr]=RAM[SP]\n',
                    '  A=M\n',
                    '  D=M\n',
                    '  @addr\n',
                    '  A=M\n',
                    '  M=D\n',
                ]

    def instructionsForPush(self, segment, index):
        return [
                    f'// push {segment} {index}\n',
                    f'// addr = {segment} + {index}\n',
                    f'  @{index}\n',
                    '  D=A\n',
                    f'  @{segment}\n',
                    '  D=D+M\n',
                    '  @addr\n',
                    '  M=D\n',
                    '// RAM[SP]=RAM[addr]\n',
                    '  A=M\n',
                    '  D=M\n',
                    '  @SP\n',
                    '  A=M\n',
                    '  M=D\n',
                    '// SP++\n',
                    '  @SP\n',
                    '  M=M+1\n',
                ]

    def instructinsForPushConstant(self, command, segment, index):
        return [
                    f'// {command.value} {segment} {index}\n',
                    '// D = i',
                    f'  @{index}\n',
                    '  D=A\n',
                    f'// RAM[SP]=D\n',
                    '  @SP\n',
                    '  A=M\n',
                    '  M=D\n',
                    '// SP++\n',
                    '  @SP\n',
                    '  M=M+1\n',
                ]
