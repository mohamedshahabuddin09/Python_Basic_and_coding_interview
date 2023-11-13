# Write a pyhon program that prints the first and last three characters of the string as a single string
# if the string has less than six characters, print an empty string

s="blue"
if len(s) <6:
    print("")
else:
    ss=s[:3]+s[len(s)-3:]
    print(ss)
