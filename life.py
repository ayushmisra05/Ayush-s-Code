'''
Name: Ayush Misra
Pledge: I pledge my honor that I have abided by the Stevens Honor System
CS 115 Lab 10
'''

import sys
import random

def createOneRow(width):
    """ returns one row of zeros of width "width"...
    You might use this in your createBoard(width, height) function.
    """
    row = []
    for col in range(width):
        row += [0]
    return row


def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)] # What do you need to add a whole row here?
    return A



def printBoard( A ):
    """ this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )


def diagonalize(width, height):
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells.
    """
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A


def innerCells(w, h):
    """ makes every inner number 1 and leaves edges as 0.
    if the list starts or ends with 1, the entire list becomes 0.
    """
    newList = []
    for lst in diagonalize(w,h):
        if lst[0] == 1 or lst[-1] == 1:
            newList += [createOneRow(w)]
        else:
            lst[1:-1] = [1]*(len(lst) - 2)
            newList += [lst]
    return newList


def randomCells(w, h):
    """Creats a board of width and height and randomizes the inner
cells to become either 0s or 1s"""
    newList = createBoard(w, h)
    for row in range(1,(h - 1)):
        for col in range(1, (w - 1)):
                newList[row][col] = random.choice([0,1])
    return newList

def copy(A):
    """Makes a deep copy of A"""
    newA = createBoard(len(A), len(A[0]))
    for row in range(len(A)):
        for col in range(len(A[0])):
            newA[row][col] = A[row][col]
    return newA

def innerReverse(A):
    """ takes an old 2d array (or "generation") and then
creates a new generation of the same shape and size and
changes 0s to 1s and vice versa"""
    reversed_board = copy(A)
    for row in range(1, len(A) - 1):
        for col in range(1, len(A[0]) - 1):
            if reversed_board[row][col] == 0:
                reversed_board[row][col] = 1
            else:
                reversed_board[row][col] = 0
    return reversed_board


def countNeighbors(row, col, A):
    """Counts the ammount of 1s and 0s and adds them up near an area."""
    bottom = A[row-1][col-1] + A[row-1][col] + A[row-1][col+1]
    mid = A[row][col-1] + A[row][col+1]
    top = A[row+1][col-1] + A[row+1][col]+ A[row+1][col+1]
    return bottom + mid + top

def next_life_generation(A):
    '''The Game of Life. Rules on the Script'''
    newA = copy(A)
    for row in range(1, len(A) - 1):
        for col in range(1, len(A[0]) -1):
            if countNeighbors(row, col, A) < 2:
                newA[row][col] = 0
            elif countNeighbors(row, col, A) > 3:
                newA[row][col] = 0
            elif countNeighbors(row, col, A) == 3:
                newA[row][col] = 1
    return newA
