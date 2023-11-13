# Write a python program that counts the number of elements in a list with value greater than 3
# You may assume list only contains numbers
# print the final count

my_list=[1,-1,8,9,2,3]
count=0

for elem in my_list:
    if elem>3:
        count+=1
print(count)