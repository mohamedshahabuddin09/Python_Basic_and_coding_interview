# Write a python program that removes duplicates elements from a list,only keeping one occurence of each element in the list
# The original list should be mutated(modified)
# The program must print the final version of the list
# hint:use set() function

my_list=[1,1,2,3,4,4]

no_duplicates=list(set(my_list))
print(no_duplicates)

