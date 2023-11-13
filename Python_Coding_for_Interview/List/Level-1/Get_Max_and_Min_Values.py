# Write a pyton program that prints the largest and smallest values in a list
# Print the two values on the same line,separated by a space
# The largest value should appear first and the smallest value should appear second
# You may assume that the list only contains numeric values.
# If the list is empty print None

#Method-1
my_list=[5,6,7,3]
# if len(my_list)==0:
#     print(None)
# else:
#     print(max(my_list),min(my_list),end=" ")

#Method-2

# if my_list:
#     print(max(my_list), min(my_list), end=" ")
# else:
#     print(None)

#Method-3
# using sorted() function and len() function

# my_list2=sorted(my_list)
# print(my_list2[len(my_list2)-1])

#Method-4
#without using any built in function

temp=my_list[0]
for i in my_list:
    if i>temp:
        temp=i
print(temp)
