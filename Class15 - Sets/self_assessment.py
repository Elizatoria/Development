'''
Self-assessment
1. Print Hello World
2. Assign my first name to a variable and print
3. Write a for loop to loop through
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
4. Write a while loop to count from 1 to 75
5. Use a While true loop that prompts you for 2 numbers, it will add the 2 numbers and print the result than stop
6. Using range function, count from 5 to 50
7. Use a string method to change WEDNESDAY to wednesday
8. Take input from the user and using an if statement, let the user know if the value they entered is a letter or a number
9. Take a word from the user and let them know how many vowels are in the word
10. Remove the duplicates from a list with values [4, 4, 4, 3, 2, 1, 4, 9]
'''
# # 1. Print Hello World
# print('Hello World')


# # 2. Assign my first name to a variable and print
# first_name = 'Victoria'
# print(first_name)


# # 3. Write a for loop to loop through
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for m in my_list:
#     print(m)


# # 4. Write a while loop to count from 1 to 75
# start = 1
# end = 75

# while start <= end:
#     print(start)
#     start += 1


# # 5. Use a While true loop that prompts you for 2 numbers, it will add the 2 numbers and print the result than stop
# while True:
#     num1 = int(input('Enter an Integer: '))
#     num2 = int(input('Enter anoter Integer: '))
#     sum = num1 + num2
#     print(sum)
#     break


# # 6. Using range function, count from 5 to 50
# for r in range(5, 51):
#     print(r)


# # 7. Use a string method to change WEDNESDAY to wednesday
# day = 'WEDNESDAY'
# print(day.lower())


# # 8. Take input from the user and using an if statement, let the user know if the value they entered is a letter or a number
# user_input = input('Enter your input: ')

# if user_input.isalpha():
#     print(f'{user_input} is a Letter.')
# elif user_input.isdigit():
#     print(f'{user_input} is a Number.')


# # 9. Take a word from the user and let them know how many vowels are in the word
# is_a_vowel = input('Put in your Word: ')
# counter = 0

# for v in is_a_vowel:
#     if v in 'aeiou':
#         counter += 1
# print(counter)


# # 10. Remove the duplicates from a list with values [4, 4, 4, 3, 2, 1, 4, 9]
# my_list = [4, 4, 4, 3, 2, 1, 4, 9]
# my_list = set(my_list)
# print(my_list)