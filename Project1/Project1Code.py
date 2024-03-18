taken_usernames = ['admin', 'admin123', 'superuser', 'superuser123']
username, password = '', ''
username_input, password_input = '', ''

print('''To sign up, create a Username and Password.
The Username must start with a lowercase letter and only contain letters, numbers, and underscores.
The Password must contain, at least, each of the following.
    ● 8 characters long
    ● One uppercase letter
    ● One lowercase letter
    ● One digit
    ● One of these characters:  !, ?, @, #, $, ^, &, *, _,  -
    ● No spaces''')

while True:
    username_input = input('Create Username: ')
    taken_test = username_input not in taken_usernames
    lower_test = username_input[0].islower()
    underscore_test = ('_' in username_input)
    for u in username_input:
        alpha_num_test = username_input.isalnum()
    if taken_test and lower_test and (underscore_test or alpha_num_test) == True:
        username += username_input
        taken_usernames.append(username_input)
        print('Username Made Successfully')
        break
    else:
        print('Invalid Username')

print(taken_usernames)