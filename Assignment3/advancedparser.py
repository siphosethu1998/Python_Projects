import simpleparser

'''
 This program asks the user to input their ID number and does two things:

  (i) using the check digit, it determines whether the number is valid; 

  (ii) if the number is valid then it decodes and prints out the user’s date of birth, gender, 
citizenship status.

'''
# Siphosethu shumani
# 2021/12/23


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

first_twelve = id[:-1] # getting the first 12 digits

dc = int(id[-1]) # getting the last digit 

total = 0

# calculating the sum of the first 11 digits
for letter in first_twelve:
    
    if first_twelve.index(letter)%2 == 0:

        total += (int(letter)*2)%9

    else:
        total += int(letter)

expected_digit = total%10

''' Output '''


if  10 - expected_digit != dc:
    print("Invalid ID number.")
else:
    print(f'Your date of birth is {day}/{month}/{year}.')

    if gender in female_range : 
        print("You are Female.")
    else : 
        print("You are male.")
    
    if citizen_resident == 0:
        print("You are a South African citizen.")
    else :
        print("You are a permanent resident.") 
