# Write a python program that prints the elements of a list on the same line
# The elements should be separated only by a space(not by a comma)
# The output should not include the opening and closing square brackets.


#Methhod-1
list=[3,4,5,6]
# for elem in list:
#     print(elem,end=" ")

#Method-2

print(*list,sep=" ")