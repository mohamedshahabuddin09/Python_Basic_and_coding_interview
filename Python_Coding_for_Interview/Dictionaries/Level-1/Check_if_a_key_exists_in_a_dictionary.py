# Write a python program that checks if a key exists in a dictionary or not
# If the key exists in the dictionary,print True,Else,print False
# The key should be stored in the variable key

my_dictionary={"a":4,"b":6}
key="c"
# print(len(my_dictionary))
# for i in my_dictionary:

#Method-1
if key in my_dictionary:
    print(True)
else:
    print(False)

#Method-2
print(key in my_dictionary)