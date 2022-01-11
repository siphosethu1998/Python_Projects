"""
 This is a recursive program that counts the number of pairs
 of repeated character in a string.
 Author : Siphosethu Shumani
 Date : 2022/01/12 
"""

def count_pairs(s):
    if len(s) < 2:
        return 0
    elif s[0] == s[1]:
        return 1 + count_pairs(s[2:])
    else:
        return count_pairs(s[2:])

# main method is for testing purposes
def main():
    print(count_pairs("hello, salaama"))
    print(count_pairs("aaa, bbb, ccc"))


main()
