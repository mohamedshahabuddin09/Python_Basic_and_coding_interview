# Write a python program that prints a list with ListA and ListB have in common
# If they dont have any elements in common,print an empty list
# The program should not assume that the lists have the same length
# You may assume that each element will only appear once in each list.

ListA=[4,5,6]
ListB=[1,2,3]
ListC=[]

for elem in ListA:
    for elem1 in ListB:
        if elem==elem1:
            ListC.append(elem)
print(ListC)
