'''
1. Now, create a second python file, called name.py. 
2. Import the module you just created.
3. Call the function with the necessary arguments so it prints a full names, reverse names, and initials as needed in the terminal.
'''
import name_module

first_name = 'Seth'
last_name = 'Nightroad'

print(f'Full Name is {name_module.full_name(first_name, last_name)}.')
print(f'Reverse Name is {name_module.reverse_name(first_name, last_name)}.')
print(f'The Initials of the Name is {name_module.get_initials(first_name, last_name)}')