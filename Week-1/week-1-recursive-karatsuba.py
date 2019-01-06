#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 23:48:37 2019

@author: jameswang
"""

"""
Instructions:

In this programming assignment you will implement one or more of the integer multiplication algorithms described in 
lecture.

To get the most out of this assignment, your program should restrict itself to multiplying only pairs of single-digit 
numbers. You can implement the grade-school algorithm if you want, but to get the most out of the assignment you'll 
want to implement recursive integer multiplication and/or Karatsuba's algorithm.

So: what's the product of the following two 64-digit numbers?

3141592653589793238462643383279502884197169399375105820974944592

2718281828459045235360287471352662497757247093699959574966967627

[TIP: before submitting, first test the correctness of your program on some small test cases of your own devising. 
Then post your best test cases to the discussion forums to help your fellow students!]

[Food for thought: the number of digits in each input number is a power of 2. Does this make your life easier? 
Does it depend on which algorithm you're implementing?]
"""

import sys
sys.setrecursionlimit(2000)

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

def recursive_karatsuba(a, b):

    a_str = str(a)
    b_str = str(b)
    base = 10 ** (max(len(a_str), len(b_str)) - 1)
    
    a1 = a // base
    a2 = a % base
    b1 = b // base
    b2 = b % base
    
    #print('a,b: ', a,b)
    #print('base: ', base)
    #print('a1,b1,a2,b2: ', a1,b1,a2,b2)
    #print('\n')
    
    res_inner = 0
    
    if (a2 != 0) and (b2 != 0):
        res_inner = recursive_karatsuba(a2, b2)
        
    res1 = a1 * b1
    res3 = res_inner
    res2 = (((a1 + a2) * (b1 + b2)) - res1 - res3)
    
    res = (res1 * base**2) + (res2 * base**1) + (res3 * base**0)
    
    return res

res = recursive_karatsuba(x, y)
assert recursive_karatsuba(x, y) == x*y
print(res)
