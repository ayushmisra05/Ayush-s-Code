'''
Name: Ayush Misra
Pledge: I pledge my Honor that I have abided by the Stevens Honor System
CS 115 HW 4
'''


#Task 1

from functools import reduce

def pascal_row(n):
    ''' A python function that calculates the nth row
in pascals triangle. '''
    if n == 0:
        return [1]
    prev_row = pascal_row(n-1)
    new_row = [1] + sumList(prev_row) + [1]
    return new_row
    
#my helper function
def sumList(L):
    '''A helper function used to sum the first two numbers of a list
in order to output those numbers between [1] and [1] on each side.
'''
    if not L:
        return 0
    if len(L) == 1:
        return []
    else:
        return [reduce(lambda x, y: x + y, L[0:2])] + sumList(L[1:])


#Task 2
def pascal_triangle(n):
    '''A function that takes a non-zero integer n and returns
pascals triangles rows including the nth row starting from [[1]].
'''
    if n == 0:
       return [[1]]
    else:
        putting_it_in_a_list = pascal_row(n-1)
        triangle = pascal_triangle(n-1) + [putting_it_in_a_list[::-1]] + [pascal_row(n)]
        return removeAll(triangle)
    
#helper function
def removeAll(L):
    '''A helper function used for pascal_triangle to remove
any repeats in the pascal triangle list.
'''
    if not L:
        return []  
    if len(L) == 1:
        return L 
    if L[0] == L[1]:
        return [L[0]] + removeAll(L[2:])
    else:
        return [L[0]] + removeAll(L[1:])

#Task 3
def test_pascal_row():
    ''' This function takes no arguments. This function
checks to see if the pascal_row function was designed correctly
by using the assert function. It will throw an assertion error
if the code is incorrect.
'''
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1, 1]
    #DON'T HIT DOWN KEY HERE YOU'LL REGRET IT ;)
    assert pascal_row(69) == [1, 69, 2346, 52394, 864501, 11238513, 119877472, 1078897248, 8361453672, 56672074888, 340032449328, 1823810410032, 8815083648488, 38650751381832, 154603005527328, 566877686933536, 1913212193400684, 5964720367660956, 17231414395464984, 46252743903616536, 115631859759041340, 269807672771096460, 588671286046028640, 1202936975833188960, 2305629203680278840, 4150132566624501912, 7023301266595310928, 11185257572725865552, 16777886359088798328, 23720460024918645912, 31627280033224861216, 39789158751476438304, 47249626017378270486, 52976853413424121454, 56093138908331422716, 56093138908331422716, 52976853413424121454, 47249626017378270486, 39789158751476438304, 31627280033224861216, 23720460024918645912, 16777886359088798328, 11185257572725865552, 7023301266595310928, 4150132566624501912, 2305629203680278840, 1202936975833188960, 588671286046028640, 269807672771096460, 115631859759041340, 46252743903616536, 17231414395464984, 5964720367660956, 1913212193400684, 566877686933536, 154603005527328, 38650751381832, 8815083648488, 1823810410032, 340032449328, 56672074888, 8361453672, 1078897248, 119877472, 11238513, 864501, 52394, 2346, 69, 1]
    assert pascal_row(7) == [1, 7, 21, 35, 35, 21, 7, 1]

def test_pascal_triangle():
     ''' This function takes no arguments. This function
checks to see if the pascal_triangle function was designed correctly
by using the assert function. It will throw an assertion error
if the code is incorrect.
'''
    assert pascal_triangle(0) == [[1]]
    #code test too:
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    assert pascal_triangle(8) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1]]
