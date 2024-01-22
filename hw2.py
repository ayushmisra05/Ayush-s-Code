'''
Created on 9/28/2023
@author: Ayush Misra (Bryan told me to name my 1st variable)
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Hw 2
'''
import sys
from functools import reduce
# Be sure to submit hw2.py. Remove the '_template' from the file name.
# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)
# Leave the following lists in place.
scrabbleScores = \
[ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]
Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
'spam', 'spammy', 'zzyzva']
# Implement your functions here.
def letterScore(letter, scorelist):
    """
    A python function that returns the score of the letter you provide
    """
    if letter == "":
        return 0
    if letter == scorelist[0][0]:
        return scorelist[0][1]
    else:
        return letterScore(letter, scorelist[1:])


def addition(x,y):
    """
    A python helper function that adds two numbers.
    """
    return x+y


def wordScore(S, scorelist):
    """
    A python function that returns the score of a word provided. For example, the word 'spam' has a score of 8
    because the scores that correspond to the letters making the word all add up to 8.
    """
    if scorelist == []:
        return 0 
    if S == "":
        return 0
    im_gonna_kms = map(lambda x: letterScore(x, scorelist), S)
    return reduce(addition, im_gonna_kms)
    

#Hard Ones: Go to Office Hours
def scrabbleRack(Rack, char):
    """
    A python helper function that checks if the first letter of the word is in the given Rack, either
    returning a 1 or -1. This, in turn, allows the next helper funtion create an actual word from the
    dictionary.
    """
    if char in Rack:
        if Rack[0] == char:
            return 0
        return 1 + scrabbleRack(Rack[1:], char)
    else:
        return -1

def AddWord(Rack, index):
    """
    A python helper function that creates a word when given a rack of letters. From the previous helper
    function, when returned 1 or -1, that value that was returned will tell this function to either keep
    the letter, or move on to the next letter.
    """
    if index == "":
        return True
    elif scrabbleRack(Rack, index[0]) == -1:
        return False
    rack_new = Rack[0:scrabbleRack(Rack, index[0])]
    rack_new = rack_new + Rack[scrabbleRack(Rack, index[0])+1:len(Rack)]
    return AddWord(rack_new, index[1:])


def wordsInDictionary(Rack, i):
    """
    A python helper function that uses the previous function and wordScore to return the list of words from
    the provided dictionary. The words can only be returned if the provided rack includes those letters.
    """
    if (i + 1) > len(Dictionary):
        return []
    elif AddWord(Rack, Dictionary[i]):
        return [[Dictionary[i]] + [wordScore(Dictionary[i], scrabbleScores)]] + wordsInDictionary(Rack, i+1)
    return wordsInDictionary(Rack,i+1)

def scoreList(Rack):
    """
    This python function returns all the possible words that could be made from a given rack and returns their
    scrabble score in list format.
    """
    return wordsInDictionary(Rack, 0)

def largestNumba(o, p):
    """
    A python helper function that checks whether one variable has a higher value.
    """
    if o[1] > p[1]:
        return o
    elif p[1] > o[1]:
        return p
    return o + p

def bestWord(Rack):
    """
    This python function finds the best word to use from a given rack and returns the word and score of the word
    in list format.
    """
    if not scoreList(Rack):
        return ["", 0]
    else:
        return list(reduce(largestNumba, scoreList(Rack)))
