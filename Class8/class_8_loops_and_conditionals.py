'''Loops and conditionals'''

'''What is the difference between a For and While Loop?
How do I write a For Loop?
How do I write a While Loop?'''

# For Loop
colors = ['green', 'blue', 'orange', 'yellow']  # How you can solve the Taken Usernames Problem

# for c in colors:
#     print(c)


# While Loop
# Initialization of Varibles
limit = 26
start = 0

# while start < limit:  # Condition
#     print(start)  # Feedback to User
#     start += 1


''' Break Keyword '''
# Lets look at the 2 examples below and take note where the loop stops
south, north, east, west = '', '', '', ''  # Initializing Varibles on One Line

# userin = ''  # Initialization of Varible
# while userin != 'Stop':
#     userin = input('Enter Something or Hit Stop to Leave Loop: ')
#     print(userin)

# userin = ''  # Initialization of Varible
# while True:
#     userin = input('Enter Something or Hit Stop to Leave Loop: ')
#     if userin == 'Stop':
#         break
#     print(userin)


''' Break in nested loops '''
# # When i = 3, break is skipped. When i = 6, it breaks on 4.
# i = 3

# while i > 0:
#     print(i)
#     i -= 1
#     if i == 4:
#         break
# else:
#         print('Done')

# userin = ''
# # Taking a string from a User until they hit Stop
# while userin != 'Stop':
#     userin = input('Please, enter a word or hit Stop to end Loop: ')

#     for l in userin: # Looping through the input from the User
#         if l.isalpha():  # Testing to see if each character is in the alphabet
#             print(l)
#         else:
#             break
#     print('This is our next Line')


# while True:
#     userinput = input('Enter a Word: ')
#     print('We are on Line 68')
#     print(userinput)
#     print('We are still in the While Loop')
#     break
#     print('I will not Print because the Break Keyword is used above me')
# print("Why am I being Printed?")  # Outside of the Loop


'''
Exercise

Write some code that takes in numbers from a user one at a time. 
This should keep going until the user enters 0. Then print the sum of all the numbers.
If the user inputs something that isn't a number, an error message should appear and the program should stop. (Hint: use break)

Example (no error):
5
12
0
Sum: 17

Example (error):
5
7
c
Error: Not a number
'''

# '''Declare any needed variables'''
# userinput, sum = '', 0

# '''Start our Loop'''
# while True:
#     '''Get User Input'''
#     userinput = input('Enter your Number: ')

#     '''Test for Letters'''
#     if userinput.isalpha():
#         print('Error: Not a Number')
#         break
#     '''Covert to Integer, End and Print Sum if Zero, Otherwise continue to add to Sum'''
#     userinput = int(userinput)  # Recast as Integer

#     if userinput != 0:
#         sum += userinput
#     else:
#         print(f'Sum: {sum}')
#         break


'''Continue keyword'''

'''Example: Use the continue keyword to loop through a string and only print the vowels.'''

# # Option 1  # This method can be used to look for Taken Usernames
# test_string = 'Hello'
# vowels = 'aeiou'

# for t in test_string:
#     if t in vowels:
#         print(t)
#     else:
#         continue

# Option 2
# test_string = 'Hello'

# for t in test_string:
#     if t in 'aeiou':
#         print(t)
#     else:
#         continue


''' 
Exercise:
Sum of Even Digits

Take a string as user input, and verify that it's a number.
Loop through each digit of the number, and only add it to the sum if it's even.
Print the sum of all the even digits at the end. 
Make sure to use the continue keyword.
'''
user_input, sum = '', 0

# while True:
#     user_input = input('Enter your String: ')
#     for u in user_input:  # Loop through string entered by user
#         if u.isalpha():
#             continue  # Continue will allow us to skip the letters
#         else:
#             u = int(u)  # Recasting to a number
#             if (u % 2) == 0:
#                 sum += u
#     print(sum)


''' Break, Continue, and Pass '''
word = 'Hello'
vowels = 'aeiou'

# for l in word:
#     if l in vowels:
#         print(l)
#         break

# for l in word:
#     if l in vowels:
#         continue
#     print(l)

# for l in word:
#     if l in vowels:
#         pass  # Skips the if statement
#     print(l)


'''
Exercise

Write some code that takes in strings from a user one at a time.
After each string is taken in evaluate if the string is empty, a number, a set of letters, or contains symbols.
If the string is empty, stop the loop.
If the string is a number, convert it to a float and add it to a total.
If the string is a set of letters, concatenate to the other letter strings passed in.
If it contains a symbol, or is none of the above, do nothing and repeat the loop.
Make sure to use break and/or continue.


REQUIREMENTS
    If the string is empty, stop the loop.
    If the string is a number, convert it to a float and add it to a total.
    If the string is a set of letters, concatenate to the other letter strings passed in.
    If it contains a symbol, or is none of the above, do nothing and repeat the loop.
'''

'''These variables will be placeholders for the total and new string we will be creating'''
new_total = 0
new_string = ''

while True:
    user_input = input('Enter your Data: ')

    # If Empty, Stop the Loop.
    if len(user_input) == 0:
        print('String is Empty. Stopping the Loop.')
        break
    # If Number, Covert to Float, and Add to Total.
    elif user_input.isnumeric():
        user_input = float(user_input)  # Casting into a FLoat
        new_total += user_input
        print(f'Updated Total is {new_total}')
        continue
    # If concatenate to new string
    elif user_input.isalpha():
        new_string += user_input
        print(f'Updated String is {new_string}')
        continue
    # Check for Special Characters
    elif not user_input.isalnum():
        print(f'{user_input} is Speical Character')
        continue