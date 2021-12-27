# This program calculates the class to which a vehicle belongs.
# Siphosethu Shumani
# 2021/12/27

""" Input """

gvm = int(input("What is the gross vehicle mass (in kg)? \n"))

is_trailer = input("Does the vehicle have a trailer? \n")


""" Process and  Output """
    
if gvm <= 3500:

    if is_trailer[0] in "yY":
        trailer_mass = int(input("What is the gross vehicle mass of the trailer (in kg)? \n"))

        if trailer_mass > 750:
            print("This vehicle is class EB.")
        else:
            print("This Vehicle is class B.") 
    else:
        is_articulated = input("Is the vehicle articulated? \n")

        if is_articulated[0] in "yY":
            print("This vehicle is class EB.")
        else:
            print("This Vehicle is class B.") 

elif 3500 < gvm <= 16000:

    if is_trailer[0] in "yY":
        trailer_mass = int(input("What is the gross vehicle mass of the trailer (in kg)? \n"))

        if trailer_mass > 750:
            print("This vehicle is class EC1.")
        else:
            print("This Vehicle is class C1.") 
    else:
        is_articulated = input("Is the vehicle articulated? \n")

        if is_articulated[0] in "yY":
            print("This vehicle is class EC1.")
        else:
            print("This vehicle is class C1.")
else:

    if is_trailer[0] in "yY":
        trailer_mass = int(input("What is the gross vehicle mass of the trailer (in kg)? \n"))

        if trailer_mass > 750:
            print("This vehicle is class EC.")
        else:
            print("This Vehicle is class C.") 
    else:
        is_articulated = input("Is the vehicle articulated? \n")

        if is_articulated[0] in "yY":
            print("This vehicle is class EC.")
        else:
            print("This vehicle is class C.")





