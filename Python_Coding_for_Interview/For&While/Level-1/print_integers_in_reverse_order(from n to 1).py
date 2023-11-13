# Write a python program that prints the integers between a given number n and 1(in desecnding order both inclusive)
# The value of n should be entered by the user and may assume that it is an integer greater than or equal to 1
# Use a loop to print each number on a separate line

n=int(input("enter the number"))
for i in range(n,0,-1):
    print(i)
# range()--->range(start,stop,step)
#n=6
#start=n
#start=start+step=6-1=5 first second iteration and soo on.