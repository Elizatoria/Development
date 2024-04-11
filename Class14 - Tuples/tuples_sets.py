'''Tuples & Sets'''

'''
Fun Facts about Tuples
    -ordered and unchangeable (example, storing a username and password, storing an RGB value that must not change)
    -can't add or remove items
    -round brackets
    -faster than lists
    -used to store constants
    -used heterogeneous data structures (integers, floats, strings, etc) 
    for example someone's age, gender and last name, (15, 'M', 'JONES')
    -heterogenous data structures save memory. why? lists need to over-allocate to account for new elements
    -readability
    -lets the programmer or other programmer know, this data collection should not be altered
'''
## Count & Indexing

# Use the count Tuple method to count how many instances we have for 2, 3, 8, 9, 10
my_number_tuple = (1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 8, 8, 8, 9, 10, 10, 10, 10)

# print(my_number_tuple.count(2))
# print(my_number_tuple.count(3))
# print(my_number_tuple.count(8))
# print(my_number_tuple.count(9))
# print(my_number_tuple.count(10))


# Use the index tuple method to return the position of letters b, d, f, h, and i
my_letter_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')

# print(my_letter_tuple.index('b'))
# print(my_letter_tuple.index('d'))
# print(my_letter_tuple.index('f'))
# print(my_letter_tuple.index('h'))
# print(my_letter_tuple.index('i'))


# Unpacking
user = ('Joe', 'Smith', 24)

# fname, lname, age = user
# print(fname)
# print(lname)
# print(age)


# colors = 'blue', 'green', 'red', 'orange'
# color1, color2, color3, color4 = colors
# print(color1)
# print(color2)
# print(color3)
# print(color4)


# Loop through list of Tuples
weekdays = [("Monday", 1), ("Tuesday", 2), ("Wednesday", 3), ("Thursday", 4), ("Friday", 5), ("Saturday", 6), ("Sunday", 7)]

# for day, num in weekdays:  # Looping through List of Tuples
#     print(f'{day} is day {num} of the week.')


# Adding tuples
first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)

# third_tuple = first_tuple + second_tuple
# print(third_tuple)


'''
You have a tuple of numbers:
numbers = (1,2,3,4,5,6,7,8,9,10,11,12)
You have a tuple of months:
months = ("January","February","March","April","May","June", "July","August","September","October","November","December")
Use these tuples to make a list of tuples where each tuple contains a number and the month it corresponds to, like this: 
[("January",1),...,("December",12)]
Now print each month and its number using tuple unpacking in a for loop. The first line of output should look like this:
January is month 1 of the year.
'''
months = ("January","February","March","April","May","June", "July","August","September","October","November","December")
numbers = (1,2,3,4,5,6,7,8,9,10,11,12)

# # Create List of Tuples
# calender = []  # Will hold the List of Tuples

# for n in range(len(numbers)):
#     calender.append((months[n], numbers[n]))
# # print(calender)

# # Use a for loop to unpack and generate strings
# for month, num in calender:  
#     print(f'{month} is month {num} of the year.')


'''
Fun Facts about Sets

-unordered, unchangeable*, and unindexed.
* The items are unchangeable, but you can add and remove items.
Sets do not allow duplicates, so they are used to store a set of unique values. You use curly brackets for sets: { }
Because sets are unordered, you can't index them like a list. They don't have indexes at all. 
You can still loop through a set with a for loop.
'''
# Ways to create a set
i_am_empty = set()

# print(i_am_empty)
# print(type(i_am_empty))


# What am I?
check_my_type = {}

# print(type(check_my_type))


# Pass in a list
my_fav_colors_list = ['green', 'blue', 'red']

# my_fav_colors_set = set(my_fav_colors_list)  # Converts List into a Set
# print(my_fav_colors_set)
# print(type(my_fav_colors_set))


# Unordered
my_unordered_set = {'blue', 'green', 'red', 'orange'}

