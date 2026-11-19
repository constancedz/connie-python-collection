import unittest
from load_shedding_status import load_shedding_status


class LoadSheddingStatusTests(unittest.TestCase):
    def test_stage_zero(self):
        self.assertEqual(load_shedding_status(0), 'No load shedding. Grid is stable.')

    def test_valid_stage_ranges(self):
        for stage in (1, 2):
            self.assertTrue(load_shedding_status(stage).startswith('Low impact:'))
        for stage in (3, 4):
            self.assertTrue(load_shedding_status(stage).startswith('Moderate impact:'))
        for stage in (5, 8):
            self.assertTrue(load_shedding_status(stage).startswith('High impact:'))

    def test_invalid_stages(self):
        for stage in (-1, 9, '2', 1.5):
            self.assertEqual(load_shedding_status(stage), 'Error: Stage must be between 0 and 8.')


if __name__ == '__main__':
    unittest.main()
