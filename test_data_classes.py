# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# Chad Conklin, 11/29/2020, Added testing for Person and Employee classes
# ------------------------------------------------------------------------------------------------- #

import unittest
from datetime import date
from data_classes import Person, Employee

# Test data for the Person class
class TestPerson(unittest.TestCase):
    # tests the creation of a person
    def test_person_creation(self):
        person = Person("John", "Doe")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Doe")

    # tests the validation of the first name
    def test_person_name_validation(self):
        with self.assertRaises(ValueError):
            Person("John3", "Doe")

# Test data for the Employee class
class TestEmployee(unittest.TestCase):
    # tests the creation of an employee
    def test_employee_creation(self):
        employee = Employee("John", "Doe", "2023-01-01", 4)
        self.assertEqual(employee.first_name, "John")
        self.assertEqual(employee.last_name, "Doe")
        self.assertEqual(employee.review_date, "2023-01-01")
        self.assertEqual(employee.review_rating, 4)

    # tests the validation of the review date
    def test_review_date_validation(self):
        with self.assertRaises(ValueError):
            Employee("John", "Doe", "2023-02-30", 4)

    # tests the validation of the review rating
    def test_review_rating_validation(self):
        with self.assertRaises(ValueError):
            Employee("John", "Doe", "2023-01-01", 6)

if __name__ == '__main__':
    unittest.main()
