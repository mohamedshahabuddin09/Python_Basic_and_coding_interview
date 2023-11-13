# Write a python program that prints the string without the characters located at even indices
# If the string is empty or only has one character, print it without any changes

s="Coding"
new_s=""
count=len(s)

#Method-1
# for i in range(count):
#     if(i%2!=0):
#         new_s=new_s+s[i]
# print(new_s)

#Method-2-using increment value in range() function

for i in range(1,len(s),2):
    new_s+=s[i]
print(new_s)
