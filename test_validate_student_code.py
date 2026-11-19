import unittest
from validate_student_code import validate_student_code


class ValidateStudentCodeTests(unittest.TestCase):
    def test_valid_example(self):
        self.assertTrue(validate_student_code('CS-1234'))

    def test_invalid_formats(self):
        for code in ('CS-123', 'CS-12345', 'cs-1234', 'CS-12A4', 'AB-1234', '', 1234567, None):
            with self.subTest(code=code):
                self.assertFalse(validate_student_code(code))

    def test_isdigit_accepts_non_ascii_digits(self):
        self.assertTrue(validate_student_code('CS-١٢٣٤'))


if __name__ == '__main__':
    unittest.main()