# print(my_unordered_set)  # Each time it prints, it changes order.


# Unchangeable
my_unchangeable_set = {'hello', 'welcome', 'to', 'newyork'}

# my_unchangeable_set[3] = {'vermont'}  # Will not Work, Only Works on Lists
# print(my_unchangeable_set)


# Unindexed
my_unindexable_set = {'I', 'cant', 'be', 'indexed'}

# print(my_unindexable_set[2])  # Gives Error because Sets can't be indexed


# # Break up a string
# first_name = set('John')  # Breaks up a String into a List
# print(first_name)


# No duplicates allowed
my_cars = {'chevy', 'toyota', 'ford', 'ford', 'honda', 'honda'}
# print(my_cars)


'''
8. Exercise: Removing All Duplicates
You have a list storing important data for your company, but it contains some duplicate entries. 
Go through your list and remove all the duplicates. When you're done, each item should appear in 
the list exactly once.
'''
# No duplicates - How did we solve this problem before?
'''With a for loop and appending'''
#original list
# states = ['alaska', 'alaska', 'alaska', 'alabama', 'alabama', 'new york', 'new york', 'new york']

# no_duplicate_states = []

# for s in states:
#     if s not in no_duplicate_states:
#         no_duplicate_states.append(s)
# print(no_duplicate_states)


'''With sets and returning a list'''
states = ['alaska', 'alaska', 'alaska', 'alabama', 'alabama', 'new york', 'new york', 'new york']

# new_states = list(set(states))
# print(new_states)


# We can loop through sets
top_ten_movies = {'Shawshank Redemption', 'Avatar', 'Avengers', 'Its a Wonderful Life'}

# for t in top_ten_movies:
#     print(t)


# Let's add silver .add()
colors = {'blue', 'green', 'red'}

# colors.add('silver')
# print(colors)


# Lets clear all our items .clear()
transportation = {'cars', 'bikes', 'plane'}

# transportation.clear()
# print(transportation)


# Lets create a copy .copy()
sitcoms = {'friends', 'seinfeld', 'honeymooners'}

# comedy = sitcoms.copy()
# print(sitcoms)
# print(comedy)


# Remove vermont from our set
states = {'california', 'new york', 'vermont', 'connecticut'}

# states.remove('vermont')
# print(states)


'''Break'''
# Difference - What's different?
student_set = {'oleg', 'anna', 'farley'}
student_set_2 = {'oleg', 'anna', 'brenetta'}

# result = student_set - student_set_2  #Operator
# result2 = student_set_2 - student_set
# print(result)
# print(result2)

# result = student_set.difference(student_set_2)  # Method
# result2 = student_set_2.difference(student_set)
# print(result)
# print(result2)


# Intersect - What do we have in common?
my_schedule = {'mon', 'wed', 'thurs'}
dana_schedule = {'wed', 'fri', 'sat'}

# result = my_schedule & dana_schedule  # Operator
# print(result)

# result2 = my_schedule.intersection(dana_schedule)  # Method
# print(result2)


# Union - uniquely list every pet
sarah_pets = {'dog', 'cat', 'bird'}
isaiah_pets = {'chickens', 'dog', 'fish'}
khadaziah_pets = {'bird', 'dog', 'fish'}
brenetta_pets = {'turtle'}

# result = sarah_pets | isaiah_pets | khadaziah_pets | brenetta_pets  # Operator
# print(result)

# result2 = sarah_pets.union(isaiah_pets, khadaziah_pets, brenetta_pets)  # Method
# print(result2)


# Symmetric difference - Items outside of matching items
my_books = {'catcher in the rye', 'richest man in babylon'}
her_books = {'catcher in the rye', 'richest man in babylon', 'sounder'}

# result = my_books ^ her_books  # Operator
# print(result)

# result2 = my_books.symmetric_difference(her_books)  # Method
# print(result2)


