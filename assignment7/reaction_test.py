"""
    This is program that calculates the reation time of test subjects.
    Author : Siphosethu Shumani
    Date : 25 January 2022
"""

from time import *
from random import *

def flush_input(): 
    try :
        import  msvcrt 
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError :
        import sys, termios 
        termios.tcflush(sys.stdin, termios.TCIOFLUSH) 
        
def process_test_subjects():
    file_name = input("Enter the name of the output file: \n")
        
    sub_name = input("Enter subject name (or press 'enter' to quit): \n")
    
    while not sub_name == 'quit':
        num_of_tests = int(input("Enter the number of tests:\n")) # get the number of tests
        
        sum_reaction_time = 0
        
        for test in range(num_of_tests): # processing the number of tests
            
            print('Get ready...', flush=True)
                                                                
            sleep(randint(1,5))
            
            flush_input()
                                    
            initial_time = time()
            
            sub_response = input("Press 'enter' NOW!")
           
            end_time = time()
            
            reaction_time = round(end_time - initial_time ,6)
            
            print("Reaction time:",reaction_time) # displaying the reaction time
            
            sum_reaction_time += reaction_time
            avg_reaction_time = round(sum_reaction_time/num_of_tests,6)
            
        print("Tests complete.")
        print("Average reaction time:", avg_reaction_time ) # displaying the average reaction time
        
        file_input = open(file_name,'a')
        
        print(sub_name,str(num_of_tests),str(avg_reaction_time), file=file_input)
        
        file_input.close()
        
        sub_name = input("Enter subject name (or press 'enter' to quit): \n")
  
def main():
    
    process_test_subjects()
    
main()
