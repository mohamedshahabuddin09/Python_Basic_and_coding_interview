# Write a python program that prints (as a list) the elements of ListA that are not in ListB
# if the lists have the same elements,print an empty list.
# If ListA is an empty list,print an empty list

list1=[]
list2=[1,2,3,4]
list3=[]

# if list1 in list2:
#     print(list3)
# elif len(list1)==0 and len(list2)!=0:
#     print(list1)
# else:
for elem in list1:
    if elem not in list2:
        list3.append(elem)
print(list3)
