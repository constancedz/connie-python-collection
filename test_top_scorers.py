import unittest
from get_top_scorers import get_top_scorers


class TopScorersTests(unittest.TestCase):
    def test_threshold_and_order(self):
        self.assertEqual(get_top_scorers([69, 70, 100, 85, 70]), [70, 100, 85, 70])

    def test_out_of_range_and_empty(self):
        self.assertEqual(get_top_scorers([-1, 101]), [])
        self.assertEqual(get_top_scorers([]), [])


if __name__ == '__main__':
    unittest.main()
