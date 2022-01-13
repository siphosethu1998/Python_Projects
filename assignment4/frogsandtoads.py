"""
    - This program allows a person to play a game of Frogs and Toads using the computer. 
    - The program should ask for the number of frogs and the number of toads, and
    then repeatedly print the puzzle state and ask the user for the index of a frog or toad to move.

    Author : Siphosethu Shumani

    Date : 2021/12/31
"""

""" Input """

num_frogs = int(input('Enter the number of frogs:\n'))

num_toads = int(input('Enter the number of toads:\n'))


""" Process and Output """

state = ['Frog']*num_frogs+['']+['Toad']*num_toads

# corresponding positions on top of the frogs and toads
for i in range(len(state)):
    print(f"{i+1:3}", end=" ")

print()

# display frogs and toads
for item in state:
    if item == "":

        print("    ", end="")
    else:

        print(item, end="")

print()

# play the game
while True:
    command = input(">")

    if command == "quit":
        break

    else:
        current_index = int(command) - 1

        if state[current_index] == "Frog":

            # swapping the indices of space and frog
            if state[current_index+1] == "": 
                state[current_index+1] = state[current_index] # move frog to space
                state[current_index] = ""  # move space to where the frog was

            # jumping over the toad
            else:
                state[current_index+2] = state[current_index] # jump over the toad to free space
                state[current_index] = ""  # move space to where the frog was

        else:

            # swapping the indices of space and toad
            if state[current_index-1] == "": 
                state[current_index-1] = state[current_index] # move toad to space
                state[current_index] = ""  # move space to where the toad was

            # jumping over the frog
            else:
                state[current_index-2] = state[current_index] # jump over the frog to free space

                state[current_index] = ""  # move space to where the toad was


    # corresponding positions on top of the frogs and toads
    for i in range(len(state)):
        print(f"{i+1:3}", end=" ")

    print()

    # display frogs and toads
    for item in state:
        if item == "":

            print("    ", end="")
        else:

            print(item, end="")

    print()

    # ending the game if all toads on the left side and frogs are on the right
    space_index = state.index("")

    frogs_one_side = False
    toads_one_side = False
    
    # checking if all toads are on one side
    for animal in range(0, space_index):
        if state[animal] == "Toad":
            toads_one_side = True
        else:
            toads_one_side = False
            break
            
    # checking if all frogs are on one side
    for animal in range(space_index+1, len(state)):
        if state[animal] == "Frog":
            frogs_one_side = True
        else:
            frogs_one_side = False
            break
   
    if frogs_one_side == True and toads_one_side == True:
        print("Congratulations, you've won!")
        break

    if state[0] == "":
        if state[1] == "Frog" and state[2] == "Frog":
            print("Sorry, you've lost.")

    elif  state[len(state)-1] == "":
        if state[len(state)-2] == "Toad" and state[len(state)-3] == "Toad":
            print("Sorry, you've lost.")
    else:
        continue

