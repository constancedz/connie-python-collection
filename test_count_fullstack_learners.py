import unittest
from count_fullstack_learners import count_fullstack_learners


class CountFullstackLearnersTests(unittest.TestCase):
    def test_case_insensitive_and_extra_skills(self):
        records = {
            'Learner A': ['HTML', 'css', 'Python'],
            'Learner B': ['html', 'CSS', 'PYTHON', 'javascript'],
            'Learner C': ['html', 'css'],
        }
        self.assertEqual(count_fullstack_learners(records), 2)

    def test_empty_and_incomplete_records(self):
        self.assertEqual(count_fullstack_learners({}), 0)
        self.assertEqual(count_fullstack_learners({'Learner A': []}), 0)
        self.assertEqual(count_fullstack_learners({'Learner A': ['html', 'python']}), 0)

    def test_duplicate_skill_does_not_replace_missing_skill(self):
        self.assertEqual(count_fullstack_learners({'Learner A': ['html', 'HTML', 'css']}), 0)


if __name__ == '__main__':
    unittest.main()
