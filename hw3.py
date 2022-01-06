'''
Created on 2/15/20
@author: Claudia MacRae
Pledge: I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 3
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def length(L):
    '''returns length of list L'''
    if L == []: return 0
    return 1 + length(L[1:])

def giveChange(amount, coins):
    '''Given a target amount, and a list of available coins,
    return the lowest count of coins that can be used to make the amount'''
    if coins == [] and amount != 0:
        return float("inf")
    CL = (subsetList(amount, coins))
    return [ length(CL), CL]


def subsetList(target, L):
    '''Assuming L is a list of positive integers and target is a
    non-negative integer, return a list of elements that would produce the largest
    sum of elements of L that does not exceed target.'''
    if L == []:
        return []
    if L[0] > target:
        return subsetList(target, L[1:])
    else:
        use = [L[0]] + subsetList(target - L[0], L)
        lose = subsetList(target, L[1:])
        if sum(use) == sum(lose):
            if length(use) > length(lose): return lose
            return use
        elif sum(use) > sum(lose):
            return use
        else:
            return lose

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
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    if(dct == []):
        return []
    return [[dct[0], wordScore(dct[0], scores)]] + wordsWithScore(dct[1:], scores)

def letterScore(letter, scoreList):
    '''returns score for given letter'''
    if(letter == scoreList[0][0]):
        return scoreList[0][1]
    return letterScore(letter, scoreList[1:])

def wordScore(s, scoreList):
    '''returns total score for given string'''
    if(s == ''):
        return 0
    return letterScore(s[0], scoreList) + wordScore(s[1:], scoreList)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    if n == 0 or L == []:
        return []
    return [L[0]] + take(n-1, L[1:])



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if n == 0:
        return L
    return drop(n-1, L[1:])

