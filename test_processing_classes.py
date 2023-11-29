# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# Chad Conklin, 11/29/2020, Added testing for processing classes
# ------------------------------------------------------------------------------------------------- #

import unittest
import os
from processing_classes import FileProcessor
from data_classes import Employee

# Test data for the FileProcessor class
class TestFileProcessor(unittest.TestCase):
    test_file = "test_EmployeeRatings.json"

    # Set up a test file with some dummy data
    def setUp(self):
        # Set up a test file with some dummy data
        with open(self.test_file, "w") as file:
            file.write('[{"FirstName": "John", "LastName": "Doe", "ReviewDate": "2023-01-01", "ReviewRating": 4}]')

    # tests the reading of employee data from a file
    def test_read_employee_data_from_file(self):
        employees = []
        employees = FileProcessor.read_employee_data_from_file(self.test_file, employees, Employee)
        self.assertEqual(len(employees), 1)
        self.assertIsInstance(employees[0], Employee)

    # tests the writing of employee data to a file
    def test_write_employee_data_to_file(self):
        employees = [Employee("Jane", "Doe", "2023-02-01", 5)]
        FileProcessor.write_employee_data_to_file(self.test_file, employees)
        with open(self.test_file, "r") as file:
            content = file.read()
            self.assertIn("Jane", content)

    # Clean up by removing the test file
    def tearDown(self):
        # Clean up by removing the test file
        os.remove(self.test_file)

if __name__ == '__main__':
    unittest.main()
