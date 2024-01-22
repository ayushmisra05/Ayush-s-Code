############################################################
# Name: Ayush Misra
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
# CS115 Lab 0
#
############################################################
"""
This is a python program
that detects if the word
provided has the same first
and last letter regardless of
capitalization and character count
"""
def same(word):

    word = word.lower()
    if len(word) == 0:
        return False
    if word[0] == word[len(word) - 1]:
        return True
    else:
        return False

    
"""
This is a python program
that finds the sum between
two numbers. For example,
since the numbers between 4
and 7 and 5 and 6, the sum
of 5 and 6 will be evaluated
to 11.
"""
def consecutiveSum(x, y):

    x = int(x)
    y = int(y)
    i = ((x+y)/2)*(y-x-1) 
    while (x < y):
        return int(i) 
