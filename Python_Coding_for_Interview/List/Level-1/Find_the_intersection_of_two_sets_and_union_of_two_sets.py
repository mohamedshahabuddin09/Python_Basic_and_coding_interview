# Write a python program that finds the intersection of two sets(set 1 and set 2)
# Create a new set called intersection with their intersection
# Print the new set as the output
# If the intersection is empty,print an empty set.

set1={1,2,3,4,5}
set2={3,4,7,8,9}

intersection=set()

#print(type(intersection))

#Method-1

# for elem in set1:
#     if elem not in set2:
#         intersection.add(elem)
# print(intersection)

#Method-2

print(set1.intersection(set2))
print(set1.union(set2))
