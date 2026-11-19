import unittest
from robotics_kit_ratio import robotics_kit_ratio


class RoboticsKitRatioTests(unittest.TestCase):
    def test_ideal_ratio(self):
        self.assertEqual(robotics_kit_ratio(20, 10), '2.0 learners per kit — Ideal (<= 2 per kit)')
        self.assertEqual(robotics_kit_ratio(5, 10), '0.5 learners per kit — Ideal (<= 2 per kit)')

    def test_high_sharing(self):
        self.assertEqual(robotics_kit_ratio(25, 10), '2.5 learners per kit — Rotate stations (high sharing)')

    def test_zero_learners(self):
        self.assertEqual(robotics_kit_ratio(0, 3), 'No learners checked in yet.')

    def test_invalid_counts(self):
        for learners, kits in ((1, 0), (1, -1), (-1, 2)):
            self.assertEqual(robotics_kit_ratio(learners, kits),
                             'Constraint Error: Kits must be >= 1 and learners >= 0.')


if __name__ == '__main__':
    unittest.main()
