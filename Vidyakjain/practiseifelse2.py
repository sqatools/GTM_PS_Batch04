################
for i in range(10, 1, -1):
    print(i)

#########print table of any given number######

n=5
for i in range(1,11):
 print(n,"*",i,":",i*n)

################program to check number is divided by 3 and 5###########
n=8
if n%3==0 and n%5==0:
    print("number is divided by 3 and 5")
else:
    print("number is not divided by 3 and 5")

##########program to print the square of the number if it is divided by a certain number ( 11 ).#########
n=33
if n%11==0:
    print(n**2)
else:
    print("number is not divisible by 11")

################Program to check whether the number is a prime number######
num=3
if num==2:
    print("number is prime number")
elif num == 3:
    print("number is prime number")
elif num == 5:
    print("number is prime number")
elif num == 7:
    print("number is prime number")
elif num == 11:
    print("number is prime number")
else:
    print("number is not prime")