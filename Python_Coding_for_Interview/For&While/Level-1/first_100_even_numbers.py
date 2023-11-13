# Write a python program that prints the first 100 even numbers (from 2 to 200 inclusive)

#Method-1
for i in range(2,201,2):
    print(i)

#Method-2
for i in range(1,201):
    if(i%2==0):
        print(i)
