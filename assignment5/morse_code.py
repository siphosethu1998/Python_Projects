"""
    This program serves a module for 
    Author : Siphosethu Shumani
    Date : 2022/01/07
"""

from morse_utils import *

letter_code_dict = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".",
                    "f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---",
                    "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---",
                    "p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-",
                    "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", 
                    "z":"--.."
}


def code_for(letter):
    """
        A function that returns the Morse code for a given letter ('a', ...,'z', 'A', ...,'Z'). For example,
        given the parameter value 'S', the function returns '...'. 
    """
    return letter_code_dict[letter.lower()]

def morse_beep(char):
    """
        produces a beep sound based on the character.
        100ms for a dot, 300ms for a dash and 700ms for a word pause
    """
    
    if char == ".":
        beep(1000, 100)
    elif char == "-":
        beep(1000, 300)
    else:
        beep(1000, 700)

def transmit_letter(letter):
    """
        A function that accepts a letter ('a', ...,'z', 'A', ...,'Z') as a parameter, determines the
        corresponding Morse code, and then makes the computer produce the required series of
        beeps and pauses. 
    """

    transmitted_letter = ""
    
    if len(code_for(letter)) == 1:
        morse_beep(code_for(letter))
        return code_for(letter)
    else:
        for char in code_for(letter):
            morse_beep(char)
            transmitted_letter += char + "^" 

        return transmitted_letter[:-1]

def transmit_word(word):
   """
        A function that accepts a word (composed of the letters 'a', ...,'z', 'A', ...,'Z'), determines the
        corresponding Morse code sequence, and then makes the computer produce the required
        series of beeps and pauses.
   """

   transmitted_word = ""

   for letter in word:
       transmitted_word += transmit_letter(letter) + "|"

   print(transmitted_word[:-1], end="")

def word_pause():
    """
        A function that prints two vertical bars and causes the program to pause (be silent) for the
        duration of 7 dots.
    """
    morse_beep("||")    
    print("||", end="")

