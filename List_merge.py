#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 22:57:21 2024

@author: ozgur
"""
lFirst = [1,11,2,3]
lSecond = [4,5,6,7, -5]
#lMerged= []

def merge(*l1, **l2):
    "this function merges 2 lists"
    l3 = []
    for x in l1: 
        l3.append(x)
    for y in l2: 
        l3.append(y)
    return l3 

lMerged = merge(*lFirst, *lSecond)
print(lMerged)

lMerged.sort()
print(lMerged)

lMerged2 = lMerged.copy()
lMerged2.sort(reverse=True)
print(lMerged2)

print(len(lFirst))
print(len(lSecond))
print(len(lMerged))