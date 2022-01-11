"""
 This extends and fixes the mistakes made in broken_mod.py
 author : Siphosethu Shumani
 Date : 2022/11/01
"""

import string

def palindrome (s):
   if len(s) == 1:
      return s.isalpha()
   elif len(s) == 0:
       return True
   elif s[0] in string.punctuation or s[0] in string.whitespace:
       return palindrome(s[1:])
   elif s[-1] in string.punctuation  or s[-1] in string.whitespace:
      return palindrome(s[:-1])
   elif s[0].lower() == s[-1].lower():
      return palindrome (s[1:-1])
   else:
      return False

