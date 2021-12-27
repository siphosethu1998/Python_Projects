# This program displays a conversion table for measurements in feet to measurements in metres.
# Siphosethu Shumani
# 2021/12/27

""" input """

min_feet = int(input("Enter the minimum number of feet (not less than 0): \n"))

max_feet = int(input("Enter the maximum  number of feet (not more than 99): \n"))

""" Process and Output """
feet_to_metres = 0

for feet in range(min_feet, max_feet+1):
    feet_to_metres = feet/3.28

    print(f"{feet:2}' |   {feet_to_metres:<04.3}m")
