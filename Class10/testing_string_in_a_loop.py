import re

'''
You are testing a string through a while loop. 
The string must pass the following tests or the user must start over, be sure to tell the user the error.

1. String must be at least 10 characters
2. String must contain at least 1 number
3. String must contain at least 1 capital letter
4. String must contain '@' symbol
5. String must contain no spaces

Test data
jdefwkwf - not enough characters
sdnesleuex - at least 10 characters but no number
sdksdjsdf0 - at least 10 characters, contains number, no caps
Sdksdjsdf0 - at least 10 characters, contains number, has caps, no @ symbol
Sd@sdjs df0 - at least 10 characters, contains number, has caps, @ symbol, contains a space
Sd@sdjsdf0 - should pass all tests
'''

while True:
    user_input = input("Please enter your string ")
    # print(user_input)
    # break

    # Not enough characters
    if len(user_input) >= 10:
        print(f'Pass: {user_input} is greater than or equal to 10 characters.')
    else:
        print(f'Fail: {user_input} is under 10 characters.')
        continue
    
    # Contain at least 1 number
    contains_num = re.search(r'\d', user_input)
    if contains_num:
        print(f'Pass: {user_input} has a number.')
    else:
        print(f'Fail: {user_input} does not have a number.')
        continue
  
    # Contains at least 1 capital letter
    any_uppercase = any(u.isupper() for u in user_input)
    if any_uppercase:
        print(f'Pass: {user_input} has a Capital Letter.')
    else:
        print(f'Fail: {user_input} does not have any Capital Letters.')
        continue

    # Contains '@' symbol
    
    # Contains no spaces  