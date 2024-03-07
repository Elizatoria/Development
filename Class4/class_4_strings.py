''' Class 4 Strings '''

# String operators

'''Concatenation'''
operator_code = 'A987'
part_id = '49Be'
item_id = operator_code + part_id
# print(item_id)


''' Create two variables, one to capture first name, another for last name. 
Combine them to a third variable to display the user's full name. '''
first_name = 'Joe'
last_name = 'Smith'
full_name = first_name + ' ' + last_name
# print(full_name)


''' Multiplication '''
greeting = 'hip hip hooray ' * 3
# print(greeting)

''' Using multiplication, create a new string that multiplies your favorite color 5 times'''
my_fav = 'Blue ' * 5
# print(my_fav)


# Reference vs Value equality
x = 'hello'
str2 = 'HELLO'.lower()
# print(x)
# print(str2)
# print(x == str2)
# print(x is str2)
# print(id(x))
# print(id(str2))


''' in - Returns True if a string appears inside another string (as a substring), and False otherwise.'''
test_character = 'b'
test_string = 'bananas'
# print(test_character in test_string) #?


''' create a quick test to see if the sub string 'spreh' can be found in the string 'Incomprehensibilities' '''
test_chars = 'spreh'
test_word = 'Incomprehensibilities'
# print(test_chars in test_word)


''' len() - Returns the length of a string, aka the number of characters in a string.'''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
length_of_alphabet = len(alphabet)
# print(length_of_alphabet)


''' create a variable that holds a string of your favorite animal, 
create a variable to capture the length of that animal's string value'''
animal = 'zebra'
length_of_animal = len(animal)
# print(length_of_animal)


# String methods

word_1 = 'happy' # capitalize me!
# print(word_1.capitalize())
# print('happy'.capitalize())


ex_1 = 'cereal' # capitalize me!
# print(ex_1.capitalize())
# print('cereal'.capitalize())


word_2 = 'SuPrISe' # make me lower case!
# print(word_2.casefold())
# print('SuPrISe'.casefold())


ex_2 = 'RuMMaGe' # make me lower case!
# print(ex_2.casefold())
# print('RuMMaGe'.casefold())


word_3 = 'ZOO' # make me lower case!
# print(word_3.casefold())
# print(word_3.lower())


ex_3 = 'PLANET' # make me lower case!
# print(ex_3.casefold())
# print(ex_3.lower())


'''FUN FACT: Whereas casefold() method is an advanced version of lower() method, 
it converts the uppercase letter to lowercase including some special characters which are not specified in the ASCII table 
for example ‘ß’ which is a German letter and its lowercase letter is 'ss'.'''


word_4 = 'Good Evening'
# print(word_4)
# print(word_4.center(100))
# print(word_4.center(50))


ex_4 = 'Hello World!' # center me within a space of 65 characters
# print(ex_4.center(65))


word_5 = 'Pseudopseudohypoparathyroidism' # How many p's?
# print(word_5.count('p'))


ex_5 = 'Antidisestablishmentarianism' # how many times does the letter 'e' occur?
# print(ex_5.count('e'))


word_6 ='I\tam\ta\ttab'
# print(word_6)
# print(word_6.expandtabs(10))


ex_6 = "Let's\t do\t some\t coding!" # lets try to increase the tabs to 15 whitespaces
# print(ex_6.expandtabs(15))


# Find the position of the letter k
word_7 = 'Omphaloskepsis'
# print(word_7.find('k'))

ex_7 = 'Dichlorodifluoromethane' # find the position of the letter f
# print(ex_7.index('f'))

word_8 = 'Supercalifragilisticexpialidocious'
# print(word_8.find('g'))


'''Fun Fact - Both index() and find() are identical in that they return the index position 
of the first occurrence of the substring from the main string. 
The main difference is that Python find() produces -1 as output if it is unable to find the substring, 
whereas index() throws a ValueError exception.'''


# isalnum() Are all my characters alphanumeric? Alphanumeric is A-Z, a-z and 0-9

test_1 = 'abcdef'
test_2 = '%$123'
# print(test_1.isalnum())
# print(test_2.isalnum())

ex_8 = '123*' # Am I alphanumeric?
# print(ex_8.isalnum())


# isalpha() Are all characters in the string in the alphabet?

test_3 = 'abcde'
test_4 = '012345'
# print(test_3.isalpha())
# print(test_4.isalpha())

ex_9 = 'LMN0P' # Are we all in the alphabet
# print(ex_9.isalpha())


# isdecimal() Are all characters decimals?

test_5 = '1234P'
test_6 = '234567'
# print(test_5.isdecimal())
# print(test_6.isdecimal())

ex_11 = '123456' # Check for decimals?
# print(ex_11.isdecimal())


# isdigit() Are all characters digits?

test_7 = 'H1234'
test_8 = '9876'
# print(test_7.isdigit())
# print(test_8.isdigit())

ex_10 = '123Hello' # Check for digits!
# print(ex_10.isdigit())


