# test_presentation_classes.py
import unittest
from unittest.mock import patch
from presentation_classes import IO
from data_classes import Employee

class TestIO(unittest.TestCase):
    # Example of testing an IO method that doesn't require user input
    def test_output_employee_data(self):
        employees = [Employee("John", "Doe", "2023-01-01", 4)]
        with patch('builtins.print') as mock_print:
            IO.output_employee_data(employees)
            mock_print.assert_called()

    # Example of testing an IO method that requires user input
    def test_input_employee_data(self):
        with patch('builtins.input', side_effect=["Jane", "Doe", "2023-02-01", "5"]):
            employees = []
            employees = IO.input_employee_data(employees, Employee)
            self.assertEqual(len(employees), 1)
            self.assertIsInstance(employees[0], Employee)

if __name__ == '__main__':
    unittest.main()
