import unittest
from even_odd import check_even_odd
from reverse_string import reverse_string
from find_max import find_max
from count_vowels import count_vowels
from fizz_buzz import fizz_buzz
from is_palindrome import is_palindrome
from factorial import factorial
from remove_duplicates import remove_duplicates
from two_sum import two_sum
from calculate_average import calculate_average
from get_matric_pass import get_matric_pass

class CollectionTests(unittest.TestCase):
    def test_even_odd(self):
        self.assertEqual(check_even_odd(4), '4 is Even')
        self.assertEqual(check_even_odd(3), '3 is Odd')
        with self.assertRaises(TypeError): check_even_odd('4')
    def test_reverse(self):
        self.assertEqual(reverse_string('Python'), 'nohtyP')
        with self.assertRaises(TypeError): reverse_string(4)
    def test_max(self):
        self.assertEqual(find_max([-4, 2, 1]), 2)
        self.assertIsNone(find_max([]))
    def test_vowels(self):
        self.assertEqual(count_vowels('Hello AE'), 4)
        self.assertEqual(count_vowels(None), 0)
    def test_fizz_buzz(self):
        result = fizz_buzz(15)
        self.assertEqual((result[2], result[4], result[14]), ('Fizz', 'Buzz', 'FizzBuzz'))
    def test_palindrome(self):
        self.assertTrue(is_palindrome('A man, a plan, a canal: Panama'))
        self.assertFalse(is_palindrome('Python'))
        self.assertFalse(is_palindrome(None))
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError): factorial(-1)
    def test_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 1, 3]), [1, 2, 3])
    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum([1, 2], 10), [])
    def test_average(self):
        self.assertEqual(calculate_average([10, 20, 30]), 20)
        self.assertEqual(calculate_average([]), 0.0)
    def test_matric_exercise(self):
        self.assertEqual(get_matric_pass(80), "Distinction (Bachelor's Pass)")
        self.assertEqual(get_matric_pass(101), 'Invalid mark: Must be between 0 and 100.')

if __name__ == '__main__':
    unittest.main()
