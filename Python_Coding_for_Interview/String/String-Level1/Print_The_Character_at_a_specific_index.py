#Description
# Write a python program that prints the character at index i in the string s
# if the index is out of range,the program should print "i out of range"
# Expected Output:
# If the string is "Hello" and i is 2, the output should be "L"
# If the string is "Pizza" and i is 4, the output should be "a"
# If the string is "" and i is 3, the output should be "Empty string"
# If the string is "World" and i is 15, the output should be "i out of range"

s="World"
i=2
if len(s)==0:
    print("string is empty")
elif i<len(s):
    print(s[i])
else:
    print("i out of range")
