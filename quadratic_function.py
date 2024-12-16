#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 23:34:08 2024

@author: ozgur
"""
# from math import sqrt

def solve_quadratic(a,b,c): 
    " this function solves quadratic function"
    delta = ((b**2)-(4*a*c)) ** (1/2)
    x1 =  (-b + delta) / (2*a)
    x2 =  (-b - delta) / (2*a)
    return(x1,x2)


print(solve_quadratic(2,6,4))