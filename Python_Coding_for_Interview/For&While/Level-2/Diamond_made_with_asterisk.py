# Write a python program that cecks if a number is prime or not
# If the number is prime,it should print prime
# If the number is not prime,it should print not prime

n=int(input("enter the number"))

is_prime=True

if n==1 or n==0:
    is_prime=False
else:
    for i in range(2,n):
        if n%i==0:
            is_prime=False
            break
if is_prime:
    print("prime")
else:
    print("Not a prime")