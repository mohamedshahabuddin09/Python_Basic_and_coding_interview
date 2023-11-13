# Write a Python program that prints the reversed version of a string
# The program must preserve uppercase and lowercase lettrers
# If the string is empty print it intact

#Method-1
s="Hello"
#string[start:stop:step]
# here we are not mentioning the start and stop of characters so we are given step
print(s[::-1])

#Method-2

rev_string="".join(reversed(s))
print("The reverse string is"+" "+rev_string)