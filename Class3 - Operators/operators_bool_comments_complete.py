# Operators, Boolean Expressions, and Comments

# I am a comment

# Everything after the hash will be ignored when you run your code

temperature = 95 # I can be an inline comment

# Or I can be a standard single-line comment
weekday = 'Wednesday'


first_name = 'Thomas' ''' Multi-line comments can be inline '''
last_name = 'The Train' """ This makes an inline comment as well """

'''
I am a multi-line comment and 
can easily be used to span 
multiple lines in a Python file
'''

"""
You can also use the double quotes
to create as a multi-line comment.
Anything in between these three quotes will not run
"""

'''
Comments that contradict the code are worse than no comments. Always make a priority of keeping the comments up-to-date when the code changes!
'''

'''
Ensure that your comments are clear and easily understandable to other speakers of the language you are writing in.

'''

'''
An inline comment is a comment on the same line as a statement. Inline comments should be separated by at least two spaces from the statement. They should start with a # and a single space.
'''

# Inline comments are unnecessary and in fact distracting if they state the obvious.

# Comment me!

# length = 5  
# width = 7 
# perimeter = 2 * (length + width)
# print(perimeter)


# Comment me!

# fahrenheight = 89 
# celsius = (fahrenheight - 32) * 5/9
# print(celsius)


# Shortcut operators

# Add 5 to me using shortcut operator +

# age = 25
# age += 5
# print(age)

# Add 10 to me using shortcut operator +

# year = 2024
# year += 10
# print(year)

# Subtract 20 -

# num_one = 55
# num_one -= 20
# print(num_one)

# Subtract 15 -

# num_two = 11
# num_two -= 15
# print(num_two)


# Multiply by 3 *

# my_value = 9
# my_value *= 3
# print(my_value)

# Multiply by 10 *

# mileage = 15
# mileage *= 10
# print(mileage)

# Divide by 2 /
# pizza_slices = 8
# pizza_slices /= 2
# print(pizza_slices)

# Divide by 7 /
# fees = 8.90
# fees /= 7
# print(fees)

# Raise to the 3rd power **
# num_three = 6
# num_three **= 3
# print(num_three)

# Raise to the 2nd power **
# data = 16
# data **= 2
# print(data)

# Integer divide by 3 //
# val_one = 16
# val_one //= 3
# print(val_one)

# Integer divide by 4 //
# val_two = 9
# val_two //= 4
# print(val_two)

# Find the remainder if divided by 3 %
# val_three = 10
# val_three %= 3
# print(val_three)

# Find the remainder if divided by 5 %
# val_four = 14
# val_four %= 5
# print(val_four)


# Refactor the fahrenheit/celsius converter using shortcut operators

# fahrenheight = 89 
# celsius = (fahrenheight - 32) * 5/9
# print(celsius)

# fahrenheit = 89 
# fahrenheit -=32
# fahrenheit *= 5/9
# celsius = fahrenheight
# print(celsius)


# Boolean Operators

# Is 7 less than 5? <

# print(7 < 5)
# result = (7 < 5)
# print(result)


# Is 4 less than or equal to 4? <=

# print(4 <= 4)
# result = (4 <= 4)
# print(result)

# Is 6 greater than 2? >

# print(6 > 2)
# result = (6 > 2)
# print(result)

# Is 5 greater than or equal to 6? >=

# print(5 >= 6)
# result = (5 >= 6)
# print(result)

# Is 5 equal to 5? ==

# print(5 == 7)
# result = (5 == 7)
# print(result)

# Is 100 not equal to 75? !=

# print(100 != 75)
# result = (100 != 75)
# print(result)

# and

# print(5 == 5 and 4 == 4) # these are true because both are true
# print(5 == 5 and 4 == 3) # one true and one false equals false
# print(4 == 2 and 1 == 8) # false because both are false

# Values from example 1 can be stored in variables

# log_1 = (5 == 5)
# log_2 = (4 == 4)
# print(log_1 and log_2)

# or
# print(5 == 5 or 5 == 3)

# not
# x = 5
# y = 7
# # Is x less than y?
# print(x < y)
# print(not x < y)

# Are we the same object? is 
# fname = 'Taylor'
# new_name = fname
# print(fname is new_name)

# in
# print('J' in 'January') # true
# print('F' in 'January') # false 

# eval
# is_hot = 'True'
# is_wednesday = 'False'

# print(eval(is_hot))
# print(eval(is_wednesday))
