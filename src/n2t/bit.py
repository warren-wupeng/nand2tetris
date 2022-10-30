import unittest


class Bit:
    def __init__(self, value: int = 0):
        if value not in (0, 1):
            raise ValueError(f"{value}")
        self.value = value

    def __and__(self, other):
        result = Bit(self.value & other.value)
        return result

    def __eq__(self, other):
        return self.value == other.value

    def __invert__(self):
        return Bit(0 if self.value else 1)

    def __bool__(self):
        return bool(self.value)

    def __repr__(self):
        return f'Bit({self.value})'


class TestBit(unittest.TestCase):

    def test_should_not_accept_value_other_than_0_and_1(self):
        with self.assertRaises(ValueError):
            Bit(2)

        with self.assertRaises(ValueError):
            Bit(-1)

    def test_should_be_comparable(self):
        self.assertEqual(Bit(0), Bit(0))
        self.assertEqual(Bit(1), Bit(1))

    def test_should_support_and_operation(self):
        self.assertEqual(Bit(0) & Bit(0), Bit(0))
        self.assertEqual(Bit(0) & Bit(1), Bit(0))
        self.assertEqual(Bit(1) & Bit(0), Bit(0))
        self.assertEqual(Bit(1) & Bit(1), Bit(1))

    def test_should_support_invert(self):
        self.assertEqual(~ Bit(0), Bit(1))
        self.assertEqual(~ Bit(1), Bit(0))

    def test_should_to_str_friendly(self):
        self.assertEqual(str(Bit(0)), 'Bit(0)')
        self.assertEqual(str(Bit(1)), 'Bit(1)')


if __name__ == '__main__':
    unittest.main()
