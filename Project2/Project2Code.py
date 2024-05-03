# from datetime import datetime
import datetime

'''
You are tasked to build an employee management system for a small business.
The system allows the business to store and manage employee data and perform tasks related to employee management, 
such as adding and removing employees, updating employee information, 
searching for employees by name or department, and calculating total salary expenses. 
You will need to create one class for this project: Employee, which represents a single employee.

Attributes:
● name: string
● job_title: string
● department: string
● salary: float
● hire_year: int

Methods:
● __str__():  return a string representation.
● years_worked():  return the total years this employee has 
worked here, based on the hire year.
● total_expense():  calculate the total salary expense for this 
employee, which is the salary multiplied by the years worked.
● write_employees():  Write your employee information to a text 
file.
● Add accessor and mutator methods for each attribute so a user 
doesn't need to access them directly. 
● Be sure to use type hinting and a docstring in your class
'''
class Employee:
    # Initializer with Attributes
    def __init__(self, name: str, job_title: str, department: str, salary: float, hire_year: int) -> None:
        self.name = name
        self.job_title = job_title
        self.department = department
        self.salary = salary
        self.hire_year = hire_year

    # __str__():  return a string representation
    def __str__(self) -> str:
        return f'{self.name} is a {self.job_title} in the {self.department} Department. She makes {self.salary} and was hired in {self.hire_year}.'
    
    # years_worked():  return the total years this employee has worked here, based on the hire year.
    def years_worked(self) -> int:
        today = datetime.datetime.now()
        year = today.year
        return year - self.hire_year
    
    # total_expense():  calculate the total salary expense for this employee, which is the salary multiplied by the years worked.
    def total_expense(self) -> str:
        total_expense = self.salary * self.years_worked()
        return f'Total Expense for {self.name} is {total_expense}.'

employee1 = Employee('Xylia Pietas', 'Data Scientist', 'Data Analysis', 124360, 2011)  # Creates our first Object of the Employee Class

# String Representation
print(employee1)

# How many years worked at the Company
print(employee1.years_worked())

# Total Expense of the Employee
print(employee1.total_expense())