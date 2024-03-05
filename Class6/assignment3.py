'''
Exercise

You're working on a project to develop a login system for a website. 
The website requires the user to enter a username and password to log in. 
Write a Python program that checks whether the user entered the correct username and password.
Create two variables called username and password and set them to any valid string values.
Prompt the user to enter their username and password using the input() function.
Use conditionals and logical operators to check whether the username and password entered by the user match the username and password variables.
If they match, print “Login successful.” If they don't, print “Incorrect username or password.”
'''
''' Exercise solution '''

# Prompt the user to enter their username and password using the input() function.
username_input = input('Enter Username: ')
password_input = input('Enter Password: ')

#Clean Input
username_input = username_input.strip()
password_input = password_input.strip()

# Create two variables called username and password and set them to any valid string values.
username = 'MysticElla'
password = 'YuGi1989!'

# Create your conditional
if username_input == username and password_input == password:
    print('Login Successful')
else:
    print('Incorrect Username or Password')