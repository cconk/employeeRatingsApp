# Employee Ratings Application
Employee ratings app for Intro to Python UW
# Introduction
The Employee Ratings App is an educational project developed as part of the Intro to Python course at the University of Washington. This application is designed to manage employee ratings effectively.

# Features
  * Employee Management: 
    * Add, 
    * update, 
    * and track employee information.
  
  * Ratings Review: 
    * Assign and update employee performance ratings.
  * Data Storage: 
    * Store and retrieve employee data from a JSON file.

# Installation
  To use the Employee Ratings App, clone the repository from GitHub:
  * git clone https://github.com/cconk/employeeRatingsApp.git
  * Navigate to the cloned directory and run the application using Python.

# Usage
  The application provides a user-friendly interface to input and manage employee data:
  * Add new employee information.
  * Update existing employee records.
  * Review and assign ratings to employees.

# Contributing
  Contributions to the Employee Ratings App are welcome. Please fork the repository and submit a pull request with your proposed changes.

# Description of Functionality from a user perspective
  The Employee Ratings App is a Python program designed for managing and reviewing employee performance. From a user's perspective, here's what the program does:
  * Manage Employee Data: Users can add and update employee information, including names, review dates, and ratings.
  * Menu-Driven Interface: The program offers a menu with options to display current data, enter new employee data, save data to a file, or exit the program.
  * Data Storage: Employee information is stored and managed in a JSON file (EmployeeRatings.json), allowing for persistence of data between sessions.
  * Employee Class: The Employee class inherits from the Person class and includes additional properties for the review date and review rating.
  * File Processing: The FileProcessor class handles reading from and writing to the JSON file, ensuring data is correctly saved and retrieved.
  * User Interaction: The IO class manages user input and output, displaying the menu, capturing user choices, and handling data entry.
  * Error Handling: The program includes error handling to manage incorrect data inputs and other exceptions.
  * Users interact with the program through a simple command-line interface, selecting options from the menu to manage and review employee data.

  # Employee Ratings Application Detailed Documentation

## Overview
This section of the documentation covers the source code for the Employee Ratings application, with descriptions for each function and class.

### data_classes.py
#### Person:
Description: Base object for application

Properties:
- first_name (str): The person's first name.
- last_name (str): The person's last name.
```python
class Person:
    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    @property
    def last_name(self):
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    def __str__(self):
        return f"{self.first_name},{self.last_name}"
```

#### Employee(Person):
Description: Expands person class and tailors for more specific use within the context of this application
 Properties:
- first_name (str): The employee's first name.
- last_name (str): The employee's last name.
- review_date (date): The data of the employee review.
- review_rating (int): The review rating of the employee's performance (1-5)
```python
class Employee(Person):
    def __init__(self, first_name: str = "", last_name: str = "", review_date: str = "1900-01-01", review_rating: int = 3):

        super().__init__(first_name=first_name,last_name=last_name)
        self.review_date = review_date
        self.review_rating = review_rating

    @property
    def review_date(self):
        return self.__review_date

    @review_date.setter
    def review_date(self, value: str):
        try:
            date.fromisoformat(value)
            self.__review_date = value
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    @property
    def review_rating(self):
        return self.__review_rating

    @review_rating.setter
    def review_rating(self, value: str):
        try:
            int(value)
            if int(value) in (1, 2, 3, 4, 5):
                self.__review_rating = value
            else:
                raise ValueError("Please choose only values 1 through 5")
        except ValueError as e:
            raise ValueError("Please choose only values 1 through 5")
    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.review_date},{self.__review_rating}"
```

### main.py

Description: This is the entry point for the application and running this file will start the application.
```python
from processing_classes import FileProcessor
from presentation_classes import IO
from data_classes import Employee


# Data -------------------------------------------- #
FILE_NAME: str = 'EmployeeRatings.json'

MENU: str = '''
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''

employees: list = []  # a table of employee data
menu_choice = ''

# Beginning of the main body of this script
employees = FileProcessor.read_employee_data_from_file(file_name=FILE_NAME, employee_data=employees, employee_type=Employee)  # Note this is the class name (ignore the warning)

# Repeat the follow tasks
while True:
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            IO.output_employee_data(employee_data=employees)
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        try:
            employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)  
            IO.output_employee_data(employee_data=employees)
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)
            print(f"Data was saved to the {FILE_NAME} file.")
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop
```

