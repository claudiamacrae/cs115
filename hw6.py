'''
Created on 3/11/20
@author:  Claudia MacRae, Brendan Probst
Pledge:  I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.


s1 = '01'*32
s2 = '0'*32 + '1'*32
s3 = '1'*16 + '0'*16 + '1'*16 + '0'*16
s4 = '10'*32

def show(S):
    '''shows the string in 8x8 grid'''
    assert len(S) == 64
    for i in range(8): print(S[8*i : 8*i+8])

def compression(S):
    '''the compresssion ratio of S'''
    return len(compress(S))/len(S)
    
def compress(S):
    '''takes an input of a string of 64-bits (8x8 grid) with 0 representing black
    and 1 representing 1. Compresses the string into its run length sequnce
    where each compressed block size is 5 bits, and the first compressed block
    refers the to number of 0's'''
    def comp(S,b):
        if S == '':
            return ''
        num = prefix(b, S)
        if num > MAX_RUN_LENGTH:
            return numToBinaryByte(MAX_RUN_LENGTH) + '0'*COMPRESSED_BLOCK_SIZE + comp(S[MAX_RUN_LENGTH:], b)
        return numToBinaryByte(num) + comp(S[num:], opp(b))
    return comp(S,0)
        
def uncompress(s):
    '''given a compressed string, will return a string of 64 bits representing an 8x8 black and white grid'''
    def uncomp(s, b):
        if s == '':
            return ''
        byte = s[:COMPRESSED_BLOCK_SIZE]
        binary = byte[prefix(0, byte):] #trim leading 0s
        return bitToChar(b)*binaryToNum(binary) + uncomp(s[COMPRESSED_BLOCK_SIZE:], opp(b))
    return uncomp(s, 0)

def opp(n):
    '''given n is 1 or 0, will return the alternate bit'''
    assert n == 0 or n == 1
    if n == 1:
        return 0
    return 1

def prefix(b, s):
    '''assuming b is an integer 0 or 1, how many of character b does S have at the beginning'''
    if s == '':
        return 0
    elif s[0] == bitToChar(b):
         return 1 + prefix(b, s[1:])
    else:
        return 0

def bitToChar(b):
    '''assuming b is integer 0 or 1, return it as a character'''
    return chr(b + ord('0'))


def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.nu
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    return numToBinary(n//2) + bitToChar(n%2)


def numToBinaryByte(n):
    '''returns the binary number with the length == COMPRESSED_BLOCK_SIZE'''
    num = numToBinary(n)
    k = (COMPRESSED_BLOCK_SIZE - len(num))
    return '0'*k + num

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '': return 0
    if s[-1] == '0':
        return 2*binaryToNum(s[:-1])
    else:
        return 1 + 2*binaryToNum(s[:-1])
'''
assert uncompress(compress(s1)) == s1
assert uncompress(compress(s2)) == s2
assert uncompress(compress(s3)) == s3
'''
