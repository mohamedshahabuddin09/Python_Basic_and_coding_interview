# Write a program to count the number of repeated characters in the string
# The program must print the total number of repeated characters and a message on
# the next line displaying the repeated characters separated by a space and sorted alphabetically
# If there are no repeated characters in the string,print 0 as the total count abd none on the next line

s="Hello"

repeated_count=0
repeated_chars=[]

for char in s:
    print(s.count(char))
    if (s.count(char)>1) and (char not in repeated_chars):
        repeated_count+=1
        repeated_chars.append(char)
print(repeated_count)

if len(repeated_chars)>0:
    for char in sorted(repeated_chars):
        print(char,end="")
else:
    print(None)