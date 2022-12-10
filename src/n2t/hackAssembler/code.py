import unittest
from typing import Union


class Code:

    _compTable = {
        "0": "0101010",
        "1": "0111111",
        "-1": "0111010",
        "D": "0001100",
        "A": "0110000",
        "M": "1110001",
        "!D": "0001101",
        "!A": "0110001",
        "!M": "1110001",
        "-D": "0001111",
        "-A": "0110011",
        "-M": "1110011",
        "D+1": "0011111",
        "A+1": "0110111",
        "M+1": "1110111",
        "D-1": "0001110",
        "A-1": "0110010",
        "M-1": "1110010",
        "D+A": "0000010",
        "D-A": "0010011",
        "D-M": "1010011",
        "A-D": "0000111",
        "D&A": "0000000",
        "D&M": "1000000",
        "D|A": "0010101",
        "D|M": "1010101",
    }

    @classmethod
    def dest(cls, word: Union[str, None]) -> str:
        if not word:
            return "000"
        bits = ["A" in word, "D" in word, "M" in word]
        return "".join([str(int(b)) for b in bits])

    @classmethod
    def comp(cls, word: Union[str, None]) -> str:
        if result := cls._compTable.get(word):
            return result
        else:
            raise cls.InvalidInstruction(word)

    class InvalidInstruction(Exception):
        pass


class TestCode(unittest.TestCase):

    def test_dest(self):
        self.assertEqual("000", Code.dest(None))
        self.assertEqual("001", Code.dest("M"))
        self.assertEqual("010", Code.dest("D"))
        self.assertEqual("011", Code.dest("DM"))
        self.assertEqual("100", Code.dest("A"))
        self.assertEqual("101", Code.dest("AM"))
        self.assertEqual("110", Code.dest("AD"))
        self.assertEqual("111", Code.dest("ADM"))

    def test_comp(self):
        self.assertEqual("0101010", Code.comp("0"))
        self.assertEqual("0111111", Code.comp("1"))
        self.assertEqual("0111010", Code.comp("-1"))
        self.assertEqual("0001100", Code.comp("D"))
        self.assertEqual("0110000", Code.comp("A"))
        self.assertEqual("1110001", Code.comp("M"))
        self.assertEqual("0001101", Code.comp("!D"))
        self.assertEqual("0110001", Code.comp("!A"))
        self.assertEqual("1110001", Code.comp("!M"))
        self.assertEqual("0001111", Code.comp("-D"))
        self.assertEqual("0110011", Code.comp("-A"))
        self.assertEqual("1110011", Code.comp("-M"))
        self.assertEqual("0011111", Code.comp("D+1"))
        self.assertEqual("0110111", Code.comp("A+1"))
        self.assertEqual("1110111", Code.comp("M+1"))
        self.assertEqual("0001110", Code.comp("D-1"))
        self.assertEqual("0110010", Code.comp("A-1"))
        self.assertEqual("1110010", Code.comp("M-1"))
        self.assertEqual("0000010", Code.comp("D+A"))
        self.assertEqual("0010011", Code.comp("D-A"))
        self.assertEqual("1010011", Code.comp("D-M"))
        self.assertEqual("0000111", Code.comp("A-D"))
        self.assertEqual("0000000", Code.comp("D&A"))
        self.assertEqual("1000000", Code.comp("D&M"))
        self.assertEqual("0010101", Code.comp("D|A"))
        self.assertEqual("1010101", Code.comp("D|M"))


if __name__ == "__main__":
    unittest.main()
