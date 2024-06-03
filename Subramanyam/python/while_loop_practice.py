for i in range(1500,2701):
    if i%7==0 and i%5==0:
        print(i)

##############################
val=0
for i in range(6):
    for j in range(i):
        print(j,end=" ")
        val+=1
    print()

for i in range(6,0,-1):
    for j in range(i):
        print(j,end=" ")
        val+=1
    print()
print("*"*100)

temp=1
for i in range(6):
    for j in range(i):
        print(temp,end=" ")
        temp+=1
    print()
temp1=15
for i in range(5,0,-1):
    for j in range(i):
        print(temp1,end=" ")
        temp1-=1
    print()

print("*"*100)

ascii_valve=65
for i in range(6):
    for j in range(i):
        print(chr(ascii_valve),end=" ")
        ascii_valve+=1
    print()

for i in range(6,0,-1):
    for j in range(i):
        print(chr(ascii_valve),end=" ")
        ascii_valve+=1
    print()

print("*"*100)

num=197
prime = True

for i in range(2,num):
    #print(i,end=" ")
   # print()
    if num%i==0:
        prime= False
        break
    else:
        continue

if prime:
    print("prime")
else:
    print("not prime")


'''
for n in range(2,100):
    prime = True
    for i in range(2,n):
        if n%i==0:
            prime=False
            break
        else:
            continue

    if prime:
        print(n,end=" ")
    else:
        pass
'''

for i in range(2,100):
    prime=True
    for j in range(2,i):
        if i%j==0:
            prime=False
            break
        else:
            continue
    if prime:
        print(i,end=" ")
    else:
        pass
print()

str1="python"
n=""
for i in range(len(str1)):
    n +=str1[i]

print(n)

############################################
lst=[1,2,3,4,5,6,7,8,9]
even=0
odd=0
for i in lst:
    if i%2==0:
        even+=1
    else:
        odd+=1

print(even)
print(odd)

################################################
lst=(1,2,3,4,5,6,7,8,9)
even=0
odd=0
for i in lst:
    if i%2==0:
        even+=1
    else:
        odd+=1

print(even)
print(odd)
################################################
print("$"*100)
for i in range(10):
    if i!=3 and i!=6:

        print(i)


##################################################

num1=0
num2=1
count=0

print("fibonacci serics for 20: ",end=" ")
while count<20:
    print(num1,end=" ")
    n3=num1+num2
    num1=num2
    num2=n3
    count+=1
print()
###########################################################

for i in range(1,31):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")

#############################################################
'''
tet=input("Enter string")
for c in tet:
    if c.isupper():
        print(c.lower(),end=" ")
    else:
        print(c,end=" ")
'''
##################################################################
'''
d=input("input data")
digit=0
character=0

for i in d:
    if i.isalpha():
        character+=1
    elif i.isnumeric():
        digit+=1

print(digit)
print(character)
print("#"*100)
'''
###################################################################
for row in range(0,7):
    for column in range(0,7):
        if (row==0 or row==6) and (1 < column < 5):
            print("*",end=" ")
        elif (0 < row <= 5) and (column==1 or column==5):
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()

###############################
''' num = int(input("Enter the number: "))
count=1
while count<=num:
    count_sum = count + i
    print(count,end=" ")
    count+=1

print()
print(count_sum)
'''
#################################################
'''
num = int(input("Enter the number: "))
count=num
while count!=0:
    #count_sum = count + i
    print(count,end=" ")
    count-=1
print()

print("&"*100)
'''
###################################################
import string

print("Alphabet from a-z: ")
for letter in string.ascii_lowercase:
    print(letter,end=" ")

print("\nAlphabet from A-Z: ")
for letter in string.ascii_uppercase:
    print(letter,end=" ")

print()

#########################################################
print("&"*100)

print("Alphabet for a-z: ")
for i in range(26):
    print(chr(97+i),end=" ")

print("\nAlphabet for A-Z: ")
for i in range(26):
    print(chr(65+i),end=" ")