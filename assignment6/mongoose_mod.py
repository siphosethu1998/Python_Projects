"""
 This program calculates the population of Mongoose species using recursion
 Autho : Siphosethu
 Date: 2022/01/10
"""

def population(n):
    if n == 1:
        return 2
    
    elif n == 2:
        return 2

    else:
        return population(n-1) + population(n-2)
     
