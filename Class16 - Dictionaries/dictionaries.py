from statistics import mode

'''Fun facts about dictionaries 
    -collection of keys and values
    -used to store associated information
    -keys are the words, values are the definitions
'''
# How do we create a dictionary?
user = {'user ID': 400, 
        'name': 'Fritz',
        'address': '1515 Mockingbird Lane'}
# print(user)
# print(type(user))


# Access keys with brackets
# print(user['name'])
# print(user['user ID'])
# print(user['address'])


# # Add new key value
# user['state'] = 'NY'
# print(user['state'])
# user['state'] = 'NJ'
# print(user['state'])


# lets look at all the methods available to us
# print(dir(user))


# lets try one
# print(user.__contains__('user ID'))
# print(user.__contains__('city'))


# Dict constructor
new_dict = dict()
# print(new_dict)
# print(type(new_dict))

pet = dict(name='Fido', age=14)
# print(pet)
# print(type(pet))


# Dictionary methods
dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

# Lets use the keys methods to get the keys from this dictionary
# Assign keys to a variable
dog_info = dog.keys()
# print(dog_info)


# Lets use clear method to remove all elements
# print(dog.clear())


# Lets use get method to get a key value
age = dog.get('age')
# print(age)


# # # lets look at one of the parameters to show an error if the key doesnt exist
# print(dog.get('Temperament', 'Key does not exist.'))


# Lets create a copy
new_dog = dog.copy()
# print(new_dog)
# print(type(new_dog))


# Lets remove a specified key with pop
# new_dog.pop('breed')
# print(new_dog)


# Lets remove a last inserted key-value pair with popitem
# new_dog.popitem()
# print(new_dog)


# Get a list with each key-value pair with items
key_values_pair = new_dog.items()
# print(key_values_pair)  # List of Tuples


# we can loop through using the Items Method
# for k, v in new_dog.items():
#     print(k, v)


# Update allows us to update by changing and adding data
# dog.update({'temperament': 'happy', 'breed': 'chihuahua'})
# print(dog)


# Dictionaries vs Lists
list1 = ['a', 'b', 'c', 'd', 'e']
dict1 = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 5: 'e'}

# print(list1[3])
# print(dict1[3])

list1[3] = 'z'
dict1[3] = 'z'

# print(list1[3])
# print(dict1[3])


'''
Write some code that takes two lists and converts them into one dictionary.
In:
list1 = ['one', 'two', 'three']
list2 = [4, 10, 30]
Out:
{'one': 4, 'two': 10, 'three': 30}
'''
# Problem One
list1 = ['one', 'two', 'three']
list2 = [4, 10, 30]

# new_dict = {}
# for n in range(len(list1)):
#     new_dict.update({list1[n]: list2[n]})
# print(new_dict)


# Problem Two
my_keys = ['one', 'two', 'three']
my_values = [4, 10, 30]

# Using Zip & Dict
# my_dict = dict(zip(my_keys, my_values))
# print(my_dict)

# Using dictionary comprehension
# my_dict = {keys: values for (keys, values) in zip(my_keys, my_values)}
# print(my_dict)


'''
Exercise

Write a dictionary that contains five words and their definitions. 
Then have your code print the word and their definition one at a time.
Hint: Use the items() method
'''
words = {"color":"blue", "veggie":"radish", "vehicle": "bike", "mood": "happy", "pet":"cat"}



# As datasets, we can use bracket notation

choices = {"flavors":['strawberry', 'vanilla', 'orange'],
           "sizes":['large', 'medium', 'small']}


'''
Exercise
Create a dictionary for an automobile including make, model, year, number of doors, and number of cylinders.
'''

# car = {"make":"honda", 
#        "model":"accord", 
#        "year":2011 , 
#        "number of doors":4,
#        "cylinders": 6}

# print(car)

'''
In statistics, the mode is the value that appears most frequently in a dataset.
For example, in this list: [1,2,4,1,3,4,1,1] the mode is 1
Write some code that uses a dictionary to calculate the mode of a list.

'''

my_list_items = [1,2,4,1,3,4,1,1] # our list


# Statistics module


# Looping through and adding 
incomes = {"apple": 5600.00, "orange": 3500.00, "banana": 5000.00}



'''
Suppose you have a list of employee records that contain the following information for each employee: name, job title, salary. The records are stored as a list of dictionaries.
Use this list to create a dictionary where the keys are the job titles and the values are the average salaries for each job title.
Example:
records = [{'name': 'Bob', 'title': 'manager', 'salary': 50000},\
           {'name': 'Alice', 'title': 'developer', 'salary': 60000},\
           {'name': 'David', 'title': 'developer', 'salary': 65000}]
Output: {'manager': 50000, 'developer': 62500}
'''

records = [{'name': 'Bob', 'title': 'manager', 'salary': 50000},\
           {'name': 'Alice', 'title': 'developer', 'salary': 60000},\
           {'name': 'David', 'title': 'developer', 'salary': 65000},
           {'name': 'Alice', 'title': 'consultant', 'salary': 25000},\
           {'name': 'David', 'title': 'consultant', 'salary': 40000}]









 



