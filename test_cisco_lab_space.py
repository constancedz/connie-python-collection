import unittest
from check_cisco_lab_space import check_cisco_lab_space


class CiscoLabSpaceTests(unittest.TestCase):
    def test_seats_available(self):
        self.assertEqual(check_cisco_lab_space(29), 'Seat available! 1 spots remaining.')
        self.assertEqual(check_cisco_lab_space(0, 20), 'Seat available! 20 spots remaining.')

    def test_cohort_full(self):
        self.assertEqual(check_cisco_lab_space(30), 'Cisco Cohort Full: Add student to the waiting list.')
        self.assertEqual(check_cisco_lab_space(20, 20), 'Cisco Cohort Full: Add student to the waiting list.')

    def test_invalid_enrollment(self):
        self.assertEqual(check_cisco_lab_space(-1), 'Error: Invalid enrollment count.')
        self.assertEqual(check_cisco_lab_space(31), 'Error: Invalid enrollment count.')


if __name__ == '__main__':
    unittest.main()
