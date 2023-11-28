# test_processing_classes.py
import unittest
import os
from processing_classes import FileProcessor
from data_classes import Employee

class TestFileProcessor(unittest.TestCase):
    test_file = "test_EmployeeRatings.json"

    def setUp(self):
        # Set up a test file with some dummy data
        with open(self.test_file, "w") as file:
            file.write('[{"FirstName": "John", "LastName": "Doe", "ReviewDate": "2023-01-01", "ReviewRating": 4}]')

    def test_read_employee_data_from_file(self):
        employees = []
        employees = FileProcessor.read_employee_data_from_file(self.test_file, employees, Employee)
        self.assertEqual(len(employees), 1)
        self.assertIsInstance(employees[0], Employee)

    def test_write_employee_data_to_file(self):
        employees = [Employee("Jane", "Doe", "2023-02-01", 5)]
        FileProcessor.write_employee_data_to_file(self.test_file, employees)
        with open(self.test_file, "r") as file:
            content = file.read()
            self.assertIn("Jane", content)

    def tearDown(self):
        # Clean up by removing the test file
        os.remove(self.test_file)

if __name__ == '__main__':
    unittest.main()
