'''
Created on October 8th, 2023
@author: Ayush Misra
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Hw 3
'''

from functools import reduce
# Be sure to submit hw3.py. Remove the '_template' from the file name.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def giveChange(capacity, coins):
    """
    A python function that returns the amount of coins used and list of coins
    used in order to return the change when a user inputs the change required
    and list of coins of any currency. For example, calling
    giveChange(48, [1,5,10,25,50]) would output (6, [25,10,10,1,1,1])
    """
    if capacity <= 0:
        return [0, []]
    if coins == []:
        return [float('inf'),[]]
    elif coins[0] > capacity:
        return giveChange(capacity, coins[1:])
    else:
        use_it = giveChange(capacity - coins[0], coins)
        lose_it = giveChange(capacity, coins[1:])
        if use_it[0] < lose_it[0]:
            use_it[0] += 1
            use_it[1] += [coins[0]]
            return use_it
        else:
            return lose_it


# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
[ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]
Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
'spam', 'spammy', 'zzyzva']
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
     
#HELPER FUNCTIONS FROM HW2:
def letterScore(letter, scores):
    """
    A python function that returns the score of the letter you provide.
    """
    if letter == "":
        return 0
    if letter == scores[0][0]:
        return scores[0][1]
    else:
        return letterScore(letter, scores[1:])

def addition(x,y):
    """
    A python helper function that adds two numbers.
    """
    return x+y

def wordScore(S, scores):
    """
    A python function that returns the score of a word provided. For example, the word 'spam' has a score of 8
    because the scores that correspond to the letters making the word all add up to 8.
    """
    if scores == []:
        return 0 
    if S == "":
        return 0
    im_gonna_kms = map(lambda x: letterScore(x, scores), S)
    return reduce(addition, im_gonna_kms)

#ACTUAL FUNCTION:
def wordsWithScore(dct, scores):
    '''
    List of words in dct, with their Scrabble score.
    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
     [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    if scores == [] or dct == []:
        return []
    firstWord = dct[0]
    scoreOfWord = map(lambda n: wordScore(n, scores), [firstWord])
    return [[firstWord, reduce(addition, scoreOfWord)]] + wordsWithScore(dct[1:], scores)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''
    if L == []:
        return []
    if n <= 0:
        return []
    else:
        return [L[0]] + take(n-1, L[1:])
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
    if L == []:
        return []
    if n <= 0:
        return L
    else:
        return drop(n-1, L[1:])



