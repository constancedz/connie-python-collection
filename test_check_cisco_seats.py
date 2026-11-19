import unittest
from check_cisco_seats import check_cisco_seats


class CheckCiscoSeatsTests(unittest.TestCase):
    def test_available_seats(self):
        self.assertEqual(check_cisco_seats(0), '30 seats remaining.')
        self.assertEqual(check_cisco_seats(29), '1 seats remaining.')
        self.assertEqual(check_cisco_seats(3, 10), '7 seats remaining.')

    def test_full(self):
        self.assertEqual(check_cisco_seats(30), 'Cohort full (waitlist active).')
        self.assertEqual(check_cisco_seats(10, 10), 'Cohort full (waitlist active).')

    def test_invalid_enrollment(self):
        for value in (-1, 31, '10', 1.5):
            self.assertEqual(check_cisco_seats(value), 'Invalid enrollment count.')


if __name__ == '__main__':
    unittest.main()
