import unittest
from attendance_percentage import attendance_percentage


class AttendancePercentageTests(unittest.TestCase):
    def test_at_threshold_and_above(self):
        self.assertEqual(attendance_percentage(4, 5), '80.0% (Certificate Eligible)')
        self.assertEqual(attendance_percentage(5, 5), '100.0% (Certificate Eligible)')

    def test_below_threshold(self):
        self.assertEqual(attendance_percentage(3, 5), '60.0% (Needs Make-up Sessions)')
        self.assertEqual(attendance_percentage(0, 5), '0.0% (Needs Make-up Sessions)')
        self.assertEqual(attendance_percentage(1, 3), '33.3% (Needs Make-up Sessions)')

    def test_invalid_counts(self):
        for attended, total in ((0, 0), (0, -1), (-1, 5), (6, 5)):
            self.assertEqual(attendance_percentage(attended, total), 'Invalid attendance numbers.')


if __name__ == '__main__':
    unittest.main()
