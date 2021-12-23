# This program asks the user to input their ID number, and then decodes and prints out their date of birth, gender, and citizenship status.
# siphosethu shumani
# 2021/12/22


''' input '''

id = input("Please enter your ID number: ")


''' Processing '''

# extracting needed information
year = id[0:2]

month  = id[2:4]

day  = id[4:6]

gender = int(id[6:10])

female_range = list(range(0, 5000))

citizen_resident = int(id[10])


''' Output '''

print(f'Your date of birth is {day}/{month}/{year}.')

if gender in female_range : 
    print("You are Female.")
else : 
    print("You are male.")

if citizen_resident == 0:
    print("You are a South African citizen.")
else :
    print("You are a permanent resident.") 
