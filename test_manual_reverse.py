import unittest
from manual_reverse import manual_reverse


class ManualReverseTests(unittest.TestCase):
    def test_multiple_items(self):
        items = [1, 2, 3]
        self.assertEqual(manual_reverse(items), [3, 2, 1])
        self.assertEqual(items, [1, 2, 3])

    def test_empty_and_single(self):
        self.assertEqual(manual_reverse([]), [])
        self.assertEqual(manual_reverse(['one']), ['one'])

    def test_duplicate_items(self):
        self.assertEqual(manual_reverse(['a', 'b', 'a', 'c']), ['c', 'a', 'b', 'a'])


if __name__ == '__main__':
    unittest.main()
