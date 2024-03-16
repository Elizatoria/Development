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
email = input('Please enter your email: ')  #Getting User Email

# Clean data
clean_email = email.strip()  #removing whitespace from email

# Test 1: It has a "." at the third-to-last index
test_1 = (clean_email[-4] == '.')  #Looking for "." at -4
# print(f'Test 1: Does {clean_email} have a "." at the third-to-last index?', test_1)

# Test 2: It has exactly one "@" symbol, at the fifth-to-last index or earlier
# if test_2 := "@" in clean_email[0:-5]: 
#     test_2 == True
# else:
#     test_2 == False
# Realized that I could make Test 2 one line XD
test_2 = "@" in clean_email[0:-5]  #Looking for "@" at -5 or before
# print(f'Does it have exactly one "@" symbol, at the fifth-to-last index or earlier?', test_2)

# Test 3: There is at least one character before the "@" symbol
if test_3 := test_2 == True:  #If there is no "@" symbol, you can't look for its index.
    index = clean_email.find("@")  #Looking for the index for "@"
    test_3 = clean_email[index-1].isalnum()  #Looking for a Character before the "@" symbol
else:
    False
# print(f'Is there at least one character before the "@" symbol?', test_3)

# Test 4: It doesn’t have any spaces (doesn’t contain " ")
test_4 = " " not in clean_email  #Making sure there are no spaces within the email
# print(f'Does the email have no spaces?', test_4)

#Final Test with and Keyword
# if final_test := test_1 and test_2 and test_3 and test_4 == True:
#     final_test == True
# else:
#     final_test== False
# Realized that I could make Final Test one line XD
final_test = (test_1 and test_2 and test_3 and test_4)  #Testing for all Tests to be True
print(f'Is the email valid?', final_test)