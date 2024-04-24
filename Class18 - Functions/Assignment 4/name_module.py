'''
1. Create a python file called name_module.py. 
2. Inside this python file, you will create 3 functions. 
3. One called full_name, another called reverse_name, and a third called get_initials. 
4. Each function will take 2 strings. 
5. One string will be the first name, the second string will be the last name. 
6. full_name will concatenate and return the full name. 
Example: If the first string is "Joseph" and the second string is "Simpson" This function will return the string, "Joseph Simpson". 
7. Reverse name will flip the name around. 
Example: The name Diana Prince, would come back as Prince Diana. 
8. The third function will take the first and last name and return the initials. 
Example: The name Tony Stark will return T.S.
'''

def full_name(first_name, last_name):
    return first_name + ' ' + last_name

def reverse_name(first_name, last_name):
    return last_name + ', ' + first_name

def get_initials(first_name, last_name):
    return first_name[0] + '.' + last_name[0] + '.'