# Write a python program that prints a triangular pattern like the ones shown below in the examples.
# Each row must hhave its corresponding number of asterisks.
# The first row contains one asterisk. The second row contains two asterisk.
# The third row contains three asterisk and so on.
# The number of rows should be determined by the value of n,a value entered by the user.

n=int(input("enter the value"))

for i in range(1,n+1):
    print("a"*i)