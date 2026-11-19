import unittest
from calculate_kit_ratio import calculate_kit_ratio


class CalculateKitRatioTests(unittest.TestCase):
    def test_ratio_at_or_below_two(self):
        self.assertEqual(calculate_kit_ratio(20, 10), 'Optimal ratio: 2.0 students per kit.')
        self.assertEqual(calculate_kit_ratio(5, 10), 'Optimal ratio: 0.5 students per kit.')

    def test_high_sharing(self):
        self.assertEqual(calculate_kit_ratio(25, 10), 'High sharing ratio (2.5 per kit): Rotate groups.')

    def test_missing_kits_and_students(self):
        self.assertEqual(calculate_kit_ratio(10, 0), 'Constraint Error: At least 1 robotics kit is required.')
        self.assertEqual(calculate_kit_ratio(0, 3), 'No students registered for this session.')


if __name__ == '__main__':
    unittest.main()
