'''
Exercise - Valid email
Write some code that takes input from the user and prints whether it's a valid email address. 
Make sure to sanitize the user input with .strip()
An email address is valid if:
It has a "." at the third-to-last index
It has exactly one "@" symbol, at the fifth-to-last index or earlier
There is at least one character before the "@" symbol
It doesn't have any spaces (doesn't contain " ")
If all these conditions are met, print True. Otherwise, print False.
To do this, use boolean statements on your string.
Test your code on a few inputs to make sure it works!

'''
# Get input 
email = input('Please enter your email: ')

# Clean data
clean_email = email.strip()

# Test 1: It has a "." at the third-to-last index
test_1 = (clean_email[-4] == '.')
# print(f'Test 1: Does {clean_email} have a "." at the third-to-last index?', test_1)

# Test 2: It has exactly one "@" symbol, at the fifth-to-last index or earlier
if test_2 := "@" in clean_email[0:-5]: 
    test_2 == True
else:
    test_2 == False
# print(f'Does it have exactly one "@" symbol, at the fifth-to-last index or earlier?', test_2)

# Test 3: There is at least one character before the "@" symbol
test_3 = clean_email

# Test 4: It doesn’t have any spaces (doesn’t contain " ")

#Final Test with and Keyword