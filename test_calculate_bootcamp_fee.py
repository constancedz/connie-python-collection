import unittest
from calculate_bootcamp_fee import calculate_bootcamp_fee


class BootcampFeeTests(unittest.TestCase):
    def test_full_fee_by_default(self):
        self.assertEqual(calculate_bootcamp_fee(200), 'Final Fee: R200.00')

    def test_example_scholarship_discount(self):
        self.assertEqual(calculate_bootcamp_fee(200, True), 'Final Fee: R150.00')
        self.assertEqual(calculate_bootcamp_fee(200, False), 'Final Fee: R200.00')

    def test_invalid_fee(self):
        for fee in (0, -1):
            self.assertEqual(calculate_bootcamp_fee(fee), 'Error: Fee must be positive.')


if __name__ == '__main__':
    unittest.main()
