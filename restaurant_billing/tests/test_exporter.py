# tests/test_exporter.py

import unittest
import os
from logic.exporter import export_bill_to_csv, export_bill_to_json

class TestExporter(unittest.TestCase):

    def setUp(self):
        self.order_id = "TEST123"
        self.item = "Idli"
        self.quantity = 2
        self.price = 30
        self.total = 60
        self.folder = "test_bills"

    def test_csv_export(self):
        filename = export_bill_to_csv(
            self.order_id, self.item, self.quantity, self.price, self.total, folder=self.folder
        )
        self.assertTrue(os.path.exists(filename))
        self.assertTrue(filename.endswith(".csv"))

    def test_json_export(self):
        filename = export_bill_to_json(
            self.order_id, self.item, self.quantity, self.price, self.total, folder=self.folder
        )
        self.assertTrue(os.path.exists(filename))
        self.assertTrue(filename.endswith(".json"))

    def tearDown(self):
        # Clean up test files
        for file in os.listdir(self.folder):
            os.remove(os.path.join(self.folder, file))
        os.rmdir(self.folder)

if __name__ == "__main__":
    unittest.main()
