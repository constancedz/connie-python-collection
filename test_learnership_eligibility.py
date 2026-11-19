import unittest
from check_learnership_eligibility import check_learnership_eligibility


class LearnershipEligibilityTests(unittest.TestCase):
    def test_example_inclusive_age_boundaries_and_case(self):
        for age in (18, 35):
            self.assertEqual(check_learnership_eligibility('FEMALE', age, False),
                             'Eligible! Proceed to technical assessment.')

    def test_example_age_outside_boundaries(self):
        for age in (17, 36):
            self.assertEqual(check_learnership_eligibility('female', age, False),
                             'Ineligible: Age must be between 18 and 35.')

    def test_example_gender_and_employment(self):
        self.assertEqual(check_learnership_eligibility('male', 25, False),
                         'Ineligible: Program is exclusively for women.')
        self.assertEqual(check_learnership_eligibility('female', 25, True),
                         'Ineligible: Must be currently unemployed.')


if __name__ == '__main__':
    unittest.main()
