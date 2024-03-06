'''
You have a variable called hours which equals 24, the number of hours in a day.
Print There are 24 hours in a day. Make sure to use your variable.
First, print using commas. Remember that using commas automatically adds spaces!
Now, print using string concatenation. Remember to cast hours to a string and manually add the spaces!
'''
# hours = 24
# print('There are',hours,'in a day.')
# print('There are' + str(hours) + 'in a day.')
# print(f'There are {hours} in a day.')


'''
Write some code that will print a box around a string.

Examples:
User input: hello
*******
*hello*
*******

User input: programming is fun
********************
*programming is fun*
********************
'''
# user_input = 'I Love Programming'
# border = (len(user_input) * '*' + '**') 
# print(border)
# print('*' + user_input + '*')
# print(border)


'''
You need to write a script that will generate an email to a customer who has just made a purchase. You have 3 variables:
name, which stores the customer's name as a string
product, which stores the product name as a string
price, which stores the price of the product as a float
Use an f-string to generate an email message with the following text, and print it. Make sure to round the price to 2 decimal places. The email should be one multi-line string.
Dear {name},
Thank you for your purchase of a {product}. Your credit card has been charged ${price}.
We appreciate your business and look forward to serving you again.
Sincerely,
The ABC Company
'''
# name = 'Josiah Wilson'
# product = 'ABC Sneakers'
# price = 74.95343452342
# # Remember to format the price

# print(f'''
# Dear {name},
# Thank you for your purchase of a {product}. Your credit card has been charged ${price:.2f}.
# We appreciate your business and look forward to serving you again.
# Sincerely,
# The ABC Company
# ''')


'''
Write some code that takes a string and tells if it is a palindrome (same forwards and backwards).
Hint: Use indexing/slicing and boolean expressions

Examples:
racecar: True
cat: False
'''
word = 'racecar'

reverse_word = word[::-1]

if word == reverse_word:
    print('You have a palindrome.')
else:
    print('Not a palindrome.')