# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# Chad Conklin, 11/29/2020, Added read_employee_data_from_file and write_employee_data_to_file
# ------------------------------------------------------------------------------------------------- #

from datetime import date

class Person:
    """
    A class representing person data.

    Properties:
    - first_name (str): The person's first name.
    - last_name (str): The person's last name.

    ChangeLog:
    - RRoot, 1.1.2030: Created the class.
    Chad Conklin, 11/29/2020, Added first_name and last_name properties
    """

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


class Employee(Person):
    """
    A class representing employee data.

    Properties:
    - first_name (str): The employee's first name.
    - last_name (str): The employee's last name.
    - review_date (date): The data of the employee review.
    - review_rating (int): The review rating of the employee's performance (1-5)

    ChangeLog:
    - RRoot, 1.1.2030: Created the class.
     Chad Conklin, 11/29/2020, Added read_employee_data_from_file and write_employee_data_to_file
    """

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