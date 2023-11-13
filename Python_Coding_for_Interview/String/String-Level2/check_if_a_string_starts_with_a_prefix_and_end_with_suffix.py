# Write a python program that checks if the string s starts with the sequence of characters denoted by the variable prefix
# If it does, print True,Else,print False

#Method-1

# s="Hello"
# prefix = "He"
# print(s[:len(prefix)]==prefix)

#Method-2

s="Hello"
suffix="ello"
print(s[-len(suffix):]==suffix)

#Method-3 using string built in functions

#startswith(prefix)
#endswith(suffix)




