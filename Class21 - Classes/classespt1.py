from datetime import datetime
import datetime

'''
Classes
'''
## Class Definition and Initializer
class point2d:
    # Initializer
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # String Representation  # Let’s add a __str__ method to our Point2D class so we can print Point2D objects.
    def __str__(self):
        return f'{self.x}, {self.y}'
    
    # Add an Object to another Object in your Class  # Lets add __add__ to add objects of the same class together
    def __add__(self, other):
        return point2d(self.x + other.x, self.y + other.y)
    
    # Subtraction  # Lets try __sub__ to add objects of the same class together
    def __sub__(self, other):
        return point2d(self.x - other.x, self.y - other.y)
    
    # Test Equality between objects  # Let's try __eq__ method to test equality
    '''
    What is the output of this code if we don't override ==?
    What is the output if we override == to use value equality?
    Is it the same or different? Why?

    Without the __eq__ method, we will only be able to test if it is the same object
    '''
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False
    
    # Less Than  # Let's try __lt__ method to test less than
    def __lt__(self, other):
        if self.x < other.x and self.y < other.y:
            return True
        return False
    
    # Mutator Method - Setter  # Setting with mutator methods
    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    # Accessor Method  # Getting with accessor methods
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

# Creating an object of the Point2d Class
point1 = point2d(4, 10)
point2 = point2d(8, 15)
        
# # Return a string representation of this object
# print(point1)
# print(point2)
    
# # Adds this object to another object from the same class, return a new object.
# print(point1 + point2)
    
# # Subtracts another object from this object, return a new object.
# print(point1 - point2)

# Test equality between this object and another, return a boolean.
point3 = point2d(3, 4)
point4 = point2d(3, 4)   
# print(point3 == point4)

# Less Than
point5 = point2d(10, 12)
point6 = point2d(13, 15)
# print(point5 < point6)

# Mutator Method
point7 = point2d(5, 11)
point7.set_x(10)  # Our Method will change the value of x
# print(point7)

point7.set_y(25)
# print(point7)

# # Accessor Method
# print(point7.get_x())
# print(point7.get_y())


'''
Exercise - Dog Class
This Class will have 3 Parameters: Dog Name, Dog Breed, and Age in Human years
'''
# class Dog:
#     def __init__(self, name, birth_year, breed):
#         self.name = name
#         self.birth_year = birth_year
#         self.breed = breed

#     def __str__(self):
#         return f'{self.name} is a {self.breed} born in {self.birth_year}'
    
#     def human_age(self):
#         today = datetime.datetime.now()
#         year = today.year
#         return f'{self.name} is {year - self.birth_year} years old in Human years.'
    
#     # Write a method that will calculate dog years
#     def dog_years(self):
#         today = datetime.datetime.now()
#         year = today.year
#         return f'{self.name} is {(year - self.birth_year) * 7}​​ years old in Dog years'

# dog1 = Dog('Fido', 2020, 'Golden Retriever')  # Creates our first Object of the Dog Class
# dog2 = Dog('Zuzu', 2021, 'Dachsund')
# dog3 = Dog('Stella', 2016, 'Japanese Chin')

# String Representation
# print(dog1)
# print(dog2)
# print(dog3)

# Human Age
# print(dog1.human_age())
# print(dog2.human_age())
# print(dog3.human_age())

# Dog Age
# print(dog1.dog_years())
# print(dog2.dog_years())
# print(dog3.dog_years())

'''Other Version of Dog Class'''
# class Dog:
   
#     def __init__(self, name, birth_year, breed):
#         self.name = name
#         self.birth_year = birth_year
#         self.breed = breed
 
   
#     def __str__(self):
#         return f'{self.name} is a {self.breed} and was born in {self.birth_year}'
   
#     def human_age(self):
#         today = datetime.datetime.now()
#         year = today.year
#         return year - self.birth_year
   
#     def dog_years(self):
#         dog_years = 7 * self.human_age()
#         return f'{self.name} is {dog_years} in dog years'
    
# dog1 = Dog('Fido', 2020, 'Golden Retriever')  # Creates our first Object of the Dog Class
# dog2 = Dog('Zuzu', 2021, 'Dachsund')
# dog3 = Dog('Stella', 2016, 'Japanese Chin')
    
# # String Representation
# print(dog1)
# print(dog2)
# print(dog3)

# # Human Age
# print(dog1.human_age())
# print(dog2.human_age())
# print(dog3.human_age())
# # Dog Age
# print(dog1.dog_years())
# print(dog2.dog_years())
# print(dog3.dog_years())


'''Exercise - Date Class'''