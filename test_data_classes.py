# test_data_classes.py
import unittest
from datetime import date
from data_classes import Person, Employee

class TestPerson(unittest.TestCase):
    def test_person_creation(self):
        person = Person("John", "Doe")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Doe")

    def test_person_name_validation(self):
        with self.assertRaises(ValueError):
            Person("John3", "Doe")

class TestEmployee(unittest.TestCase):
    def test_employee_creation(self):
        employee = Employee("John", "Doe", "2023-01-01", 4)
        self.assertEqual(employee.first_name, "John")
        self.assertEqual(employee.last_name, "Doe")
        self.assertEqual(employee.review_date, "2023-01-01")
        self.assertEqual(employee.review_rating, 4)

    def test_review_date_validation(self):
        with self.assertRaises(ValueError):
            Employee("John", "Doe", "2023-02-30", 4)

    def test_review_rating_validation(self):
        with self.assertRaises(ValueError):
            Employee("John", "Doe", "2023-01-01", 6)

if __name__ == '__main__':
    unittest.main()
