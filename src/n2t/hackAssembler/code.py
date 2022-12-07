import unittest
from typing import Union


class Code:

    _destTable = {
        None: "000",
        "M": "001",
        "D": "010",
        "DM": "011",
        "A": "100",
        "AM": "101",
        "AD": "110",
        "ADM": "111"
    }

    @classmethod
    def dest(cls, word: Union[str, None]) -> str:
        if result := cls._destTable.get(word):
            return result
        else:
            raise cls.InvalidDest(word)

    class InvalidDest(Exception):
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


if __name__ == "__main__":
    unittest.main()
