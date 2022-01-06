'''
Created on 2/10/20
@author: Claudia MacRae
Pledge: I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter
from dict import *

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
    
def canBeMade(w, rack):
    '''returns true if string can be made from letters given'''
    if(w == ''):
        return True
    if w[0] in rack:
        return canBeMade(w[1:], removeOne(w[0], rack))
    return False

def removeOne(e, L):
    '''returns a list identical to L, with all instances of e removed'''
    if(L == []):
        return []
    if(e == L[0]):
        return L[1:]
    else:
        return [L[0]] + removeOne(e, L[1:])
    
def myFilter(rack, L):
    '''filters L to only include words able to be made from the rack'''
    if(L == []):
        return []
    if(canBeMade(L[0], rack)):
        return [L[0]] + myFilter(rack, L[1:])
    return myFilter(rack, L[1:])

def scoreList(rack):
    '''given a rack of letters, will return all possible words in dictionary and their respective scores'''
    words = myFilter(rack, Dictionary)
    return addScores(words)

def addScores(L):
    '''given list of words, will return a list of lists of two elements, the word and its scrabble score'''
    if(L == []):
        return []
    return [[L[0], wordScore(L[0], scrabbleScores)]] + addScores(L[1:])

def bestWord(rack):
    '''given a rack of letters, will return the highest scoring word possible and its respective score'''
    L = scoreList(rack)
    index = findBest(L,0)
    if index > -1 : return L[index]
    else: return ['', 0]

def findBest(L, highest):
    '''given list of pairs, where the 0th element is a word and the 1st is its score
    returns index of L with the greastest score'''
    if L == []:
        return -1
    if L[0][1] > highest:
        return 1 + findBest(L[1:], L[0][1])
    else:
        return 1 + findBest(L[1:], highest)



                            
