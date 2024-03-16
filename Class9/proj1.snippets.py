import re


'''What are some of the things we may come across while building this project'''

'''Initialization and prompt (and testing)'''
first_input, second_input = '', ''

# while True:
#     first_input = input(f'Please Enter Your Data: ')
#     second_input = input(f'Please Enter Your Data: ')
#     print(first_input, second_input)
#     break

'''Handling error messages with a list (and testing)'''
error_messages = ['Error Message 1', 'Error Message 2', 'Error Message 3']

# if 5 > 7:
#     print(error_messages[0])
# else:
#     print(error_messages[2])


'''Testing a string'''

# Example of string testing (testing for lowercase letter)
test_string = 'Popeye1989'

# Testing for uppercase as first letter
first_letter = test_string[0]
lowercase_test = first_letter.islower()

# if lowercase_test:
#     print('This string has failed Lowercase Test')
# else:
#     print('This string has passed Lowercase Test')


''' Taken usernames '''
sample_word = 'blue'
sample_list = ['green', 'blue', 'orange', 'yellow', 'purple']

# if sample_word in sample_list:
#     print('Word exists in the List')
# else:
#     print('Word does not exists in the List')


''' Using Break and Continue to control the flow of loop'''

# If input is a number we will go through this while loop and continue through, if not, we will send the user back to the beginning

# while True:
#     userinput = input('Enter your Test String: ')
#     if userinput.isnumeric():
#         print('This is a Number. We will stay in the Loop.')
#     else:
#         print('Not a Number. Try Again.')
#         continue
#     print('You will only see this line of code if you are still in the Loop.')
#     break


'''Password requirements'''

test_string = 'C1234567'

# At least 8 characters long

# # Contains at least one uppercase letter
one_uppercase = False

# for t in test_string:
#     if t.isupper():
#         one_uppercase = True
# print(f'Contains at least one uppercase?', one_uppercase)

# Even better, is the any function! Tests if any of items in iterable is true.
# The any() function returns True if any item in an iterable are true, otherwise it returns False.
# If the iterable object is empty, the any() function will return False.
any_uppercase = any(u.isupper() for u in test_string)
# print(f'Contains at least one Uppercase?', any_uppercase)

# Or Regular Expressions match method
uppercase_test_regex = bool(re.match(r'\w*[A-Z]\w', test_string))
# print(f'Contains at least one Uppercase?', uppercase_test_regex)


''' Logging in and handling the loop'''

# These can represent the user id and password the user created
sys_username = 'simonsays123'
sys_password = 'fido1950'

# These can represent the re-authentication
username = 'simonsays123'
password = 'fido1950'

# Lets check for a match

# while True:
#     if sys_username == username and sys_password == password:
#         print('Login Successful')
#         break
#     else:
#         print('Incorrect Username or Password')