### presentation_classes.py
Description: Presentation classes are used to handle data input and output
```python
class IO:

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):

        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')


    @staticmethod
    def output_menu(menu: str):
        print()
        print(menu)
        print()


    @staticmethod
    def input_menu_choice():
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # passing the exception object to avoid the technical message

        return choice


    @staticmethod
    def output_employee_data(employee_data: list):
        message:str = ''
        print()
        print("-" * 50)
        for employee in employee_data:
            if int(employee.review_rating) == 5:
                message = " {} {} is rated as 5 (Leading)"
            elif int(employee.review_rating) == 4:
                message = " {} {} is rated as 4 (Strong)"
            elif int(employee.review_rating) == 3:
                message = " {} {} is rated as 3 (Solid)"
            elif int(employee.review_rating) == 2:
                message = " {} {} is rated as 2 (Building)"
            elif int(employee.review_rating) == 1:
                message = " {} {} is rated as 1 (Not Meeting Expectations)"

            print(message.format(employee.first_name, employee.last_name, employee.review_date, employee.review_rating))
        print("-" * 50)
        print()


    @staticmethod
    def input_employee_data(employee_data: list, employee_type: Employee):
        def check_quit(input_value: str):
            if input_value.lower() == "quit":
                # opttional messaging if the user wants to quit
                # print("You chose to quit the employee input process.")
                return True
            return False
        
        try:
            employee_object = employee_type()

            # Validate first name
            while True:
                first_name = input("What is the employee's first name? (or enter quit to return to the main menu) ")
                if check_quit(first_name):
                    return employee_data
                try:
                    employee_object.first_name = first_name
                    break
                except ValueError as e:
                    print(e)

            # Validate last name
            while True:
                last_name = input("What is the employee's last name? (or enter quit to return to the main menu) ")
                if check_quit(last_name):
                    return employee_data
                try:
                    employee_object.last_name = last_name
                    break
                except ValueError as e:
                    print(e)
           
            # Validate review date
            while True:
                review_date_str = input("What is their review date (YYYY-MM-DD)? (or enter quit to return to the main menu) ")
                if check_quit(review_date_str):
                    return employee_data
                try:
                    employee_object.review_date = review_date_str
                    break
                except ValueError as e:
                    print(e)

            # Validate review rating
            while True:
                review_rating_str = input("What is their review rating (1-5)? (or enter quit to return to the main menu) ")
                if check_quit(review_rating_str):
                    return employee_data
                try:
                    employee_object.review_rating = review_rating_str
                    break
                except ValueError as e:
                    print(e)

            # Assign validated values to the employee object
            employee_object.first_name = first_name
            employee_object.last_name = last_name
            employee_object.review_date = review_date_str
            employee_object.review_rating = review_rating_str

            employee_data.append(employee_object)

        except ValueError as e:
            IO.output_error_messages("Input error: " + str(e))
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)

        return employee_data
```

### processing_classes.py
Description: This class handles the processing of files where the data is saved.
```python
class FileProcessor:

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: Employee):
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(file)
                for employee in list_of_dictionary_data:
                    employee_object = employee_type()
                    employee_object.first_name = employee["FirstName"]
                    employee_object.last_name = employee["LastName"]
                    employee_object.review_date = employee["ReviewDate"]
                    employee_object.review_rating = employee["ReviewRating"]
                    employee_data.append(employee_object)
        except FileNotFoundError:
            print(f"File {file_name} not found. Starting with an empty employee list.")
            return employee_data  # Return the empty list if the file does not exist
        except Exception as e:
            raise Exception(f"There was an error reading the file: {e}")
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        try:
            list_of_dictionary_data: list = []
            for employee in employee_data:  # Convert List of employee objects to list of dictionary rows.
                employee_json: dict = {"FirstName": employee.first_name,
                                       "LastName": employee.last_name,
                                       "ReviewDate": employee.review_date,
                                       "ReviewRating": employee.review_rating
                                       }
                list_of_dictionary_data.append(employee_json)

            with open(file_name, "w") as file:
                json.dump(list_of_dictionary_data, file)
        except TypeError:
            raise TypeError("Please check that the data is a valid JSON format")
        except PermissionError:
            raise PermissionError("Please check the data file's read/write permission")
        except Exception as e:
            raise Exception("There was a non-specific error!")
```

