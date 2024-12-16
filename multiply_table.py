# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Fri Nov 29 22:23:02 2024

# @author: ozgur
# """
# from enum import Enum
# from datetime import date
# import sys
# from pathlib import Path 

# class Weekdays(Enum) :
#     MONDAY = 1 
#     TUESDAY = 2 
#     WEDNESDAY = 3
#     THURSDAY = 4
#     FRIDAY = 5 
#     SATURDAY = 6 
#     SUNDAY = 7 
#     @classmethod
#     def from_date(cls, date):
#         return cls(date.isoweekday())

# # for i in range(1,8): 
# #     print(Weekdays(i))

# # a  = Weekdays.from_date(date.today())  
# # print(a)

# b = list(Weekdays)
# # print(b)

# L = iter(b)

# # testList = list(None for i in range(1,100))
# testList = list()
# # print(testList)
# for i in range(1,100): 
#     testList.append(i) 


# c = iter(testList)

# target_path = Path("data")/"extra_detail.log"
# with target_path.open('w') as target_file: 
#     print(c, file=target_file)
#     print(testList, file=target_file)

def mult_table(): 
    "This function prints multiply table until 10"
    for i in range(10) : 
        i += 1 
        print()
        for j in range(10): 
            j += 1 
            print('{:>3}'.format(i*j), end=' ')
        
mult_table()
print()
print("The docstring is:", mult_table.__doc__)
print(help(mult_table))







