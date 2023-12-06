# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# Chad Conklin, 11/29/2020, Added read_employee_data_from_file and write_employee_data_to_file
# ------------------------------------------------------------------------------------------------- #

from data_classes import Employee 
import datetime

class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    Chad Conklin, 11/29/2020, Added read_employee_data_from_file and write_employee_data_to_file
    """
    pass

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function
        Chad Conklin, 11/29/2020, Copied from module 8 assignment starter code

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """

        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')


    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        Chad Conklin, 11/29/2020, Copied from module 8 assignment starter code

        :return: None
        """
        print()
        print(menu)
        print()


    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        Chad Conklin, 11/29/2020, Copied from module 8 assignment starter code

        :return: string with the users choice
        """
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
        """ This function displays employee data to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        Chad Conklin, 11/29/2020, Copied from module 8 assignment starter code

        :param employee_data: list of employee object data to be displayed

        :return: None
        """
        message:str = ''
        print()
        print("-" * 50)
        for employee in employee_data:
            if employee.review_rating == 5:
                message = " {} {} is rated as 5 (Leading)"
            elif employee.review_rating == 4:
                message = " {} {} is rated as 4 (Strong)"
            elif employee.review_rating == 3:
                message = " {} {} is rated as 3 (Solid)"
            elif employee.review_rating == 2:
                message = " {} {} is rated as 2 (Building)"
            elif employee.review_rating == 1:
                message = " {} {} is rated as 1 (Not Meeting Expectations)"

            print(message.format(employee.first_name, employee.last_name, employee.review_date, employee.review_rating))
        print("-" * 50)
        print()


    @staticmethod
    def input_employee_data(employee_data: list, employee_type: Employee):
        """ This function gets the first name, last name, and rating from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        Chad Conklin, 11/29/2020, Copied from module 8 assignment starter code

        :param employee_data: list of dictionary rows to be filled with input data

        :return: list
        """
        def check_quit(input_value: str):
            """ This function checks if the user wants to quit

            ChangeLog: (Who, When, What)
            Chad Conklin, 11/29/2020, Created function

            :param input_value: string to check if the user wants to quit

            :return: boolean
            """
            if input_value.lower() == "quit":
                print("You chose to quit the employee input process.")
                return True
            return False
        
        try:
            employee_object = employee_type()

            # Validate first name
            while True:
                first_name = input("What is the employee's first name? ")
                if check_quit(first_name):
                    return employee_data
                try:
                    employee_object.first_name = first_name
                    break
                except ValueError as e:
                    print(e)

            # Validate last name
            while True:
                last_name = input("What is the employee's last name? ")
                if check_quit(last_name):
                    return employee_data
                try:
                    employee_object.last_name = last_name
                    break
                except ValueError as e:
                    print(e)
           
            # Validate review date
            while True:
                review_date_str = input("What is their review date (YYYY-MM-DD)? ")
                if check_quit(review_date_str):
                    return employee_data
                try:
                    employee_object.review_date = review_date_str
                    break
                except ValueError as e:
                    print(e)

            # Validate review rating
            while True:
                review_rating_str = input("What is their review rating (1-5)? ")
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
            employee_object.review_rating = int(review_rating_str)

            employee_data.append(employee_object)

        except ValueError as e:
            IO.output_error_messages("Input error: " + str(e))
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)

        return employee_data