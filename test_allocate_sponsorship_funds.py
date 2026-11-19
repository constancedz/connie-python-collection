import unittest
from allocate_sponsorship_funds import allocate_sponsorship_funds


class AllocateSponsorshipFundsTests(unittest.TestCase):
    def test_example_allocation(self):
        self.assertEqual(allocate_sponsorship_funds(1000), {
            'Robotics & Hardware (50%)': 'R500.00',
            'Student Data & Resources (30%)': 'R300.00',
            'Facilitator & Operations (20%)': 'R200.00',
        })

    def test_invalid_amounts(self):
        for amount in (0, -100):
            self.assertEqual(allocate_sponsorship_funds(amount), 'Invalid sponsorship amount.')

    def test_decimal_amount(self):
        self.assertEqual(allocate_sponsorship_funds(10.50), {
            'Robotics & Hardware (50%)': 'R5.25',
            'Student Data & Resources (30%)': 'R3.15',
            'Facilitator & Operations (20%)': 'R2.10',
        })


if __name__ == '__main__':
    unittest.main()
