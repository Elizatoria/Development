import math

'''Hello World'''
# def hello_world():
#     print('Hello World')

# hello_world()  # Function Call


'''Greeting - Function with Print Statement'''
# def greeting(name):
#     print('Hello', name)

# greeting('Sarah')  # Fuction Call, Argument Sarah


'''Greeting - Function with Return Statement'''
# def greeting(name):
#     return f'Hello {name}'

# print(greeting('Sarah'))  # To see return value, put Function Call in Print Statement.

# # Assign Variable
# my_name = greeting('Dana')
# print(my_name)


'''Modify a Parameter'''
# def double_me(value):
#     result = value * 2
#     print(result)

# num = 10
# double_me(num)


# def double_me(value):
#     result = value * 2
#     print(f'{value} doubled is {result}')

# double_me(10)


'''
Exercise
Write a function that will loop through a string and print whether a character is or is not a vowel.
'''
# def vowel_or_not(word):
#     vowel = 'aeiou'
#     for w in word:
#         if w in vowel:
#             print(f'{w} is a Vowel')
#         else:
#             print(f'{w} is not a Vowel')
    
# test_string = 'Hollywood' 
# vowel_or_not(test_string)


'''
Example

Write a function that returns the surface area of a box (rectangular prism).
Surface Area = width*2 + length*2 + height*2
'''
# # Result for this Data is 94
# width = 5
# length = 3
# height = 4

# def surface_area(w, l, h):
#     return 2 * ((w*l) + (h*l) + (h*w))

# print(surface_area(width, length, height))


'''
Exercise
Write a function that returns the surface area of a sphere.
Surface Area = 4 * pi * radius^2
'''
# def surface_area_sphere(radius):
#     return 4 * math.pi * (radius**2)

# print(surface_area_sphere(4))


'''Lets follow these functions through line by line and analyse the return statements'''
# def get_vowels(word):
#     out = ''
#     vowels = 'aeiou'
#     for w in word:
#         if w in vowels:
#             out += w
    
#     return out

# my_word = 'bananas'

# # get_vowels(my_word)  # It should return none
# # print(get_vowels(my_word))  # This will print the return

# # Return is none
# def print_vowels(word):
#     out = ''
#     vowels = 'aeiou'
#     for w in word:
#         if w in vowels:
#             out += w
    
#     print(out)

# my_word = 'bananas'

# # print_vowels(my_word)
# # print(print_vowels(my_word))  # Return None

# # result = print_vowels(my_word)  # Result = None instead of Out Value, Can break Code
# # print(result)


'''
Exercise
Write a function that takes a list and a value, and removes the value until it no longer exists in the list.
Return how many times the value was removed.
'''
# sample_list = [4,5,3,2,4,3,3,3,3,2,2,1,1,1,1,0,5]
# value = 5

# def val_count(my_list, my_value):  # Function Definition and Name
#      counter = 0
#      while my_value in my_list:
#         my_list.remove(my_value)
#         counter += 1
#      return counter

# result = val_count(sample_list, value)  # Invoking Function, Assigning to Varible
# print(result)


'''
Suppose you work for a bank, 
and you have a list of transactions with the following information for each one: 
customer ID, transaction amount, and transaction type (deposit or withdrawal).
Write a function that takes in the list of customer transactions 
and returns a dictionary where the keys are the customer IDs and the values are the total transaction amounts for each customer.
Example:
transactions = [{'id': 'a', 'amount': 500, 'type': 'deposit'},\
                {'id': 'b', 'amount': 350, 'type': 'deposit'},\
                {'id': 'a', 'amount': 450, 'type': 'withdrawal'}]
     Output: {'a': 50, 'b': 350}
'''
transactions = [{'id': 'a', 'amount': 500, 'type': 'deposit'},\
                {'id': 'b', 'amount': 350, 'type': 'deposit'},\
                {'id': 'a', 'amount': 450, 'type': 'withdrawal'},\
                {'id': 'c', 'amount': 545, 'type': 'deposit'},\
                {'id': 'c', 'amount': 225, 'type': 'withdrawal'},\
                {'id': 'b', 'amount': 45, 'type': 'withdrawal'},\
                {'id': 'e', 'amount': 150, 'type': 'deposit'}]

# def transaction_logs(transaction_data):
#      output = {}
#      for t in transaction_data:
#         # If ID doesn't exist yet, Add it to Output Dictionary.
#           if t['id'] not in output.keys():
#                if t['type'] == 'deposit':  # Checking for Deposits
#                 output[t['id']] = t['amount']  # Add Deposit Amount to ID Key
#           else:
#                 # Otherwise, it exists. Check for Withdrawal or Deposit.
#                if t['type'] == 'withdrawal':
#                      output[t['id']] -= t['amount']
#                else:
#                      output[t['id']] += t['amount']
#      return output

# print(transaction_logs(transactions))  # Function Call with List of Dictionaries


'''Create a python file called name_module.py. 
Inside this python file, you will create 3 functions. 
One called full_name, another called reverse_name, and a third called get_initials. 
Each function will take 2 strings. 
One string will be the first name, the second string will be the last name. 
full_name will concatenate and return the full name. 
For example if the first string is "Joseph" and the second string is "Simpson" This function will return the string, "Joseph Simpson". 
Reverse name will flip the name around. 
The name Diana Prince, would come back as Prince Diana. 
The third function will take the first and last name and return the initials. 
The name Tony Stark will return T.S. 
Now create a second python file, called name.py. 
Import the module you just created 
and call the function with the necessary arguments so it prints a full names, reverse names, and initials as needed in the terminal'''
# Solution is in Assignment 4 Folder