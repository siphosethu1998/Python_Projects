# leader_board.py

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
    file_name = input('Enter the name of the file:\n')
    file_input = open(file_name, 'r')
    
    entries = []
    for line in file_input:
        entries.append(process_line(line))
    file_input.close()
    
    entries = sort(entries)
    output(entries)
    
main()
    