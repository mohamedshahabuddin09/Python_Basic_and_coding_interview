# Write a pyhon program that prints the string s without the character at index n
# If the index n is out of range,print the string s intact
# If the string s is empty,print the string s intact

s="Hello"
new_s=""
n=int(input("enter nth number"))

for i in range(len(s)):
    if i!=n:
        new_s+=s[i]
print(new_s)
