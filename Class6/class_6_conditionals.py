''' Conditionals '''

''' Lets follow through the two code snippets below'''

# # This will run
# x = 20
# y = 15

# if x > y:
#     print(x)


# # This will not run
# x = 20
# x = 20

# if x > y:
#     print(x)


'''
Exercise

Write some code that prints “This is odd” if the user inputs an odd number.
(Hint: use an if statement)
Example:
User input: 7
This is odd

'''

# We can use modulus to figure out odd or even
# val = 6
# result = val % 2
# print(result)


'''Exercise Solution'''
# user_input = int(input('Enter a Number: '))

# if user_input % 2 != 0:
#     print('This is Odd')


''' Else If (Elif) Statements '''
'''
We want a small program that will tell a student their grade based on the following scale

A - Between 90 and 100
B - Between 80 and 89
C - Between 70 and 79
D - Between 65 and 69
F - Anything under 65
'''
# score = int(input('Enter your Grade: '))

# if score >= 90 and score <= 100:
#     print('Grade A')
# elif score >= 80 and score < 90:
#     print('Grade B')
# elif score >= 70 and score < 80:
#     print('Grade C')
# elif score >= 65 and score < 70:
#     print('Grade D')
# else:
#     print('Grade F')


'''
Exercise
Add to your previous code so it prints “This is odd” if the user enters an odd number, and “This is even” if the user enters an even number.
(Hint: add an elif statement)

Examples:
User input: 7
This is odd

User input: 12
This is even

'''

''' Exercise solution with an elif and else'''
# user_input = int(input('Enter a Number: '))

# if user_input % 2 != 0:
#     print('This is Odd')
# elif user_input % 2 == 0:
#     print('This is Even')


'''
Exercise
Add to your previous code so if the user enters something that isn't an odd number or an even number, print “Unknown”.


Examples:
User input: 7
This is odd

User input: 12
This is even

User input: 9.2
Unknown


'''

''' Exercise solution(s)'''
# # Option One
# try:
#     user_input = int(input('Enter a Number: '))
# except:
#     print('Unknown')
# else:
#     if int(user_input) % 2 != 0:
#         print(f'{user_input} is Odd')
#     else:
#         print(f'{user_input} is Even')


# # Option Two
# user_input = input('Enter a Number: ')

# if not user_input.isdecimal():
#     print(f'{user_input} is Unknown')
# elif int(user_input) % 2 != 0:
#     print(f'{user_input} is Odd')
# else:
#     print(f'{user_input} is Even')
    

'''
Exercise

Write some code that takes in a string from the user and prints whether the string is a number, if it is a word, or something else.

Examples:
User input: 7
This is a number

User input: abcde
This is a word

User input: 7!ab5
This is something else

'''
user_input = input('Enter Input: ')

if user_input.isdecimal():
    print(f'{user_input} is a Number')
elif user_input.isalpha():
    print(f'{user_input} is a Word')
else:
    print(f'{user_input} is Something Else')


'''Chaining Conditionals code results'''

# Mutually exclusive
    
# temp_f = 35
# if temp_f > 70:
#     print("It is hot outside")
# elif temp_f > 40:
#     print("It's moderate outside")
# else:
#     print("It's cold outside")


# result - evaluated separately and multiple of them could be run
    
# temp_f = 75
# if temp_f > 70:
#     print("It is hot outside")
# if temp_f > 40:
#     print("It's moderate outside")
# if temp_f <= 40:
#     print("It's cold outside")

# 70 won't run
# temp_f = 70
# if temp_f > 70:
#     print("It is hot outside")
# if temp_f > 40 and temp_f < 70:
#     print("It's moderate outside")
# if temp_f <=40:
#     print("It's cold outside")


# nested conditionals
num = 5

# if num % 2 == 1:
#     if num < 10:
#         if num > 0:
#             print("This is a single digit odd number")

# if num % 2 and num < 10 and num > 0:
#     print("This is a single digit odd number")


'''
Exercise

You're working on a project to develop a login system for a website. The website requires the user to enter a username and password to log in. Write a Python program that checks whether the user entered the correct username and password.
Create two variables called username and password and set them to any valid string values.
Prompt the user to enter their username and password using the input() function.
Use conditionals and logical operators to check whether the username and password entered by the user match the username and password variables.
If they match, print “Login successful.” If they don't, print “Incorrect username or password.”
'''
''' Exercise solution '''



# Prompt the user to enter their username and password using the input() function.


# Create two variables called username and password and set them to any valid string values.


# Create your conditional






