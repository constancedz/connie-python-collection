import unittest
from split_workshop_budget import split_workshop_budget


class SplitWorkshopBudgetTests(unittest.TestCase):
    def test_allocation(self):
        self.assertEqual(split_workshop_budget(1000), {
            'hardware_zar': 500.0,
            'data_and_materials_zar': 300.0,
            'facilitation_zar': 200.0,
        })

    def test_rounding(self):
        self.assertEqual(split_workshop_budget(10.01), {
            'hardware_zar': 5.0,
            'data_and_materials_zar': 3.0,
            'facilitation_zar': 2.0,
        })

    def test_nonpositive_amount(self):
        self.assertEqual(split_workshop_budget(0), {})
        self.assertEqual(split_workshop_budget(-10), {})


if __name__ == '__main__':
    unittest.main()
