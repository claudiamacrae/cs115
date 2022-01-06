from cs115 import reduce, map

def add(x, y):
    '''returns sum of x and y'''
    return x + y

def mult(x, y):
    '''returns product of x and y'''
    return x * y

def factorial(n):
    '''returns value of n factorial'''
    nums = range(1, n+1)
    return reduce(mult, nums)

def mean(L):
    '''returns mean of list L'''
    s = reduce(add, L)
    return s / len(L)

def divides(n):
    '''returns function div testing divisibility of n'''
    def div(k):
        '''returns true if n is divisible by k'''
        return n % k == 0
    return div

def prime(n):
    '''returns true if n is prime, returns false is n is composite'''
    result = map(divides(n), range(2, n))
    prime = reduce(add, result)
    return prime < 1
