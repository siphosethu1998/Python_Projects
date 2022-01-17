"""
    This is a program that play the frogs and toads game by itself
    Author : Siphosethu Shumani
    Date : 2022/01/12
"""

from solver_mod import *

def solvable(S):
    """
        Given a puzzle state, S, if solvable(S) is True, then S is solvable i.e.
        a series of moves can be made to get to the winning state (a series of toads, followed by
        a space, followed by a series of frogs). If solvable(S) is False, then it is not solvable i.e. a series of
        moves cannot be made to get to the winning state
    """

    # Base case(s)
    if is_win(S):
        #print_state(S)
        return True

    elif find_space(S) == 0 and is_frog(S, find_space(S)+1) and is_frog(S, find_space(S)+2):
        print("Space at the beginning")
        return False
        
    elif find_space(S) == len(S)-1 and is_toad(S, find_space(S)-1) and is_toad(S, find_space(S)-2):
        print("Space at the end")
        return False

    # recurse
    else: 
        if len(S) == 3: # if we have 1 frog and 1 toad
            if is_frog(S, find_space(S)-1):
                newState = move(S, find_space(S)-1)
                print_state(newState)
                return solvable(newState)

            else: # this is equivalent to find_space(S) == 0:
                newState = move(S, 2)
                print_state(newState)
                return solvable(newState)
                
        else: # for two frogs and/or more toads
            if is_frog(S, find_space(S)-1):
                newState = move(S, find_space(S)-1)
                print_state(newState)
                return solvable(newState)

            elif is_toad(S, find_space(S)+1):
                newState = move(S, find_space(S)+1)
                print_state(newState)
                return solvable(newState)
            
            elif is_frog(S, find_space(S)-2):
                newState = move(S, find_space(S)-2)
                print_state(newState)
                return solvable(newState)
            
            else: # is_toad(S, find_space(S)+2)
                newState = move(S, find_space(S)+2)
                print_state(newState)
                return solvable(newState)
        
def main():

    print("Welcome back to the frogs and toads game")
    print("Comes with a twist because this time it's played by a computer")
    print("Please do the following :")
    print()

    num_frogs = int(input('Enter the number of frogs:\n'))

    num_toads = int(input('Enter the number of toads:\n'))

    state = make_state(num_frogs, num_toads)

    print_state(state)
    
    if solvable(state) == False:
        print("Sorry computer, you lose.")
    else:
        print("Congratulations computer, you've won!")

main()
