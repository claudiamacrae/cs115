'''
Created on 3/24/20
@author:  Claudia MacRae
Pledge:  I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 7
'''

def numToBaseB(n, b):
    '''converts base-10 number n to base b, returns string'''
    if n == 0: return '0'
    def toBase(n, b):
        if n == 0: return ''
        return toBase(n//b, b) + str(n%b)
    return toBase(n, b)

def baseBToNum(s, b):
    '''converts string representation of base-b number, s,
    to base 10, returns int'''
    if s == '': return 0
    return int(s[-1]) + b*baseBToNum(s[:-1], b)

def baseToBase(b1, b2, sinb1):
    '''converts string represetnation of base-b1 number, sinb1,
    to base b2'''
    return numToBaseB(baseBToNum(sinb1, b1), b2)

def add(s, t):
    '''adds binary numbers s and t, returns string'''
    return numToBaseB(baseBToNum(s, 2) + baseBToNum(t, 2), 2)

FullAdder = {
    ('0','0','0') : ('0','0'),
    ('0','0','1') : ('1','0'),
    ('0','1','0') : ('1','0'),
    ('0','1','1') : ('0','1'),
    ('1','0','0') : ('1','0'),
    ('1','0','1') : ('0','1'),
    ('1','1','0') : ('0','1'),
    ('1','1','1') : ('1','1')
}

def addB(s, t):
    '''adds binary numbers s and t using full adder dictionary, returns string'''
    def adder(s, t, carryIn):
        if s == '' and t == '' and carryIn == '0' : return ''
        if s == '': s = '0'
        if t == '': t = '0'
        sum, carryOut = FullAdder[(s[-1], t[-1], carryIn)]
        return adder(s[:-1], t[:-1], carryOut) + sum
    return adder(s, t, '0')























    
    
