'''
Created on 10/19/2023
@author:   Ayush Misra
Pledge:    I Pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n % 2 == 0:
        return False
    return True

# 42 in base 2 would be 1(2^5) + 0(2^4) + 1(2^3) + 0(2^2) + 1(2^1) + 0(2^0), which is 101010
'''
An odd base-10 integer will always have 1 in the rightmost bit of a binary
representation, also referred to as the least-significant bit (LSB). This
is because, when written in binary, odd integers in base-10 always have
their least significant bit set to 1. Since even base-10 numbers have their
least significant bit set to 0 in binary, the LSB of an even base-10 integer
in its base-2 equivalent will be 0.
'''

'''
A base-2 integer is divided by two when the least-significant bit, or the
rightmost digit, is removed. This process is essentially a binary right-shift
operation. This indicates that the initial number has been halved in value.
This means that if we take the 0 out of the end of 1010, we obtain 101, which
is half of the initial number. In a similar vein, if we take the 1 at the right
out of 1011 in the beginning, we get 101, which is likewise half of the initial number.
'''

'''
By adding a "0" to the right of Y's binary, we can quickly determine the base-2 equivalent
of N if we know the base-2 version of Y, which is N/2 (rounded down). The reason for this
is that in base-2, dividing an even integer by 2 results in a shift of all its binary numbers
one place to the right, adding a "0" at the final digit.
'''



def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif isOdd(n):
        return numToBinary(n//2) + '1'
    else:
        return numToBinary(n//2) + '0'
    
#11 in base 2 is 1011

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    if s[0] == '0':
        return binaryToNum(s[1:])
    else:
        return binaryToNum(s[1:]) + 2**(len(s) - 1)
    

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.''' 
    biToNumber = binaryToNum(s) + 1
    goBack = numToBinary(biToNumber)
    answer = '0'*(8 - len(goBack)) + goBack
    return answer[-8:]

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print(s)
    if n == 0:
        return None
    else:
        return count(increment(s), n-1)
        

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif n % 3 == 2:
        return numToTernary(n//3) + '2'
    elif n % 3 == 1:
        return numToTernary(n//3) + '1'
    elif n % 3 == 0:
        return numToTernary(n//3) + '0'

# The number 59 in base 3 (ternary): 59 = 2 * 3^4 + 0 * 3^3 + 1 * 3^2 + 2 * 3^1 + 1 * 3^0 which is '20121'

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    return 3*ternaryToNum(s[:-1]) + int(s[-1])
   


