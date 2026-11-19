import unittest
from get_active_modules import get_active_modules


class GetActiveModulesTests(unittest.TestCase):
    def test_selects_active_titles_in_order(self):
        curriculum = [
            {'title': 'Scratch', 'active': True},
            {'title': 'Python', 'active': False},
            {'title': 'Robotics', 'active': True},
        ]
        self.assertEqual(get_active_modules(curriculum), ['Scratch', 'Robotics'])

    def test_only_true_is_active(self):
        curriculum = [
            {'title': 'One', 'active': 1},
            {'title': 'String', 'active': 'true'},
            {'title': 'Missing'},
            {'title': 'Active', 'active': True},
        ]
        self.assertEqual(get_active_modules(curriculum), ['Active'])

    def test_empty_curriculum(self):
        self.assertEqual(get_active_modules([]), [])


if __name__ == '__main__':
    unittest.main()
