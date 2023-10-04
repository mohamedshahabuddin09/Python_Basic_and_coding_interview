str1 = "Hello, "
str2 = "World!"
print(id(str1))
print(id(str2))
str3 = str1 + str2
print(id(str3))
print(str3)  # Prints: Hello, World!


str1 = "Hello, "
num = 7
str3 = str1 + str(num)
print(str3)


greeting = "Hello, " + "World!"
print(greeting)  # Prints: Hello, World!


x = 100
x %= 99
print(x)


x = 5
x =x+ 1  # This is equivalent to x = x + 1
print(x)