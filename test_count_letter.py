import unittest
from count_letter import count_letter


class CountLetterTests(unittest.TestCase):
    def test_counts_case_insensitively(self):
        self.assertEqual(count_letter('Banana', 'A'), 3)

    def test_missing_and_empty_sentence(self):
        self.assertEqual(count_letter('hello', 'z'), 0)
        self.assertEqual(count_letter('', 'a'), 0)

    def test_target_length(self):
        message = 'Constraint Error: Target must be a single letter.'
        self.assertEqual(count_letter('hello', ''), message)
        self.assertEqual(count_letter('hello', 'he'), message)


if __name__ == '__main__':
    unittest.main()
