import unittest
from n2t.vm_translator.parser import Parser, CommandType


class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.vm_file = '/Users/wupeng/projects/nand2tetris/src/hdl/07/MemoryAccess/BasicTest/BasicTest.vm'
        self.parser = Parser(self.vm_file)

    def test_parser(self):
        self.assertEqual(self.parser.hasMoreLines, True)

        self.parser.advance()
        self.assertEqual(self.parser.hasMoreLines, True)
        self.assertEqual(self.parser.commandType, CommandType.C_PUSH)
        self.assertEqual(self.parser.arg1, 'constant')
        self.assertEqual(self.parser.arg2, 10)

        self.parser.advance()
        self.assertEqual(self.parser.hasMoreLines, True)
        self.assertEqual(self.parser.commandType, CommandType.C_POP)
        self.assertEqual(self.parser.arg1, 'local')
        self.assertEqual(self.parser.arg2, 0)

        self.parser.advance()
        self.parser.advance()
        self.parser.advance()
        self.assertEqual(self.parser.hasMoreLines, True)
        self.assertEqual(self.parser.commandType, CommandType.C_POP)
        self.assertEqual(self.parser.arg1, 'argument')
        self.assertEqual(self.parser.arg2, 2)
