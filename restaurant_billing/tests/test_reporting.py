import unittest
from reporting import generate_report  # Replace with your actual module and function

class TestReporting(unittest.TestCase):

    def test_generate_report_basic(self):
        sample_data = [
            {'item': 'Burger', 'quantity': 2, 'price': 100},
            {'item': 'Fries', 'quantity': 1, 'price': 50}
        ]
        expected_total = 250
        result = generate_report(sample_data)
        self.assertEqual(result['total'], expected_total)

    def test_generate_report_empty(self):
        sample_data = []
        expected_total = 0
        result = generate_report(sample_data)
        self.assertEqual(result['total'], expected_total)

    def test_generate_report_invalid_data(self):
        sample_data = [
            {'item': 'Burger', 'quantity': 'two', 'price': 100}
        ]
        with self.assertRaises(TypeError):
            generate_report(sample_data)

if __name__ == '__main__':
    unittest.main()
def test_generate_report_with_discount(self):
    sample_data = [
        {'item': 'Pizza', 'quantity': 3, 'price': 200},  # ₹600 total
    ]
    result = generate_report(sample_data)
    self.assertTrue('discount' in result)
    self.assertGreater(result['discount'], 0)
    self.assertLess(result['final_total'], result['total'])  # Final should be less than original
def test_generate_report_with_tax(self):
    sample_data = [
        {'item': 'Sandwich', 'quantity': 2, 'price': 150},  # ₹300
    ]
    result = generate_report(sample_data)
    expected_tax = 0.05 * result['total']
    self.assertAlmostEqual(result['tax'], expected_tax, places=2)
    self.assertEqual(result['final_total'], result['total'] + result['tax'])
