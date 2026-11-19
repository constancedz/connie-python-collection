import unittest
from count_multi_track_students import count_multi_track_students


class MultiTrackStudentsTests(unittest.TestCase):
    def test_multiple_and_single_courses(self):
        records = {'student_a': ['Python', 'Scratch'], 'student_b': ['Python'], 'student_c': []}
        self.assertEqual(count_multi_track_students(records), 1)

    def test_no_records(self):
        self.assertEqual(count_multi_track_students({}), 0)

    def test_multiple_students(self):
        records = {'student_a': ['A', 'B'], 'student_b': ['A', 'B', 'C']}
        self.assertEqual(count_multi_track_students(records), 2)


if __name__ == '__main__':
    unittest.main()
