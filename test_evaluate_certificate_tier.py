import unittest
from evaluate_certificate_tier import evaluate_certificate_tier


class CertificateTierTests(unittest.TestCase):
    def test_excellence_boundaries(self):
        for score in (85, 100):
            self.assertEqual(evaluate_certificate_tier('Example', score),
                             'Example: Certificate of Excellence (Distinction)')

    def test_achievement_boundaries(self):
        for score in (60, 84):
            self.assertEqual(evaluate_certificate_tier('Example', score),
                             'Example: Certificate of Achievement (Pass)')

    def test_participation_boundaries(self):
        for score in (0, 59):
            self.assertEqual(evaluate_certificate_tier('Example', score),
                             'Example: Certificate of Participation (Retake Eligible)')

    def test_invalid_scores(self):
        for score in (-1, 101):
            self.assertEqual(evaluate_certificate_tier('Example', score),
                             'Invalid score: Must be between 0 and 100.')


if __name__ == '__main__':
    unittest.main()
