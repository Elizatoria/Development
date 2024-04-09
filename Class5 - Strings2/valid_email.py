# Get input
email = input("Hello, please enter your email address: ")
 
# Sanitize Data
email = email.strip()
 
# Test 1: It has a "." at the third-to-last index
test_1 = (email[-4] == '.')
print('Test 1: Does the email have a "." at the third-to-last index?',test_1)
 
# Test 2: It has exactly one "@" symbol, at the fifth-to-last index or earlier, email cannot be @.com
test_2 = ('@' in email[-6::-1])
print('Test 2: It has exactly one "@" symbol, at the fifth-to-last index or earlier?', test_2)
 
# Test 3: There is at least one character before the "@" symbol
test_3 = (email.index('@') > 0)
print('Test 3: There is at least one character before the "@" symbol?',test_3)
 
# Test 4: It doesn’t have any spaces (doesn’t contain " ")
test_4 = (' ' not in email)
print('Test 4: It doesn’t have any spaces (doesn’t contain " ")?', test_4)
 
# Final Test with and Keyword
final_result = (test_1 and test_2 and test_3 and test_4)
print('Is this email valid?', final_result)