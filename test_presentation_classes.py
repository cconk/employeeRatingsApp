# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# Chad Conklin, 11/29/2020, Added unit tests for IO class
# ------------------------------------------------------------------------------------------------- #

import unittest
from unittest.mock import patch
from presentation_classes import IO
from data_classes import Employee
from datetime import datetime

# Test data for the IO class
class TestIO(unittest.TestCase):
    #testing an IO method that doesn't require user input
    def test_output_employee_data(self):
        employees = [Employee("John", "Doe", "2023-01-01", 4)]
        with patch('builtins.print') as mock_print:
            IO.output_employee_data(employees)
            mock_print.assert_called()

    #testing an IO method that requires user input
    def test_input_employee_data(self):
        employee_data = []
        with patch('builtins.input', side_effect=("John", "Doe","2023-01-01", "4")):
            IO.input_employee_data(employee_data, Employee)
            self.assertEqual(employee_data[0].first_name, "John")
            self.assertEqual(employee_data[0].last_name, "Doe")
            self.assertEqual(employee_data[0].review_date, "2023-01-01")
            self.assertEqual(employee_data[0].review_rating, 4)
            self.assertEqual(len(employee_data), 1)

    # testing an IO method that requires user input
    def test_input_menu_choice(self):
        with patch('builtins.input', side_effect=["1"]):
            choice = IO.input_menu_choice()
            self.assertEqual(choice, "1")

    # testing an IO method that doesn't require user input
    def test_output_error_messages(self):
        with patch('builtins.print') as mock_print:
            IO.output_error_messages("Test Error Message")
            mock_print.assert_called()
    
    # testing an IO method that doesn't require user input
    def test_output_menu(self):
        with patch('builtins.print') as mock_print:
            IO.output_menu("Test Menu")
            mock_print.assert_called()

if __name__ == '__main__':
    unittest.main()
