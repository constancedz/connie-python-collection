import unittest
from calculate_sync_capacity import calculate_sync_capacity


class SyncCapacityTests(unittest.TestCase):
    def test_exact_and_partial_capacity(self):
        self.assertEqual(calculate_sync_capacity(300, 100), 'You can upload 3 student projects on this bundle.')
        self.assertEqual(calculate_sync_capacity(320, 100), 'You can upload 3 student projects on this bundle.')

    def test_project_larger_than_bundle(self):
        self.assertEqual(calculate_sync_capacity(50, 100), 'You can upload 0 student projects on this bundle.')

    def test_nonpositive_inputs(self):
        for data, project in ((0, 1), (-1, 1), (1, 0), (1, -1)):
            self.assertEqual(calculate_sync_capacity(data, project),
                             'Constraint Error: Data and project size must be positive.')


if __name__ == '__main__':
    unittest.main()
