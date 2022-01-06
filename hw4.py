'''
Created on 2/19/20
@author: Claudia MacRae
Pledge: I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 4
'''

def pascal_add(L):
    '''sums adjacent elements in given list
    returns list of sums'''
    if L == []: return []
    if len(L) == 1: return [1]
    return [L[0] + L[1]] + pascal_add(L[1:])

def pascal_row(n):
    '''returns a list of elements in the nth row of pascal's triangle'''
    if n == 0: return [1]
    return [1] + pascal_add(pascal_row(n-1))

def pascal_triangle(n):
    '''calculates pascal's triangle to the nth row
    returns a list of lists'''
    if n == 0: return [pascal_row(0)]
    return pascal_triangle(n-1) + [pascal_row(n)]

def test_pascal_row():
    '''tests the functionality of pascal_row function'''
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1,1]
    assert pascal_row(5) == [1, 5, 10, 10, 5, 1]

def test_pascal_triangle():
    '''tests the functionality of pascal_triangle function'''
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
