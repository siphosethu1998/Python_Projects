# leader_board.py
# Siphosethu Shumani
# Date : 25 Jan 2022

def process_line(line):
    parts = line.split(' ')
    name = parts[0]
    trials = int(parts[1])
    average = float(parts[2])
    return (name, trials, average)

def get_max(entries):
    max = entries[0]
    for i in range(1, len(entries)):
        if entries[i][2] <max[2]:
            max = entries[i]
            
    entries.remove(max)
    return max

def sort(entries):
    sorted_entries = []
    while len(entries)>0:
        sorted_entries.append(get_max(entries))
    return sorted_entries

def output(entries):
    print('Subject        | Average Time')
    print('************** | ************')
    for entry in entries:
        print('{:14} | {:.6}'.format(entry[0], entry[2]))
              
def main():
    try:
        file_name = input('Enter the name of the file:\n')
        file_input = open(file_name, 'r')
        
    except IOError:
        print("Could not find the specified file.")
        file_name = input('Enter the correct file name: \n')
    finally:
        counter = 0
        file_input = open(file_name, 'r')
        entries = []
        for line in file_input:
            counter += 1
            try:
                entries.append(process_line(line))
            except ValueError as val_err:
                print(f"{val_err} has occured in line {counter}")
                print(line, end="")
                print("The correct format is : <name of test subject> <number of trials> <average> \n") 
        file_input.close()
        
        entries = sort(entries)
        output(entries)
        
main()
    
