taken_usernames = ['admin', 'admin123', 'superuser', 'superuser123']
username, password = '', ''
username_input, password_input = '', ''
uppercase_test, lowercae_test, digit_test = False, False, False

print('''To sign up, create a Username and Password.
The Username must start with a lowercase letter and only contain letters, numbers, and underscores.
The Password must contain, at least, each of the following.
    ● 8 characters long
    ● One uppercase letter
    ● One lowercase letter
    ● One digit
    ● One of these characters:  !, ?, @, #, $, ^, &, *, _,  -
    ● No spaces''')

# # Username Creation
# while True:
#     username_input = input('Create Username: ')  # Input for creating a new Username
    
# # Tests for Username
#     taken_test = username_input not in taken_usernames  # Test to check if Username is Taken
#     lower_test = username_input[0].islower()  # Test to check if first letter is Lowercase Letter
#     underscore_test = ('_' in username_input)  # Test to check if there are any Underscores
#     for u in username_input:
#         alpha_num_test = username_input.isalnum()  # Test to check for Letters and Numbers

#     # Creation Loop
#     if taken_test and lower_test and (underscore_test or alpha_num_test) == True:  # Test to see if Username meets all Requirements
#         username += username_input  # If True, adds Username Input to Username Varible.
#         taken_usernames.append(username_input)  # If True, adds Username Input to Taken Usernames.
#         print('Username Made Successfully')
#         break
#     elif taken_test == False:
#         print('Username Taken')
#         continue
#     else:
#         print('Invalid Username')
#         continue


password_input = input('Create Password: ')  # Input for creating a new Password

# Tests for Password
length_test = (len(password_input) >= 8)
space_test = ' ' not in password_input

# Test for the Special Characters in the Password
special_test = '!' in password_input, '?' in password_input, '@' in password_input, '#' in password_input, '$' in password_input, '^' in password_input, '&' in password_input, '*' in password_input, '_' in password_input, '-' in password_input
for s in special_test:
    if s == True:
        special_test = True

for p in password_input:
    if p.isupper():
        uppercase_test = True
    if p.islower():
        lowercae_test = True
    if p.isdigit():
        digit_test = True

if length_test and space_test and uppercase_test and lowercae_test and digit_test and special_test == True:
    password += password_input
    print('Password Made Successfully')
    print(password)