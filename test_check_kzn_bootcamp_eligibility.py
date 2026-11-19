import unittest
from check_kzn_bootcamp_eligibility import check_kzn_bootcamp_eligibility


class BootcampEligibilityTests(unittest.TestCase):
    def test_example_eligible_and_case_insensitive(self):
        expected = 'Eligible! Welcome to the Connie sons & GirlCode bootcamp.'
        self.assertEqual(check_kzn_bootcamp_eligibility('Female', 'kzn', 16), expected)
        self.assertEqual(check_kzn_bootcamp_eligibility('FEMALE', 'KwaZulu-Natal', 30), expected)

    def test_example_gender_rule_and_order(self):
        self.assertEqual(check_kzn_bootcamp_eligibility('male', 'other', 10),
                         'Ineligible: Workshop is dedicated to girls and women in tech.')

    def test_example_province_rule(self):
        self.assertEqual(check_kzn_bootcamp_eligibility('female', 'Gauteng', 18),
                         'Ineligible: Priority is for KwaZulu-Natal residents.')

    def test_example_age_boundary(self):
        self.assertEqual(check_kzn_bootcamp_eligibility('female', 'KZN', 15),
                         'Ineligible: Minimum age requirement is 16.')


if __name__ == '__main__':
    unittest.main()
