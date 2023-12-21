import unittest

from n2t.vm_translator.codeWriter import CodeWriter
from n2t.vm_translator.parser import CommandType
from parameterized import parameterized


class TestCodeWriter(unittest.TestCase):
    def setUp(self):
        self.asm_file = '/Users/wupeng/projects/nand2tetris/src/hdl/07/MemoryAccess/BasicTest/BasicTest.asm'

    @parameterized.expand([
        (CommandType.C_PUSH, 'constant', 10, [
            '// push constant 10\n',
            '// D = i'
            '  @10\n',
            '  D=A\n',
            '// RAM[SP]=D\n',
            '  @SP\n',
            '  A=M\n',
            '  M=D\n',
            '// SP++\n',
            '  @SP\n',
            '  M=M+1\n',
        ]),
        (CommandType.C_PUSH, 'local', 0, [
            '// push local 0\n',
            '// addr = local + 0\n',
            '  @0\n',
            '  D=A\n',
            '  @local\n',
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
        ]),
        (CommandType.C_POP, 'local', 0, [
            '// pop local 0\n',
            '// addr = local + 0\n',
            '  @0\n',
            '  D=A\n',
            '  @local\n',
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
        ]),
        (CommandType.C_PUSH, 'argument', 0, [
            '// push argument 0\n',
            '// addr = argument + 0\n',
            '  @0\n',
            '  D=A\n',
            '  @argument\n',
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
        ]),
        (CommandType.C_POP, 'argument', 2, [
            '// pop argument 2\n',
            '// addr = argument + 2\n',
            '  @2\n',
            '  D=A\n',
            '  @argument\n',
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
        ]),
        (CommandType.C_PUSH, 'this', 0, [
            '// push this 0\n',
            '// addr = this + 0\n',
            '  @0\n',
            '  D=A\n',
            '  @this\n',
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
        ]),
        (CommandType.C_POP, 'this', 2, [
            '// pop this 2\n',
            '// addr = this + 2\n',
            '  @2\n',
            '  D=A\n',
            '  @this\n',
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
        ]),

    ])
    def test_something(self, cmd, segment, index, expected):

        codeWriter = CodeWriter(self.asm_file)
        codeWriter.writePushPop(cmd, segment, index)
        del codeWriter
        with open(self.asm_file, 'r') as f:
            lines = f.readlines()

        for i, expected_line in enumerate(expected):
            self.assertEqual(lines[i], expected_line, f"{cmd=} {segment=}")
