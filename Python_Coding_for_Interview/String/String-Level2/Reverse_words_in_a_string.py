# Write a python program that reverses the individual words in the string and
# changes their capitalization.
# Uppercase letters should be printed in lowercase and vice versa
# Assume that the string only contains letters and spaces are used to separate words.

#Method-1 whole string reverse
# s="Hello World"
# new_str=""
# count=len(s)-1
# while count >=0:
#     new_str+=s[count]
#     count=count-1
# print(new_str)

#Method-2
s="Hello World"
new_str=""
s1=s.split(" ")
for i in s1:
    reve_words="".join(reversed(i))
    swap_case=reve_words.swapcase()
    new_str+=swap_case+" "
print(new_str)