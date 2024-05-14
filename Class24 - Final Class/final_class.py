import pandas as pd

'''
Remove the duplicates from this list below. Can you do this in one line of code?

remove_dupes = [1, 2, 2, 3, 3, 3, 'new york', 'pennsylvania', 'new york', blue, blue, blue, green, 'hi', 'hello', 'hi']
'''
remove_dupes = [1, 2, 2, 3, 3, 3, 'new york', 'pennsylvania', 'new york', 'blue', 'blue', 'blue', 'green', 'hi', 'hello', 'hi']

# print(list(set(remove_dupes)))


''' 
Write a function that will take a single digit number written as a string and return the integer equivalent

for example
Input: 'five'
Output: 5

Hint: A dictionary can help you do this quickly
'''
def numbers(word):
    numbers = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
    }

    for k,v in numbers.items():
        if k == word:
            print(v)

# numbers('one')


'''
Recursion

Using recursion, 
write a recursive function which takes a positive number as an argument and prints the numbers from the specified argument down to zero

(Courtesy of Python Simplified and Realpython.com)
'''
def recursion(p):
    if p < 0:
        return
    else:
        print(p)
        recursion(p-1)

# recursion(7)


'''
You are given a dataset with the top 20 grossing movies of all time. 
Return a dataframe with just the movies in this list made in 2018 or after, 
put them in a new dataframe and create an excel file with the results.

Filename - top_twenty_movies.xlsx
'''
# df = pd.read_excel('Class24 - Final Class/top_twenty_movies.xlsx')
# data = df.loc[(df['Year']>=2018)]
# data.to_excel('top_for_2018.xlsx')


'''
Hide the credit card number
Write a function in Python that accepts a credit card number. 
It should return a string where all the characters are hidden with an asterisk except the last four. 
For example, if the function gets sent “4444444444444444”, then it should return “4444”.
Do not just cut out the first 12 characters and append the last for characters to a string.

ccnum = str(1234567890987654)
result = '************' + ccnum[12:16]
print(result)

 Loop through and solve with indexing
'''
# def cardNumberHider():
#     str = input("Enter the card number: ")
#     masked = len(str) - 4    
#     slimstr = str[masked:]
#     print("Your masked card number is: ", end="")
#     print("*" * masked + slimstr)
# cardNumberHider()


'''
Repeat the characters
Create a Python function that accepts a string. 
The function should return a string, with each character in the original string doubled. 
If you send the function “now” as a parameter, it should return “nnooww,” and if you send “123a!”, it should return “112233aa!!”.

Hint: Looks like a job for lambda functions and filters
'''
str_1 = 'now'
str_2 = '123a!'

# double_characters = lambda string: ''.join(char * 2 for char in string)
# doubled_string = double_characters(str_1)
# print(doubled_string)
# doubled_string = double_characters(str_2)
# print(doubled_string)


# double = map(lambda x:x+x, str_1)
# for d in double:
#     print(d, end='')

# double = map(lambda x:x+x, str_2)
# for d in double:
#     print(d, end='')


''' 
Create a function, use a for loop and conditionals (if statements) to solve the following:
Given a list of even numbers, odd numbers, and words, create a function that will create a list of even numbers, 
a list of odd numbers, and a list of words. (3 separate lists)

data = [1,2,3,4,5,6,7,8,9,10,11, 'horse', 'mule', 'ketchup', 'sunshine']
'''
data = [1,2,3,4,5,6,7,8,9,10,11, 'horse', 'mule', 'ketchup', 'sunshine']

string = []
even = []
odd = []

# def organize(my_list):
#     for d in data:
#         if isinstance(d, str):
#             string.append(d)
#         else:
#             if d % 2:
#                 even.append(d)
#             else:
#                 odd.append(d)
#     return string, even, odd

# print(organize(data))


'''Write function to count down how long an Employee has been at the company for Month Day Year'''
from dateutil.relativedelta import relativedelta
from datetime import date
 
hire_date = date(2000, 4, 20)
current_date = date.today()
 
years_of_service = relativedelta(hire_date, current_date)
print(f'Employee 1 has been working for {years_of_service.years} years, {years_of_service.months} months, {years_of_service.days} days ')