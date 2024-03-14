import re


''' What are some of the things we may come across while building this project'''

'''Initialization and prompt (and testing)'''



'''Handling error messages with a list (and testing)'''



'''Testing a string'''

# Example of string testing (testing for lowercase letter)


# Testing for uppercase as first letter




''' Taken usernames '''



''' Using Break and Continue to control the follow of loop'''

# If input is a number we will go through this while loop and continue through, if not, we will send the user back to the beginning



''' Password requirements '''
test_string = 'C1234567'
# At least 8 characters long

# Contains at least one uppercase letter
one_uppercase = False
for t in test_string:
    if t.isupper():
        one_uppercase = True

print(f'Contains at least one uppercase?', one_uppercase)

# Even better, is the any function! Tests if any of items in iterable is true


# Or Regular Expressions match method


''' Logging in and handling the loop'''

# These can represent the user id and password the user created
# sys_username = 'simonsays123'
# sys_password = 'fido1950'


# These can represent the re-authentication
# username = 'simonsays123'
# password = 'fido1950'

# Lets check for a match
