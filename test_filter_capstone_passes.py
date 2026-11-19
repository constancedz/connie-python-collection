import unittest
from filter_capstone_passes import filter_capstone_passes


class FilterCapstonePassesTests(unittest.TestCase):
    def test_inclusive_boundaries_and_order(self):
        self.assertEqual(filter_capstone_passes([74, 75, 90.5, 100, 101, -1]), [75, 90.5, 100])

    def test_empty_and_no_passing_scores(self):
        self.assertEqual(filter_capstone_passes([]), [])
        self.assertEqual(filter_capstone_passes([0, 74.99, False, True]), [])

    def test_nonnumeric_and_nonfinite_values(self):
        self.assertEqual(filter_capstone_passes(['90', None, float('nan'), float('inf'), 80]), [80])


if __name__ == '__main__':
    unittest.main()
