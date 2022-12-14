import sys
import unittest

from .symbolTable import SymbolTable
from n2t.hackAssembler.instruction import InstructionTypes
from .parser import Parser
from .code import Code


def compile_asm(file: str) -> list[str]:
    print(f"start compile {file=}")
    parser = Parser(file)
    # symbolTable = SymbolTable()
    # for ins in parser.instructions:
    #     if
    binaryCodes = list()
    while parser.hasMoreLines:
        if parser.instructionType == InstructionTypes.A_INSTRUCTION:

            binaryCodes.append(f"{int(parser.symbol):016b}")
        else:
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


if __name__ == "__main__":
    # compile_asm(sys.argv[1])
    unittest.main()
