"""
    This program logs information of endangered animals being tracked for a conservation study.
    The program will prompt the user for animal identity codes and then iteratively respond to the following commands.

    author : Siphosethu Shumani

    date: 2021/12/30
"""

def main():


    """ Input, Process and Output """

    code_ordinates_dict = {} # empty dictionary for the codes and ordinates

    print("Please enter the animal identity codes. (Press return when done.)")

    counter = 1

    while True:
        print(f"Animal no. {counter}:") 

        identity_code = input("")

        if identity_code == "":
            break

        code_ordinates_dict[identity_code] = [] # setting values of the dict to a list    
        counter += 1
    

    print("Commands: print, log <animal id> <x ord> <y ord>, quit.")

    while True:
        command = input(">")

        if command == "print":
            
            for key in code_ordinates_dict:

                if code_ordinates_dict[key]: # if the dict value has something print the details
                    print(f"Animal {key} last seen at ({code_ordinates_dict[key][0]}, {code_ordinates_dict[key][1]}).")
                else:
                    print(f"Animal {key} cannot be located.")  

        elif command[:3]  == "log":
            log_list = command.split(" ")
            
            # checking if the ordinates are integers, if so map them to their corresponding code, else print an error message
            if log_list[2].isdecimal() and log_list[3].isdecimal():

                # mapping the ordinates of the animal to its code
                for key in code_ordinates_dict:
                    
                    if log_list[1] == key:
                        temp_list = []
                        temp_list.append(int(log_list[2]))
                        temp_list.append(int(log_list[3]))
                        code_ordinates_dict[key] = temp_list
            else:
                print("The ordinates should be integers.")
                print("log <id> <x ord> <y ord>")

        elif command  == "quit":
            break
        else:
            print("Could not interpret command.")
            print("Commands: print, log <animal id> <x ord> <y ord>, quit.")

main()
