# Write a python program that prints the largest value in a dictionary
# If the dictionary is empty,print None
# You may assume that the values are numeric

my_dic ={"a": 4, "b": 3, "c": 7,"d":4}

#Method-1

# if not my_dic:
#     print(None)
# else:
#     new_dic = list(my_dic.values())
#     new_list2=sorted(new_dic)
#     print(new_list2)
#     print(new_list2[0])

#Method-2

if my_dic:
    max_value=max(set(my_dic.values()))
    #print(type(max_value))
    print(max_value)
else:
    print(None)
