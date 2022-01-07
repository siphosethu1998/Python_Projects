import morse_code


def main():
    message=input('Enter message:\n')
    
    words=message.split(' ')
    
    word=words[0]
    morse_code.transmit_word(word)
    words=words[1:]
    for word in words:
        morse_code.word_pause()
        morse_code.transmit_word(word)
    
main()