import string

def palindrome (s):
   if len(s) == 1:
      return s.isalpha()
   elif s[0] in string.punctuation or s[0] in string.whitespace:
      return palindrome(s[:-1])
   elif s[-1] in string.punctuation or s[-1] in string.whitespace:
      return palindrome(s[:-1])
   elif s[0].lower() == s[-1].lower():
      return palindrome (s[1:-1])
   else:
      return False

