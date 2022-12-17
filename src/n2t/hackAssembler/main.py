import sys
import unittest

from .symbolTable import SymbolTable
from n2t.hackAssembler.instruction import InstructionTypes
from .parser import Parser
from .code import Code


def compile_asm(file: str) -> list[str]:
    print(f"Assembling {file=}")
    parser = Parser(file)
    symbolTable = SymbolTable()
    n = 0
    for ins in parser.instructions:
        if ins.type == InstructionTypes.L_INSTRUCTION:
            if not symbolTable.contains(ins.symbol):
                symbolTable.addEntry(ins.symbol, n)
        else:
            n += 1
    #

    binaryCodes = list()
    while parser.hasMoreLines:
        if parser.instructionType == InstructionTypes.A_INSTRUCTION:
            if parser.symbol[0] in "1234567890":
                address = int(parser.symbol)
            else:
                address = symbolTable.getAddress(parser.symbol)

            binaryCodes.append(f"{address:016b}")
        elif parser.instructionType == InstructionTypes.C_INSTRUCTION:

            comp = Code.comp(parser.comp)
            dest = Code.dest(parser.dest)
            jump = Code.jump(parser.jump)
            binaryCodes.append(f"111{comp}{dest}{jump}")
        parser.advance()

    return binaryCodes


class TestCompileAsm(unittest.TestCase):

    def test_add(self):
        path = '/Users/wupeng/projects/nand2tetris/src/hdl/06/add/Add.asm'
        result = compile_asm(path)

        self.assertEqual(result, [
            "0000000000000010",
            "1110110000010000",
            "0000000000000011",
            "1110000010010000",
            "0000000000000000",
            "1110001100001000"
        ])

    def test_max(self):
        path = '/Users/wupeng/projects/nand2tetris/src/hdl/06/max/max.asm'
        result = compile_asm(path)

        self.assertEqual(result, [
            "0000000000000000",
            "1111110000010000",
            "0000000000000001",
            "1111010011010000",
            "0000000000001010",
            "1110001100000001",
            "0000000000000001",
            "1111110000010000",
            "0000000000001100",
            "1110101010000111",
            "0000000000000000",
            "1111110000010000",
            "0000000000000010",
            "1110001100001000",
            "0000000000001110",
            "1110101010000111",

        ])

    def test_max_l(self):
        path = '/Users/wupeng/projects/nand2tetris/src/hdl/06/max/maxL.asm'
        result = compile_asm(path)

        self.assertEqual(result, [
            "0000000000000000",
            "1111110000010000",
            "0000000000000001",
            "1111010011010000",
            "0000000000001010",
            "1110001100000001",
            "0000000000000001",
            "1111110000010000",
            "0000000000001100",
            "1110101010000111",
            "0000000000000000",
            "1111110000010000",
            "0000000000000010",
            "1110001100001000",
            "0000000000001110",
            "1110101010000111",

        ])


if __name__ == "__main__":
    # compile_asm(sys.argv[1])
    unittest.main()
