# Write a python program that prints a copy of the string without any spaces
# Words should be connected in the final string
# If the string does not contains spaces, print it intact.

#Method-1
s="python h"
rem_space=" "
new_str=""
for i in s:
    if i!=rem_space:
        new_str=new_str+i
print(new_str)

# #Method-2
#
# s=" Hello how are you "
# print(s.replace(" ",""))

