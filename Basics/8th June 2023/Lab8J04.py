#Identity Operators (is, is not)

#Example-1
a = 5 # Values are checked
b = 5
print(a is b)

name = "shabu"
name1 = "shabu"
print(name is name1)
print(name is not name1)
print(id(name))
print(id(name1))

#Example-2
password = "pramod"
confirm_password = "pramod"
print(password is confirm_password)
print(id(password))
print(id(confirm_password))

#Example-3

list1 = [1, 2, 3] #list - Ref which is checking

list2 = [1, 2, 3]
print(list1 is list2)
#list[0] -> 1 (static)
print(list1[1] is list2[1])  # Prints: False