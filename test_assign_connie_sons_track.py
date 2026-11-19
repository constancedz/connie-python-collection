import unittest
from assign_connie_sons_track import assign_connie_sons_track


class AssignTrackTests(unittest.TestCase):
    def test_junior_track_boundaries(self):
        for age in (5, 7):
            self.assertEqual(assign_connie_sons_track('Example', age),
                             'Example: Junior Scratch & Logic Track')

    def test_middle_track_boundaries(self):
        for age in (8, 13):
            self.assertEqual(assign_connie_sons_track('Example', age),
                             'Example: Scratch, Robotics & GirlCoder Club Track')

    def test_older_track(self):
        self.assertEqual(assign_connie_sons_track('Example', 14),
                         'Example: Python, Web Dev & Cisco Track')

    def test_invalid_ages(self):
        for age in (4, -1, '10', 10.5):
            self.assertEqual(assign_connie_sons_track('Example', age),
                             'Constraint Error: Example must be at least 5 years old.')


if __name__ == '__main__':
    unittest.main()
