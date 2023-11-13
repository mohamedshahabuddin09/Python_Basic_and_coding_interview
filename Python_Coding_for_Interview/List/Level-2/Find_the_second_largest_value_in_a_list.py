# Write a python program that prints the second largest value in a list
# If the list is empty or only has one element,print None

my_list=[]

if len(my_list)>1:
    sorted_list=sorted(my_list)
    print(sorted_list[-2])
else:
    print(None)