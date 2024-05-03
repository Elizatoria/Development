'''You are tasked to build an employee management system for a small business.
The system allows the business to store and manage employee data and perform tasks related to employee management, 
such as adding and removing employees, updating employee information, 
searching for employees by name or department, and calculating total salary expenses. 
You will need to create one class for this project: Employee, which represents a single employee.
'''
class Employee:
    def __init__(self, name, job_title, department, salary, hire_year):
        self.name = name
        self.job_title = job_title
        self.department = department
        self.salary = salary
        self.hire_year = hire_year

    def __str__(self):
        return f'{self.name} is a {self.job_title} in the {self.department} Department. She makes {self.salary} and was hired in {self.hire_year}.'

employee1 = Employee('Xylia Pietas', 'Data Scientist', 'Data Analysis', 124360, 2024)

print(employee1)