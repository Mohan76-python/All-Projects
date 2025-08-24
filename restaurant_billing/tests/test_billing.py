# tests/test_billing.py

import unittest
from logic.billing import calculate_total

class TestBilling(unittest.TestCase):

    def setUp(self):
        self.menu = {
            "Idli": 30,
            "Dosa": 50,
            "Vada": 20
        }

    def test_valid_order(self):
        self.assertEqual(calculate_total(self.menu, "Idli", 2), 60)

    def test_zero_quantity(self):
        self.assertEqual(calculate_total(self.menu, "Dosa", 0), 0)

    def test_invalid_item(self):
        with self.assertRaises(ValueError):
            calculate_total(self.menu, "Pizza", 1)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            calculate_total(self.menu, "Vada", -3)

if __name__ == "__main__":
    unittest.main()
