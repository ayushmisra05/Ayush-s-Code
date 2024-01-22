#################################
# Name: Ayush Misra
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
# Homework 1
#
#################################

from functools import reduce

"""
This python function
multiplies two given
numbers.
"""
def multiplyNumbers(x, y):
    return x*y

"""
This python function
takes the factorial
of the numbers in a
given list.
"""
def factorial(n):
    list1 = list(range(1,n+1))
    return reduce(multiplyNumbers, list1)

"""
This python function
takes the sum of two
given numbers.
"""
def add(a, b):
    return (a + b)

"""
This python function
calculates the mean,
or average of a list
of given numbers.
"""
def mean(L):
    total = reduce(add, L)
    answer = (total/len(L))
    return answer
