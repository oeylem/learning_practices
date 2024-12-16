# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Fri Nov 29 22:23:02 2024

# @author: ozgur
# """



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







