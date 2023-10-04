age = int(input("Enter your Age to Watch the A Grade Movie"))
# Condition ->  if age > 18 then I am allowed to watch the A rated.

# Condition - If else Loop
# If Condition which true Execute Code 1
# Else condition the condition Else Code 2


# Condition ? age > 18 -> true or false
# age = 31 ? x No Condition
# 7 > 9 ? True or False -> False
# 199/2 > 4 ? Yes


# 1st Only using the If and Else
# if condition:
#     # Code to be Exute if Condition is True
# else <False> :
#     # Code to be Exute if Condition is False

if age>18:
    print("Yes you can watch the A Rated Movie")
else:
    print("You can' add the watch the Movie")

x=20
y=20
if x>y:
    print("x is larger")
if y>x:
    print("Y is larger")
else:
    print("both are equal")

a=10
b=6
c=7
if a>b and a>c:
    max=a
elif b>c and b>a:
    max=b
else:
    max=c

print("max is"+str(max))