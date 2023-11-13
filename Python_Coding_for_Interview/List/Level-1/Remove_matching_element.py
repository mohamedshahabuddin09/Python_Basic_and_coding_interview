# Write a python program that removes all occurences of the element element_to_remove from a list
# The output of the program should be the new list with the element removed
# If the element is not found in the list,print the message not found
# If the list is empty,print "Empty list"

# Method-1

my_list=[]
element_to_remove=0
my_list2=[]
if len(my_list)==0:
    print("Empty List")
elif element_to_remove not in my_list:
    print("Not found")
else:
    for i in range(len(my_list)):
        if my_list[i]!=element_to_remove:
            my_list2.append(my_list[i])
    print(my_list2)