"""
    This program
    Author : Siphosethu Shumani
    Date : 26 January 2022
"""

# Input from the user

csv_file_name = input("Enter the name of the CSV file:\n")

# processing

csv_file = open(csv_file_name)

csv_data_headings = csv_file.readline().split(",") # get the index of the csv data headings

csv_data_headings = [item.strip() for item in csv_data_headings] # fixing the spaces and the new line in the items

this_week_index = csv_data_headings.index("this_week")

last_year_index = csv_data_headings.index("last_year")

fsc_index = csv_data_headings.index("fsc")

dam_name_index = csv_data_headings.index("dam")

total_fsc = 0

total_this_week = 0

print(" THIS WEEK LAST YEAR       FSC DAM NAME")

for line in csv_file :
    
    unstrip_line = line.split(",")
    
    striped_line = [item.strip() for item in unstrip_line ]
    
    fsc = float(striped_line[fsc_index])
    this_week_perc = (float(striped_line[this_week_index])/100) * fsc
    last_year_perc = (float(striped_line[last_year_index])/100) * fsc
    
    total_fsc += fsc
    total_this_week += float(this_week_perc)
    
    print('{:10.1f}'.format(this_week_perc),'{:9.1f}'.format(last_year_perc),'{:9.1f}'.format(fsc),striped_line[dam_name_index])
    
print()

current_perc_fsc = round((total_this_week/total_fsc)*100,1)

# output

print("Total FSC is",round(total_fsc,1),"million cubic metres.") 

print("Currently at",str(current_perc_fsc)+'%.')    

csv_file.close()
