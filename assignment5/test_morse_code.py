# test_morse_code.py
# Stephan Jamieson
# 12/1/2015, 4/2015

def print_welcome():
    print('Test harness for morse_code');
    
def get_selection():
    print('\nChoose from the following options:')
    print('0. quit')
    print('1. Test code_for().')
    print('2. Test transmit_letter().')
    print('3. Test transmit_word().')
    print('4. Test word_pause().')
    return int(input())

def test_code_for():
    from morse_code import code_for
    for letter in "abcdefghijklmnopqrstuvwxyz":
        print(letter, code_for(letter))
        
def test_transmit_letter():
    from morse_code import transmit_letter
    for letter in "abcdefghijklmnopqrstuvwxyz":
        print(letter, ':', end='')
        transmit_letter(letter)
        print()
               
def test_transmit_word():
    from morse_code import transmit_word
    word = input("Enter test word:\n")
    transmit_word(word)
    
def test_word_pause():
    from morse_code import word_pause    
    word_pause()


def main():
    print_welcome()
    selection = get_selection()
    
    while not selection==0:
        if selection==1:
            test_code_for()
        elif selection==2:
            test_transmit_letter()
        elif selection==3:
            test_transmit_word()
        elif selection==4:
            test_word_pause()
        else:
            print('Sorry, that selection was not recognised.')
            
        selection = get_selection()
main()