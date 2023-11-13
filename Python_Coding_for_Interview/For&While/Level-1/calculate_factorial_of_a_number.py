# Write a python program that calculates the factorial of a given number n
# The value of n should be entered by the user
# The program must print the result and use a loop to calculate it

#0!=1
#3!=3*2*1=6

n=int(input("enter the number"))
fact=1

for i in range(1,n+1):
    fact=fact*i
print(fact)
