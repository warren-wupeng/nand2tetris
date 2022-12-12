import unittest


class SymbolTable:

    def __init__(self):
        self._symbol2Address = dict()
        self._address2symbol = dict()
        for i in range(16):
            self.addEntry("R"+str(i), i)

    def contains(self, symbol: str) -> bool:
        result = symbol in self._symbol2Address
        return result

    def addEntry(self, symbol: str, address: int):
        # assert symbol not in self._symbol2Address
        self._symbol2Address[symbol] = address
        self._address2symbol[address] = symbol

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
