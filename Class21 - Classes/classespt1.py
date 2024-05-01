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

    # String Representation
    def __str__(self):
        return f'{self.x}, {self.y}'
    
    # Add an Object to another Object in your Class
    def __add__(self, other):
        return point2d(self.x + other.x, self.y + other.y)
    
    # Subtractio
    def __sub__(self, other):
        return point2d(self.x - other.x, self.y - other.y)
    
    # Test Equality between objects
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False
    
    # Less Than
    def __lt__(self, other):
        if self.x < other.x and self.y < other.y:
            return True
        return False

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
    
# Mutator method
point5 = point2d(10, 12)
point6 = point2d(13, 15)
print(point5 < point6)

# Accessor method


# Create a point object with attributes x=2, y=3

# Let’s add a __str__ method to our Point2D class so we can print Point2D objects.


# Lets add __add__ to add objects of the same class together


# Lets try __sub__ to add objects of the same class together

# Let's try __eq__ method to test equality
'''What is the output of this code if we don't override ==?
What is the output if we override == to use value equality?
Is it the same or different? Why?

Without the __eq__ method, we will only be able to test if it is the same object
'''



# Let's try __lt__ method to test less than


# Setting with mutator methods



# Getting with accessor methods





''' Exercise - Date Class '''




 




'''
Exercise - Dog Class
'''






