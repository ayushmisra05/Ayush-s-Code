#########################################
# Name: Ayush Misra
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
# CS 115 Lab 2
#########################################
def dot(L, K):
    """
A python function that
returns the dot product
of two lists of same
length. If the two lists
are not the same length,
then what is returned
is the numbers multiplied of
same index until there
aren't any left.
"""
    if not K:
        return 0
    if not L:
        return 0
    else:
        return L[0]*K[0] + dot(L[1:], K[1:])

def explode(S):
    """
A python function that
returns the indecies of a
string as a list]
"""
    if S == "":
        return []
    return [S[0]] + explode(S[1:])

def ind(e, L):
    """
This is a python function
that finds where an element
'e' occurs in a list starting
from 0.
"""
    if not L:
        return 0
    if e == L[0]:
        return 0
    return ind(e, L[1:]) + 1

def removeAll(e, L):
    """
A python function that removes
an element 'e' from a list.
"""
    if L == []:
        return []
    if e == L[0]:
        return removeAll(e, L[1:])
    else:
        return [L[0]] + removeAll(e, L[1:])


def myFilter(a, b):
    """
A python funcion that
does the same things as
'filter' without using
the built-in function
'filter.'
"""
    if b == []:
        return []
    if a(b[0]) == True:
        return [b[0]] + myFilter(a, b[1:])
    else:
        return myFilter(a, b[1:])

def deepReverse(L):
    """
A python function that
reverses a list and works
if there is a list inside
of a list.
"""
    if L == []:
        return []
    if isinstance(L[0], list):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    return deepReverse(L[1:]) + [L[0]]

    





