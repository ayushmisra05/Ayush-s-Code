############################################################
# Name: Ayush Misra
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS115 Lab 1
#
############################################################
from math import factorial
from functools import reduce

"""
This python function takes
the inverse of a number, or
its reciprocal
"""
def inverse(x):
    answer = float(1/x)
    return answer

"""
This Python function
takes the sum of two
given numbers
"""
def add(x, y):
    return x + y
"""
This python function takes
the sum of the taylor series
"e" given "n"
"""
def e(n):
    list1 = list(range(0,n+1))
    list2 = list(map(factorial, list1))
    list3 = list(map(inverse, list2))
    return reduce(add, list3)
    



    
