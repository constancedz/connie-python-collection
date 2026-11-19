import unittest
from buy_data_bundle import buy_data_bundle


class BuyDataBundleTests(unittest.TestCase):
    def test_sufficient_and_exact_balance(self):
        self.assertEqual(buy_data_bundle(100, 35), 'Purchase successful! Remaining balance: R65.00')
        self.assertEqual(buy_data_bundle(35, 35), 'Purchase successful! Remaining balance: R0.00')

    def test_insufficient_balance(self):
        self.assertEqual(buy_data_bundle(20, 35), 'Insufficient funds. You need R15.00 more.')

    def test_invalid_amounts(self):
        for balance, price in [(-1, 10), (10, 0), (10, -1)]:
            self.assertEqual(buy_data_bundle(balance, price), 'Invalid amount entered.')


if __name__ == '__main__':
    unittest.main()
