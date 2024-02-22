''' This program calculates the perimeter of a triangle

Requirements
    - Comment your code 
        +5
    - Assign meaningful variable names 
        +5
    - Output a print statement, "The perimeter of your triangle is..." 
        +5
    - The test case for your program is side # 1 is 5, the base is 6, side # 2 is 10 
        +5
    - Output a print statement, "Is side 1 greater than side 2?" 
        +5
    - Output a print statement, "Is the base equal to side 1?"
        +5
'''

#Formula for the Perimeter of a Triangle
#Perimeter = Side1 + Base + Side2

side1 = 5
base = 6
side2 = 10

perimeter = side1 + base + side2

print('The Perimeter of your Triangle is', perimeter)

print('Is Side # 1 greater than Side # 2?', side1 > side2)

print('Is the Base equal to Side # 1?', base == side1)