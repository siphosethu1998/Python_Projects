# This program displays a conversion table for inches to metres
# Siphosethu shumani
# 2021/12/27

""" input """

min_inch = int(input("Enter the minimum number of inches (not less than 0): \n"))

max_inch = int(input("Enter the maximum  number of inches (not greater than 11): \n"))
    
""" Process and output """
inches_to_metres = 0

# Displaying inches
print("Inches: ", end="")

for inch in range(min_inch, max_inch+1):
    
    print(f"{inch:4}", end=" ")

print()

# Displaying metres
print("Metres: ", end="")

for inch in range(min_inch, max_inch+1):
    inches_to_metres = inch*0.0254
    print(f"{inches_to_metres:4.2f}", end=" ")
