import unittest
from estimate_uploads import estimate_uploads


class EstimateUploadsTests(unittest.TestCase):
    def test_exact_and_partial_fit(self):
        self.assertEqual(estimate_uploads(100, 10), 10)
        self.assertEqual(estimate_uploads(100, 30), 3)

    def test_file_larger_than_bundle(self):
        self.assertEqual(estimate_uploads(5, 10), 0)

    def test_invalid_values(self):
        for bundle, file_size in ((0, 10), (-1, 10), (10, 0), (10, -1)):
            self.assertEqual(estimate_uploads(bundle, file_size), 'Error: Values must be greater than 0.')


if __name__ == '__main__':
    unittest.main()
