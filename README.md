# Employee Ratings Application
Employee ratings app for Intro to Python UW
# Introduction
The Employee Ratings App is an educational project developed as part of the Intro to Python course at the University of Washington. This application is designed to manage employee ratings effectively.

# Features
  Employee Management: Add, update, and track employee information.
  Ratings Review: Assign and update employee performance ratings.
  Data Storage: Store and retrieve employee data from a JSON file.

# Installation
  To use the Employee Ratings App, clone the repository from GitHub:
    git clone https://github.com/cconk/employeeRatingsApp.git
  Navigate to the cloned directory and run the application using Python.

# Usage
  The application provides a user-friendly interface to input and manage employee data:
    Add new employee information.
    Update existing employee records.
    Review and assign ratings to employees.

# Contributing
  Contributions to the Employee Ratings App are welcome. Please fork the repository and submit a pull request with your proposed changes.

# Description of Functionality from a user perspective
  The Employee Ratings App is a Python program designed for managing and reviewing employee performance. From a user's perspective, here's what the program does:
    Manage Employee Data: Users can add and update employee information, including names, review dates, and ratings.
    Menu-Driven Interface: The program offers a menu with options to display current data, enter new employee data, save data to a file, or exit the program.
    Data Storage: Employee information is stored and managed in a JSON file (EmployeeRatings.json), allowing for persistence of data between sessions.
    Employee Class: The Employee class inherits from the Person class and includes additional properties for the review date and review rating.
    File Processing: The FileProcessor class handles reading from and writing to the JSON file, ensuring data is correctly saved and retrieved.
    User Interaction: The IO class manages user input and output, displaying the menu, capturing user choices, and handling data entry.
    Error Handling: The program includes error handling to manage incorrect data inputs and other exceptions.
  Users interact with the program through a simple command-line interface, selecting options from the menu to manage and review employee data.