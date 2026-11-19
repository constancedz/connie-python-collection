import unittest
from assign_coding_track import assign_coding_track


class AssignCodingTrackTests(unittest.TestCase):
    def test_under_five(self):
        self.assertEqual(assign_coding_track('Learner A', 4), 'Learner A is too young for current Connie sons tracks.')

    def test_junior_scratch_boundaries(self):
        for age in (5, 7):
            self.assertEqual(assign_coding_track('Learner A', age), 'Learner A -> Junior Scratch Track')

    def test_scratch_robotics_boundaries(self):
        for age in (8, 13):
            self.assertEqual(assign_coding_track('Learner A', age), 'Learner A -> Scratch & Robotics Track')

    def test_older_track(self):
        self.assertEqual(assign_coding_track('Learner A', 14), 'Learner A -> Python, Web Dev & IoT Track')


if __name__ == '__main__':
    unittest.main()
