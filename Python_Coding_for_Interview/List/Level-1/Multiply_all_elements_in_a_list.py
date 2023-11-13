# Write a python program that multiplies all the items in a list by the value of the variable factor
# The program must print the list as the output
# The program should also allow multiplying the variable factor by a string incase the list contains string
# You may assume that the value of factor will be a positive integer

list=["a","b","c"]
factor=3

for i in range(len(list)):
    list[i]=list[i]*factor
print(list)