from datetime import datetime

'''Write a program that will take the user's first name, and than, the users last name, 
and print the value to a text file on 2 separate lines'''



'''Write a function called print_even_numbers that will take in a list of integer values, 
and will extract the even numbers from that list and write to a text file let's try different parameters in our open function x, a, w'''
# def find_even_numbers(our_list):
#     output_list = []
#     for m in our_list:
#         if m % 2 == 0:
#             output_list.append(m)
    
#     with open('even_nums.txt', 'w') as output:
#         for o in output_list:
#             o = str(o)
#             output.writelines(o)

#     print('File Printed Successfully')


# my_list = [1,2,3,4,5,6,7,12,14,15,21,22]

# find_even_numbers(my_list)


'''Lets read in the song lyrics and put it into a list, but before we do, lets look at other options we have to read files in'''
with open('23_time_to_say_goodbye.txt', 'r') as lyrics:
    my_paragraph = lyrics.read()  # Will read everything
    my_line = lyrics.readline()  # Will read one line at a time 
    lyric_list = lyrics.readlines()  # Will deliver a list

# print(my_paragraph)
# print(my_line)
# print(lyric_list)


''' 
Bank account class 
Create the bank account class per the specifications in the powerpoint.  
'''
class BankAccount:
    def __init__(self, customer_name: str, acct_num: int, date: str, balance: float):
        self.customer_name = customer_name
        self.acct_name = acct_num
        self.date = date
        self.balance = balance

    def __str__(self):
        return f'Customer Name: {self.customer_name}\nAccount Number: {self.acct_name}\nDate: {self.date}\nBalance: ${self.balance:.02f}'
    
    # Make a Deposit
    def deposit(self, amount):
        self.balance += amount
        print(f'{amount} has been deposited to your account. New Balance: {self.balance}')

ac_no_1 = BankAccount("Toninho Takeo", 2345, "05-05-24", 1000.25 )
ac_no_2 = BankAccount("Jim Jones", 5424, "01-05-22", 1000 )
ac_no_3 = BankAccount("Sally Field", 3242, "11-04-15", 1000 )
ac_no_4 = BankAccount("Burt Reynolds", 4325, "08-11-13", 1000 )

# String Representation
print(ac_no_1)

# Deposit
ac_no_1.deposit(500)