''' Fun fact isdecimal() method supports only Decimal Numbers. 
isdigit() method supports Decimals, Subscripts, Superscripts. 
isnumeric will check for unicode characters.'''


# islower() Lets check for lowercase

test_9 = 'Zebra'
test_10 = 'affordable'
# print(test_9.islower())
# print(test_10.islower())

ex_12 = 'Username' # check if all lowercase
# print(ex_12.islower())


# isupper() lets check for ALL uppercase

test_11 = 'Marshall'
test_12 = 'HALLOWEEN'
# print(test_11.isupper())
# print(test_12.isupper())

ex_13 = 'TEMPLE' # check if uppercase
# print(ex_13.isupper())


# isspace() Lets check for whitespace (someone enters nothing for an input)

test_13 = '    '
test_14 = 'j      b    c'
# print(test_13.isspace())
# print(test_14.isspace())

ex_14 = '   ' # check if whitespace
# print(ex_14.isspace())


# istitle() Let's check for title case

test_15 = 'Eye of the tiger'
test_16 = 'Eye Of The Tiger'
# print(test_15.istitle())
# print(test_16.istitle())

ex_15 = 'Tempus Fugit' # check for title casing
# print(ex_15.istitle())


# join() Joins the elements of an iterable to the end of the string

my_colors = ['blue', 'green', 'red', 'orange', 'blue']
new_string = '-'.join(my_colors)
# print(new_string)

ex_16 = ['summer', 'spring', 'fall', 'winter'] # create a string from this list and separate it with an asterisk
new_ex = '*'.join(ex_16)
# print(new_ex)


# lower() Converts a string into lower case
day = 'MONDAY'
new_day = day.lower()
# print(new_day)


# partition() Returns a tuple where the string is partitioned into three parts
test_17 = 'I am excited about spring time.'
new_tuple = test_17.partition('about')
# print(new_tuple)

ex_17 = 'We will be going to the park next week.' # partition this string on the word 'going'
new_part = ex_17.partition('going')
# print(new_part)


# replace() Returns a string where a specified value is replaced with a specified value
food = 'My favorite food is pizza.'
new_food = food.replace('pizza', 'potatoes')
# print(new_food)

ex_18 = 'Today is Tuesday. Tuesday we play golf.' # replace instances of Tuesday with Thursday
today = ex_18.replace('Tuesday', 'Thursday')
# print(today)


# split() Splits the string at the specified separator, and returns a list
test_18 = 'I will be broken up on every space'
new_list = test_18.split(' ')
# print(new_list)

ex_19 = 'Split*me*up*on*the*asterisk' # split this string up on every asterisk
ex_list = ex_19.split('*')
# print(ex_list)


# splitlines() Splits the string at line breaks and returns a list
lyrics = "Every time that I look in the mirror\nAll these lines on my face getting clearer\nThe past is gone\nOh, it went by like dusk to dawn\nIsn't that the way?"
new_lyrics = lyrics.splitlines()
#print(new_lyrics)


# startswith() Returns true if the string starts with the specified value
name = 'giraffe'
new_name = name.startswith('g')
# print(new_name)

ex_20 = 'summer' # Check if this string starts with an 's'
ex_start = ex_20.startswith('s')
print(ex_start)


# strip() Returns a trimmed version of the string
username = '   jessica123    '
username_clean = username.strip()
# print(len(username))
# print(len(username_clean))

ex_21 = '  sportsfan876  ' # sanitize this string
ex_21_clean = ex_21.strip()
# print(len(ex_21))
# print(len(ex_21_clean))


'''
Write some code that will take a string from the user and print if it is a number or not.

Examples:
apple
False

4
True
'''
# # Get input from user
# user_input = input('Please, enter your input: ')

# # Test input
# result = user_input.isdigit()

# # Provide output
# print('Is your input a Number or not?', result)
# print(f'Is {user_input} a Number or not?', result)


'''
Take a word from the user. Then take a number from the user. Then print whether the word is longer than the number.

Examples:
apple
6
False

python
4
True
'''
# # Get user input
# user_word_input = input('Enter a Word: ')
# user_number_input = int(input('Enter a Number: '))

# # Convert where needed
# length_of_word = len(user_word_input)

# # Comparison
# result = (length_of_word > user_number_input)

# # Output
# print(f'Is {user_word_input} longer than {user_number_input}?', result)


'''
Exercise 

Write some code that takes a string from the user, and prints how many vowels are in the string. (Vowels are a, e, i, o, u)
How will you count both uppercase and lowercase vowels?
What string method can you use to count the number of vowels?

Example
User input: Computer
3
'''



'''
You have a variable called hours which equals 24, the number of hours in a day.
Print There are 24 hours in a day. Make sure to use your variable.
First, print using commas. Remember that using commas automatically adds spaces!
Now, print using string concatenation. Remember to cast hours to a string and manually add the spaces!

'''


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

# get input


# get length for top and bottom border

# create output, dont forget to append asterisk to front and back of the string