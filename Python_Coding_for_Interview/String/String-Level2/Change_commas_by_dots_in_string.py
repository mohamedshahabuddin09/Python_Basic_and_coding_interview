# Write a python program that prints a version of the string with all commas replaced by dots.
#Metod-1
s="Hello,World!"
new_s=""
comm_string=","
dot_string="."
for i in s:
    if i==comm_string:
        new_s+=dot_string
    else:
        new_s+=i
print(new_s)

#Metod-2
s="Hello,World!"
new_s=""
comm_string=","
dot_string="."

print(s.replace(comm_string,dot_string))