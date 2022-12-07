import unittest

from n2t.hackAssembler.instruction import Instruction, InstructionTypes


class Parser:

    def __init__(self, path: str):
        self.instructions = []
        with open(path, 'r') as f:
            for line in f:
                if line.startswith('//'):
                    continue
                if line.startswith('\n'):
                    continue

                self.instructions.append(
                    Instruction.create(line.strip().removesuffix('\n'))
                )

        self.currentInstructionIndex = 0

    @property
    def hasMoreLines(self):
        return self.currentInstructionIndex < len(self.instructions) - 1

    def advance(self):
        self.currentInstructionIndex += 1

    @property
    def instructionType(self):
        result = self.instructions[self.currentInstructionIndex].type
        return result

    @property
    def comp(self):
        result = self.instructions[self.currentInstructionIndex].comp
        return result

    @property
    def dest(self):
        result = self.instructions[self.currentInstructionIndex].dest
        return result

    @property
    def symbol(self):
        result = self.instructions[self.currentInstructionIndex].symbol
        return result

    @property
    def jump(self):
        result = self.instructions[self.currentInstructionIndex].jump
        return result


class TestPaser(unittest.TestCase):

    def setUp(self) -> None:
        self.parserAdd = Parser(
            path='/Users/wupeng/projects/nand2tetris/src/hdl/06/add/Add.asm')
        self.parserMax = Parser(
            path='/Users/wupeng/projects/nand2tetris/src/hdl/06/max/max.asm')

    def test_should_be_able_to_check_has_more_lines(self):
        self.assertTrue(self.parserAdd.hasMoreLines)

    def test_should_be_able_to_parse_instruction_type(self):
        self.assertEqual(
            InstructionTypes.A_INSTRUCTION, self.parserAdd.instructionType)

    def test_should_be_able_to_advance(self):
        self.parserAdd.advance()
        self.assertEqual(
            InstructionTypes.C_INSTRUCTION, self.parserAdd.instructionType
        )

    def test_should_be_able_to_parse_symbol(self):
        self.parserMax.advance()
        self.parserMax.advance()
        self.parserMax.advance()
        self.parserMax.advance()
        self.assertEqual('OUTPUT_FIRST', self.parserMax.symbol)
        self.parserMax.advance()
        self.parserMax.advance()
        self.parserMax.advance()
        self.parserMax.advance()
        self.parserMax.advance()
        self.parserMax.advance()
        self.assertEqual('OUTPUT_FIRST', self.parserMax.symbol)

    def test_should_be_able_to_parse_destination(self):
        self.parserAdd.advance()
        self.assertEqual('D', self.parserAdd.dest)
        self.parserAdd.advance()
        self.parserAdd.advance()
        self.assertEqual('D', self.parserAdd.dest)
        self.parserAdd.advance()
        self.parserAdd.advance()
        self.assertEqual('M', self.parserAdd.dest)

    def test_should_be_able_to_parse_comp(self):
        self.parserAdd.advance()
        self.assertEqual('A', self.parserAdd.comp)
        self.parserAdd.advance()
        self.parserAdd.advance()
        self.assertEqual('D+A', self.parserAdd.comp)
        self.parserAdd.advance()
        self.parserAdd.advance()
        self.assertEqual('D', self.parserAdd.comp)

    def test_should_be_able_to_parse_jump(self):
        self.parserAdd.advance()
        self.assertEqual(None, self.parserAdd.jump)


if __name__ == "__main__":
    unittest.main()