'''
Exercise - Sets
You work for a sales company and must generate a set of all customers who get a certain discount. 
The criteria for getting a discount is that they're over 60 years old and have made at least 5 purchases.
You have a set of customers over 60, and a set of customers who have made at least 5 purchases. 
Use a set operation to output a set of customers that fit both criteria for the discount. You can do this in one line of code.
Example:
over_60_years = {'Dominic', 'Linda', 'Simone', 'Swathi', 'Olaf'}
over_5_purchases = {'Finn', 'Simone', 'Aaron', 'Dominic'}
Output: {'Dominic', 'Simone'}
'''
over_60_years = {'Dominic', 'Linda', 'Simone', 'Swathi', 'Olaf'}
over_5_purchases = {'Finn', 'Simone', 'Aaron', 'Dominic'}

# discounts = []

# for o in over_60_years:
#     if o in over_5_purchases:
#         discounts.append(o)
# print(discounts)

# Solve with an intersection - solve with 1 or 2 lines of code
over_60_years = {'Dominic', 'Linda', 'Simone', 'Swathi', 'Olaf'}
over_5_purchases = {'Finn', 'Simone', 'Aaron', 'Dominic'}

# result = over_60_years.intersection(over_5_purchases)
# print(result)


'''
Exercise - Sets
See flowchart
You work at a company where some people know Python, some people know JavaScript, and some people know both.
In a loop, prompt the user to input an employee name, whether they know Python, and whether they know JavaScript. 
Use this to build two sets: a set of employees that know Python, and a set of employees that know JavaScript.
Use set operators to compute the following sets:
The set of employees that know both Python and JavaScript
The set of employees that know JavaScript, but not Python
The set of employees that know Python or JavaScript, but not both
'''
'''Solution April 10, 2024'''
# instructions
print('''
JS and Python Developer Tracker
Instructions
Input 's' or 'stop' at anytime to exit Program.
To add a Python Developer, type 'p' when Prompted. 
To add a JavaScript Developer, type 'js' when Prompted. 
''')

# initialize our variables
python_devs, js_devs = set(), set()
dev_type_input, dev_name_input = '', ''

# put our error messages in a tuple
error_messages = ('Invalid Input, Please Try Again.', 'Thank You. Have a Nice Day.')
 
# while loop
while True:
    # inputs
    dev_type_input = input("Type 'p' for Python Developer, 'js' for JavaScript Developer, or 'stop' to exit program: ").lower()
    # if statements, break keyword, continue
    # Gives User an Exit
    if dev_type_input == 'stop':
        print(error_messages[1])
        break
 
    # Get Dev Type, Add to Sets, and Offer an Exit
    if dev_type_input == 'p' or dev_type_input == 'js':
        # inputs
        dev_name_input = input("Enter Developer Name: ").lower()

        if dev_name_input == 'stop':
            print(error_messages[1])
            break
        # string methods for cleanup if needed .strip(), .title()
        # sets
        elif dev_type_input == 'p':
            python_devs.add(dev_name_input.title())
        else:
            js_devs.add(dev_name_input.title())
    else:
        print(error_messages[0])
        continue

    # Logic for Handling Sets
    both_languages = python_devs.intersection(js_devs)
    know_js_not_python = js_devs.difference(python_devs)
    know_python_or_js_not_both = js_devs.symmetric_difference(python_devs)
 
    #If sets are empty, display no data for User
    if both_languages == set():
        both_languages = 'No Data'

    if know_js_not_python == set():
        know_js_not_python = 'No Data'

    if know_python_or_js_not_both == set():
        know_python_or_js_not_both = 'No Data'

    # print statement, formatted strings, to display the set results
    print('RESULTS')
    print('--------------------')
    print(f'The following Developers know both Languages: {both_languages}')
    print(f'The following Developers know JavaScript but not Python: {know_js_not_python}')
    print(f'The following Developers know Python or JavaScript but not Both: {know_python_or_js_not_both}')
    print('--------------------')