import unittest


class SymbolTable:

    def __init__(self):
        self._symbol2Address = {"R"+str(i): i for i in range(16)} | {
            "SCREEN": 16384, "KBD": 24576,
            "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
        }
        self.nextVarAddress = 16

    def contains(self, symbol: str) -> bool:
        result = symbol in self._symbol2Address
        return result

    def addEntry(self, symbol: str, address: int):
        # assert symbol not in self._symbol2Address
        self._symbol2Address[symbol] = address
        if address == self.nextVarAddress:
            self.nextVarAddress += 1


    def getAddress(self, symbol: str) -> int:
        result = self._symbol2Address.get(symbol)
        return result


class TestSymbolTable(unittest.TestCase):

    def test_add_entry_and_contains(self):
        st = SymbolTable()
        self.assertEqual(False, st.contains('a'))
        st.addEntry('a', 16)
        self.assertEqual(True, st.contains('a'))

    def test_get_address(self):
        st = SymbolTable()
        for i in range(16):
            self.assertEqual(i, st.getAddress(symbol='R'+str(i)))



if __name__ == "__main__":
    unittest.main()
