import pandas as pd

'''
Suppose you have a list of employee records that contain the following information for each employee: name, job title, salary. 
The records are stored as a list of dictionaries.
Use this list to create a dictionary where the keys are the job titles and the values are the average salaries for each job title.
Example:
records = [{'name': 'Bob', 'title': 'manager', 'salary': 50000},\
           {'name': 'Alice', 'title': 'developer', 'salary': 60000},\
           {'name': 'David', 'title': 'developer', 'salary': 65000}]
Output: {'manager': 50000, 'developer': 62500}
'''

records = [{'name': 'Bob', 'title': 'manager', 'salary': 50000},\
           {'name': 'Alice', 'title': 'developer', 'salary': 60000},\
           {'name': 'David', 'title': 'developer', 'salary': 65000},
           {'name': 'Joe', 'title': 'consultant', 'salary': 25000},\
           {'name': 'Susan', 'title': 'consultant', 'salary': 40000},
            {'name': 'Isaiah', 'title': 'sales', 'salary': 120000}]

# Our Output Dictionaries
title_salary_dict = {}  # Capture Titles and Salary Totals
title_count_dict = {}  # Capture Title Count

# Loop Through List of Dictionaries
for r in records:
    # Define Key and Value Pair for Output
    title = r['title']
    salary = r['salary']
    # If Job Title does not Currently Exist, add the title and salary
    if title not in title_salary_dict:
        title_salary_dict[title] = salary
        title_count_dict[title] = 1
    else:
        # Otherwise, update Salary and update Count of Titles
        title_salary_dict[title] += salary
        title_count_dict[title] += 1

# Lets take a look at our Output
print(f'All Titles and sum of Salaries: ', title_salary_dict)
print(f'Titles ', title_count_dict)