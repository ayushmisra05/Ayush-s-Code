
'''
Created on 11/4/2023
@author:   Liam Thomas and Ayush Misra
Pledge:    We pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    if n%2 == 1:          
        return numToBinary(n//2) + '1'
    else:
        return numToBinary(n//2) + '0'

def length(a):
    '''
    inputting an int, return that int with however many 0s before it to make it length 5
    '''
    return '0'*(COMPRESSED_BLOCK_SIZE-len(a)) + a


def helper(s, q = 0, total = 0):
    '''
    inputting a binary string, 
    return the of the consecutive number of 0s up to MAX_RUN_LENGTH-1 as a element a string,
    then the number of consecutive 1s then back and forth
    '''
    if not s:
        return [total]
    if total == MAX_RUN_LENGTH:
        return [total] + helper(s, (q+1)%2, 0)
    if s[0] == str(q):
        return helper(s[1:], q, total+1)
    else:
        return [total] + helper(s, (q+1)%2, 0)

def asd(s):
    '''
    returns string version of list
    '''
    if not s:
        return ''
    return s[0] + asd(s[1:])

def compress(s, q = 0, total = 0):
    '''
    modifies helper to convert a list of integers of base to to a string of base 2
    '''
    return asd(list(map(length,list(map(numToBinary, helper(s))))))


def lamb(s):
    '''
    returns a strong in segments of length 5 in a list
    '''
    if not s:
        return []
    return [s[0:COMPRESSED_BLOCK_SIZE]] + lamb(s[COMPRESSED_BLOCK_SIZE:])

def binaryToNum(s, a = 0):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if not s:
        return 0
    else:
        return (2**a) * int(s[-1]) + binaryToNum(s[0:-1], a + 1)


def uncompress(s, q = 0):
    '''
    inputting the output of copmress, a series of 5 bit representation of the number of 0s, then 1s, then 0s...
    return the origional binary string it represents
    '''
    if not s:
        return ''
    return str(q) * binaryToNum(s[0:COMPRESSED_BLOCK_SIZE]) + uncompress(s[COMPRESSED_BLOCK_SIZE:], (q+1)%2)




def compression(s):
    '''
    return how much smaller or larger the copmressed version of binary is than the 
    uncompressed/origional binary representation
    '''
    return (len(compress(s))/len(s))




