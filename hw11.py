'''
Created on 4/22/20
@author:  Claudia MacRae
Pledge:  I pledge my honor that I have abided by the Stevens Honor System.

CS115 - HW 11
'''
# nim template DNaumann (2018), for assignment nim_hw11.txt 

# Global variables used by several functions
piles = []         # list containing the current pile amounts
num_piles = 0      # number of piles, which should equal len(pile)


def play_nim():
    """ plays game of nim between user and computer; computer plays optimally """
    
    init_piles()
    display_piles()
    while True:
        user_plays()
        display_piles()
        if sum(piles) == 0:

            print("I didn't think it was possible, but you've won")

            break
        computer_plays()
        display_piles()
        if sum(piles) == 0:

            print("As expected, another win for me")

            break


def init_piles():
    """ Assign initial values to the global variables 'num_piles' and
        'piles'
        User chooses number of piles and initial size of each pile.
        Keep prompting until they enter valid values."""
    global piles
    global num_piles

    num_piles = int(input("How many piles would you like to play with? "))
    piles = [0]*num_piles
    for index in range(num_piles):
        print("How many coins in pile", index ,"? ", end = '')
        piles[index] = int(input())
        

        
def display_piles():
    """ display current amount in each pile """
    global piles
    global num_piles

    i = 0
    while i < num_piles:
        print('Pile ', i, '= ', piles[i])
        i += 1


def user_plays():
    """ get user's choices and update chosen pile """
    global piles
    
    print("Your turn ...")
    p = get_pile()
    amt = get_number(p)
    piles[p] = piles[p] - amt


def get_pile():
    """ return user's choice of pile
        Keep prompting until the choice is valid, i.e.,
        in the range 0 to num_piles - 1. """
    global piles
    global num_piles

    chosen_pile = int(input("Which pile? "))
    while chosen_pile not in range(0, num_piles):
        print("That is not a valid choice. Please pick a pile between 0 and", num_piles - 1)
        chosen_pile = int(input("Which pile? "))
    return chosen_pile


def get_number(pnum):
    """ return user's choice of how many to remove from pile 'pnum'
        Keep prompting until the amount is valid, i.e., at least 1
        and at most the amount in the pile."""
    global piles
    
    chosen_remove = int(input("How many? "))
    while chosen_remove not in range(1, piles[pnum] + 1):
        if chosen_remove < 1: print('You must remove at least one coin. Try again.')
        else: print("You can not remove more coins than are there. Money doesn't grow on trees you know")
        chosen_remove = int(input("How many? "))
    return chosen_remove


def game_nim_sum():
    """ return the nim-sum of the piles """
    global piles
    global num_piles 

    nSum = 0
    for p in piles:
        nSum = nSum ^ p
    return nSum


def opt_play():
    """ Return (p,n) where p is the pile number and n is the amt to
        remove, if there is an optimal play.  Otherwise, (p,1) where p
        is the pile number of a non-zero pile.

        Implement this using game_nim_sum() and following instructions
        in the homework text."""
    global piles
    global num_piles 

    nim_sum = game_nim_sum()
    for i in range(num_piles):
        pile_sum = nim_sum ^ piles[i]
        if pile_sum < piles[i]: return (i, piles[i] - pile_sum)
    j = 0
    while piles[j] == 0:
        j += 1
    return (j, 1)


def computer_plays():
    """ compute optimal play, update chosen pile, and tell user what was played

        Implement this using opt_play(). """
    global piles
    global num_piles
    print('My turn! Watch and learn grasshopper ...')
    p, amt = opt_play()
    piles[p] -= amt
    print('I remove', amt, 'coins from Pile', p)

    


#   start playing automatically
if __name__ == "__main__" : play_nim()
