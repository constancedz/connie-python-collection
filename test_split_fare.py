import unittest
from split_fare import split_fare


class SplitFareTests(unittest.TestCase):
    def test_without_tip(self):
        self.assertEqual(split_fare(100, 4), 'Each person pays: R25.00')
        self.assertEqual(split_fare(0, 2), 'Each person pays: R0.00')

    def test_with_tip(self):
        self.assertEqual(split_fare(100, 4, True), 'Each person pays: R27.50')

    def test_invalid_inputs(self):
        self.assertEqual(split_fare(100, 0), 'Error: At least 1 passenger is required.')
        self.assertEqual(split_fare(-1, 1), 'Error: Fare cannot be negative.')


if __name__ == '__main__':
    unittest.main()
