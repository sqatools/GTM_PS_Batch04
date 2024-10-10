#  Write a program to calculate the factorial of a number using Python Loops.
'''num=n=int(input('Enter the Number: '))
fact=1
while n>0:
    fact*=n
    n-=1

print(f"factorial of {num}:{fact}")
'''
#  Write a program to check whether a number is a Prime number or not using  Python Loops.
'''num=int(input("Enter the value: "))
for i in range(1,num+1):
    prime=True
    for j in range(2,i):
        if i%j==0:
            prime=False
            break
        else:
            continue
if prime:
    print("prime",i,end=" ")
else:
    print("not prime")
print()
num=int(input("Number: "))
count=1
for i in range(2,num):
    if num%i==0:
        count+=1
if count>1:
    print("NP")
else:
    print("P")
'''
###############################################################
'''
num=int(input("Give a number:"))
T_count=0
for i in range(1,num+1):
    prime=True
    count=0
    for j in range(2,i):
        if i%j==0:

            prime=False
            count+=1
            break

        else:
            continue

    if i==2:
        T_count+=i
    if prime:
        print(i,end=" ")
    else:
        pass
print()
print(T_count)

###############################################
lower=int(input("lower number: "))
upper=int(input("upper number: "))
total=0

print("Prime number of ",lower,"and",upper,"is: ")
for i in range(lower,upper):
    count=0
    for j in range(2,i):
        if i%j==0:
            count+=1

    if count==2:
        total+=i

print("sum: ",total)'''
##################################################

'''num=int(input("NUmber: "))

for i in range(1,num+1):
    if num%i ==0:
        print(i,end=" ")

print()


num1=int(input("Enter the number: "))
fact=1
while num1>0:
    fact=fact*num1
    num1=num1-1

print(f"Factorial of {num1} is : ",fact)
'''
#####################################################

'''num=int(input("Enter the number: "))
print("factors are: ")

for i in range(1,num+1):
    if num%i ==0:
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            print(i,end=" ")
print()
'''
########################################################

'''num=n=int(input("enter the number: "))
total=0

while n>0:
    digit=n % 10
    total=total + digit**len(str(num))
    n//=10

if num==total:
    print("Armstrong")
else:
    print("Not Armstrong")

print()
print("_"*100)
#############################################################

limit=int(input("Enter the limit: "))

for i in range(1,limit+1):
    total= 0
    temp=num=i
    while temp>0:
        digit=temp%10
        total+=digit**len(str(i))
        temp//=10
    if num==total:
        print(num,end=" ")'''

str1="python programming"
rlt=str1[-1:0:-1]
print(rlt)


print()


for i in range(2):

    for j in range(5):
        if i==0:
            if j==0 or j==4:
                print(" ",end=" ")
            else:
                print("*",end=" ")
        else:
            print("*",end=" ")
    print()

for i in range(4):
    for j in range(5):
        if j==2:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()

for i in range(2):
    for j in range(5):
        if i==1:
            if j==0 or j==4:
                print(" ",end=" ")
            else:
                print("*",end=" ")
        else:
            print("*",end=" ")
    print()


for i in range(6):
    for j in range(5):
        if i==3:
            if j==3:
                print("*",end=" ")
            else:
                print(" ",end="\n ")

        elif i==2 or i==4:
            if j==2 or j==4:
                print("*", end=" ")
            else:
                print(" ", end=" ")


print()
for i in range(6):
    for j in range(5):
        if i==3:
            if j==2 or j==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")

    print()