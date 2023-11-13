# Write a python program that sorts in ascending order the lists contained as values in a dictionary
# The dictionary contains key-value pairs that match strings to lists. you need to sort these lists
# The lists have to be mutated(changed

my_dic={
    "a":[7,3,4],
    "b":[3,5,7],
    "c":[1,9,10]
}
new_dic_list={}
for i in my_dic.values():
    i.sort()
print(my_dic)