### test_data_classes.py
Description: Unit tests for the data classes
```python
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
```

### test_presentation_classes.py
Description: Unit tests for presentation classes
```python
class TestIO(unittest.TestCase):
    #testing an IO method that doesn't require user input
    def test_output_employee_data(self):
        employees = [Employee("John", "Doe", "2023-01-01", "4")]
        with patch('builtins.print') as mock_print:
            IO.output_employee_data(employees)
            mock_print.assert_called()

    #testing an IO method that requires valid user input
    def test_input_employee_data(self):
        employee_data = []
        with patch('builtins.input', side_effect=("John", "Doe","2023-01-01", "4")):
            IO.input_employee_data(employee_data, Employee)
            self.assertEqual(employee_data[0].first_name, "John")
            self.assertEqual(employee_data[0].last_name, "Doe")
            self.assertEqual(employee_data[0].review_date, "2023-01-01")
            self.assertEqual(employee_data[0].review_rating, "4")
            self.assertEqual(len(employee_data), 1)

    def test_input_employee_data_quit(self):
        employee_data = []
        employee_type = Employee
        with patch('builtins.input', side_effect=("quit")), patch('builtins.print') as mock_print:
            result = IO.input_employee_data(employee_data, employee_type)
        self.assertEqual(result, [])
        mock_print.assert_called()

    def test_input_employee_data_invalid_firstName(self):
        employee_data = []
        employee_type = Employee
        with patch('builtins.input', side_effect=("John111","John", "Doe","2023-01-01", "4")), patch('builtins.print') as mock_print:
            result = IO.input_employee_data(employee_data, employee_type)
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0].first_name, "John")
            self.assertEqual(result[0].last_name, "Doe")
            self.assertEqual(result[0].review_date, "2023-01-01")
            self.assertEqual(result[0].review_rating, "4")
            mock_print.assert_called()
    
    def test_input_employee_data_invalid_lastName(self):
        employee_data = []
        employee_type = Employee
        with patch('builtins.input', side_effect=("John","Doe111", "Doe","2023-01-01", "4")), patch('builtins.print') as mock_print:
            result = IO.input_employee_data(employee_data, employee_type)
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0].first_name, "John")
            self.assertEqual(result[0].last_name, "Doe")
            self.assertEqual(result[0].review_date, "2023-01-01")
            self.assertEqual(result[0].review_rating, "4")
            mock_print.assert_called()
    
    def test_input_employee_data_invalid_reviewDate(self):
        employee_data = []
        employee_type = Employee
        with patch('builtins.input', side_effect=("John","Doe","2023-01-aa","2023-01-01", "4")), patch('builtins.print') as mock_print:
            result = IO.input_employee_data(employee_data, employee_type)
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0].first_name, "John")
            self.assertEqual(result[0].last_name, "Doe")
            self.assertEqual(result[0].review_date, "2023-01-01")
            self.assertEqual(result[0].review_rating, "4")
            mock_print.assert_called()

    def test_input_employee_data_invalid_reviewRating(self):
        employee_data = []
        employee_type = Employee
        with patch('builtins.input', side_effect=("John","Doe","2023-01-01","asdf", "4")), patch('builtins.print') as mock_print:
            result = IO.input_employee_data(employee_data, employee_type)
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0].first_name, "John")
            self.assertEqual(result[0].last_name, "Doe")
            self.assertEqual(result[0].review_date, "2023-01-01")
            self.assertEqual(result[0].review_rating, "4")
            mock_print.assert_called()
    
    #testing an IO method that user quits on first input
    def test_input_employee_data_quit_onFirstName(self):
        employee_data = []
        with patch('builtins.input', side_effect=("quit", "Doe","2023-01-01", "4")):
            IO.input_employee_data(employee_data, Employee)
            self.assertEqual(len(employee_data), 0)

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
```

