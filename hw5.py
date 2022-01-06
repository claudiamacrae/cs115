'''
Created on 2/26/20
@author:  Claudia MacRae
Pledge:  I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 5
'''
import turtle  # Needed for graphics

def sv_tree(trunk_length, levels):
    '''draws tree with given number of levels
        each branch of the tree will be half as long as its parent branch'''
    if(levels != 0):
        startingpos = turtle.pos()
        startingangle = turtle.heading()
        turtle.forward(trunk_length)
        turtle.setheading(startingangle + 45)
        sv_tree(trunk_length/2, levels - 1)
        turtle.setheading(startingangle - 45)
        sv_tree(trunk_length/2, levels - 1)
        turtle.setpos(startingpos)
        
memo = {}
def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    if n == 0:
        return 2
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    answer = fast_lucas(n - 1) + fast_lucas(n - 2)
    memo[n] = answer
    return answer

def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, coins, memo):
        if (amount, coins) in memo:
            return memo[(amount, coins)]
        if coins == () and amount != 0:
            return float("inf")
        if coins == ():
            return 0
        if coins[0] > amount:
            return fast_change_helper(amount, coins[1:], memo)
        else:
            use = 1 + fast_change_helper(amount - coins[0], coins, memo)
            lose = fast_change_helper(amount, coins[1:], memo)
            r = min(use, lose)
            memo[(amount, coins)] = r
            return r

    # Call the helper. Note we converted the list to a tuple.
    return fast_change_helper(amount, tuple(coins), {})

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a tree.
sv_tree(100, 4)
