import unittest
from is_valid_sa_id_format import is_valid_sa_id_format


class SAIDFormatTests(unittest.TestCase):
    def test_thirteen_digits(self):
        # An invented example, not a real person's ID.
        self.assertTrue(is_valid_sa_id_format('0' * 13))

    def test_wrong_length_and_non_digits(self):
        self.assertFalse(is_valid_sa_id_format('0' * 12))
        self.assertFalse(is_valid_sa_id_format('0' * 12 + 'a'))
        self.assertFalse(is_valid_sa_id_format(123))


if __name__ == '__main__':
    unittest.main()
