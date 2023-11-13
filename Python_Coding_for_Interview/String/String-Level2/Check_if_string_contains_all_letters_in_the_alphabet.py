# Write a python program that checks if the string contains all the letters in the alphabets(case-insensitive)
# if it does,print True,Else,print,False

import string
#Method-1
s= " The quick brown fox jumps over the lazy dog"
set_s = set(s.lower())
if " " in set_s:
    set_s.remove(" ")
print(set_s == set(string.ascii_lowercase))

#Method-2
s= " The quick brown fox jumps over the lazy dog"
is_pangram=True

for char in string.ascii_lowercase:
    if char not in s.lower():
        is_pangram= False
print(is_pangram)

#Method-3

s= " The quick brown fox jumps over the lazy dog"
is_pangram=True

for char in string.ascii_lowercase:
    if char not in s.lower():
        is_pangram= False
        break
print(is_pangram)

