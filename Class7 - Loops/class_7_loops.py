''' Loops '''

''' While Loops '''

''' While my start value is less than my end value, we will increment by 1'''
# end = int(input('Enter a Number: '))
# start = 0

# while start < end:
#     print(start)
#     start += 1


''' While my start value is less than my end value, we will decrement by one - You can stop the infinite loop by hitting ctrl + c'''
# end = 20
# start =0

# while start < end:
#     print(start)
#     start -= 1


''' Example Create a while loop that prints every integer from 1 to 10.'''
# start = 1
# end = 10

# while start <= end:
#     print(start)
#     start += 1


'''
While Loops and User Input

While loops are often paired with user input. The condition for the loop might be what the user needs to enter to stop the loop. 
The user is prompted for input each time it loops, and something happens based on that input.
This allows you to take user input multiple times without writing multiple lines of input(). 
It also allows the user to control how much input they give.

Lets look at code that will run infinitely until the user tells it to "stop"
'''
# userin = ''

# while userin != 'Stop':
#     userin = input('Enter a Word to Continue or Stop to End Loop: ')
#     print(userin)


'''
Exercise

Improve the login system we wrote last class to allow multiple attempts. 
You're developing a login system for a website. 
Write a Python program that checks whether the user has entered the correct username and password. Just like before:
Create two variables called username and password.
Prompt the user to enter their username and password.
Use conditionals and logical operators to check whether the username and password entered by the user match the username and password variables.
As long as the username and password are incorrect, print “Incorrect username or password”, and keep asking the user for their username and password.
If they match, print “Login successful” and end the program.
'''
# # Set sys id and pass
# sys_id = 'Admin'
# sys_password = 'Password'

# # Prompt User
# user_id = input('Enter Username: ')
# user_password = input('Enter Password: ')

# # Our initial check, while not equal we will enter loop
# while sys_id != user_id and sys_password != user_password:
#     print('Incorrect Username and Password')
#     user_id = input('Enter Username: ')
#     user_password = input('Enter Password: ')

# print('Successful Login')


''' For Loops '''

# STRING
my_string = 'Supercalifragilisticexpialidocious'
# for s in my_string:
#     print(s)


# LIST
my_list = ['dog', 'cat', 'bird', 'giraffe', 'fox', 'elephant', 'mouse', 'zebra']
# for animal in my_list:
#     print(animal)


# TUPLE
my_tuple = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')
# for month in my_tuple:
#     print(month)


# DICTIONARY
my_dictionary = {"First name": "Jill",
                 "Last name": "Simmons",
                 "Age": 34,
                 "Address":"1515 Mockingbird Lane"}

# for k in my_dictionary.keys():
#     print(k)

# for v in my_dictionary.values():
#     print(v)

# for k, v in my_dictionary.items():
#     print(k,v)


# SET
my_set = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
# for days in my_set:
#     print(days)


# RANGE
# for x in range(10, 25):
#     print(x)


'''
Write a for loop that loops through a string, counts all the letters, and then print how long the string is.
'''
# word = 'Supernova'
# count = 0

# for w in word:
#     count += 1

# print(f'Length of {word}:', count)


''' Exercise

Take a string from the user. Verify that it's a number.
Write a for loop that adds all the digits together. Then print the total.

Example:
'14253'
15

Hint: remember to cast to int() for each digit in the loop
'''
# sum = 0
# number = '14253'

# for n in number:
#     if number.isdecimal():
#         n= int(n)
#         sum += n

# print(f'Sum of {number}:', sum)


# sum = 0
# user_input = input('Enter String of Numbers: ')

# for t in user_input:
#     if user_input.isdecimal():
#         t = int(t)
#         sum += t

# print(f'Sum of {user_input}:', sum)


''' Exercise 
Write some code that will loop through a string and print whether each letter is a vowel or consonant.

Example:
'hello'
h is a consonant
e is a vowel
l is a consonant
l is a consonant
o is a vowel
'''
# word = 'Hello'
# vowels = ['a', 'e', 'i', 'o', 'u']

# for w in word:
#     if w in vowels:
#         print(f'{w} is a Vowel')
#     else:
#         print(f'{w} is a Consonant')


''' Exercise 
You're working on a data analysis project for a company that looks at written text. 
You're only interested in letters from A-Z because you're analyzing language. 
However, the data you're given has some values that shouldn't be there.
Write a Python program that takes a string as input from the user, removes anything from the string that isn't a letter, and prints the new string.
You can loop through the string in a for loop, use the .isalpha() string method, and remember that strings are immutable, so you will have to build a new string from scratch using string concatenation.
'''
# result = ''
# user_input = input('Enter Data: ')

# for u in user_input:
#     if u.isalpha():
#         result += u
#     else:
#         print(f'{u} is not a Letter')

# print(result)