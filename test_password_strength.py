import unittest
from check_password_strength import check_password_strength


class PasswordStrengthTests(unittest.TestCase):
    # These are invented test strings, not real passwords.
    def test_short_string(self):
        self.assertEqual(check_password_strength('abc1'), 'Weak: Password must be at least 8 characters long.')

    def test_missing_number(self):
        self.assertEqual(check_password_strength('abcdefgh'), 'Weak: Password must include at least one number.')

    def test_meets_example_rules(self):
        self.assertEqual(check_password_strength('abcdefg1'), 'Strong password!')


if __name__ == '__main__':
    unittest.main()
