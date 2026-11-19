import unittest
from valid_student_id import valid_student_id


class ValidStudentIdTests(unittest.TestCase):
    def test_valid_example(self):
        self.assertTrue(valid_student_id('CS-1234'))

    def test_invalid_formats_and_types(self):
        for student_id in ('CS-123', 'CS-12345', 'cs-1234', 'CS-12A4', 'AB-1234', '', 1234567, None):
            with self.subTest(student_id=student_id):
                self.assertFalse(valid_student_id(student_id))

    def test_isdigit_accepts_non_ascii_digits(self):
        self.assertTrue(valid_student_id('CS-١٢٣٤'))


if __name__ == '__main__':
    unittest.main()
