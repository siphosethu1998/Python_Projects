"""
    This program has helper functions and serves as a module to solver.py
    Author : Siphosethu Shumani
    Date : 2022/01/12

"""

def make_state(num_frogs, num_toads):
    return ["Frog"]*num_frogs + [""] + ["Toad"]*num_toads

def find_space(state):
    """ obtains the index of the empty puzzle """
    return state.index("")

def is_frog(state, index):
    """ Return True if there is a frog at the given index, otherwise return False. """

    if state[index] == "Frog":
        return True
    return False

def is_toad(state, index):
    """ Return True if there is a toad at the given index, otherwise return False. """

    if state[index] == "Toad":
        return True
    return False

def move(state, index):
    """ Return the new state, S’, produced by moving the frog or toad at the given index """
    
    newState = list(state)
    print(newState)

    if is_frog(newState,index):

        # swapping the indices of space and frog
        if newState[index+1] == newState[find_space(newState)]:
            newState[index+1] = newState[index] # move frog to space
            newState[index] = ""  # move space to where frog was

        # jumping over a toad or another frog
        else:
            if newState[index+2] == "": # checking if there's space after the toad or frog
                newState[index+2] = newState[index] # jump over the toad or frog to free space
                newState[index] = "" # move space to where the frog was
    
    else:

        # swapping the indices of space and toad
        if newState[index-1] == newState[find_space(newState)]:
            newState[index-1] = newState[index] # move toad to space
            newState[index] = ""  # move space to where toad was

        # jumping over a frog or another toad
        else:
            if newState[index-2] == "": # checking if there's space after the toad or frog
                newState[index-2] = newState[index] # jump over the toad or frog to free space
                newState[index] = "" # move space to where the frog was

    return newState

def print_state(state):
    """ Print the given state as a sequence of strings separated by vertical bars """

    for animal in state:
        if animal == "":
            print("|    ", end="")
        else:
           print(f"|{animal}", end="") 
            
    print("|")
    
def is_win(state):
    frogs_one_side = False
    toads_one_side = False

    # checking if all toads are on one side
    for animal in range(0, find_space(state)):
        if state[animal] == "Toad":
            toads_one_side = True
        else:
            toads_one_side = False
            break
    
    # checking if all frogs are on one side
    for animal in range(find_space(state)+1, len(state)):
        if state[animal] == "Frog":
            frogs_one_side = True
        else:
            frogs_one_side = False
            break
        
    if frogs_one_side == True and toads_one_side == True:
        return True
    return False

# the main method is just for testing
def main():
    print(is_win(["Toad","Toad", "","Frog","Frog"]))

main()

