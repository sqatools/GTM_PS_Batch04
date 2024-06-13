# Write a  Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
count=0
for i in range(1500,2700+1):
    if i%7==0 and i%5==0:
        count+=1

        print(i,end=" , ")
       # print(count,end=" ")

print(count)

#  Python Loops program to construct the following pattern, using a nested for loops.

for i in range(6):
    print(i*"*")
#for i in range(4,-1,-1):
   # print(i*"*")
for i in range(4, 0,-1):
    print(i*"*")

# Python Loops program that will add the word from the user to the empty string using  python.

str1="python"
k=''
for i in range(len(str1)):
    k+=str1[i]

print(k)

# Python Loops program to count the number of even and odd numbers from a series of numbers using  python.

l1=[1,2,3,4,5,6,7,8,9]
even=0
odd=0
for i in l1:
    if i%2==0:
        even+=1

    else:
        odd+=1


print(even)
print(odd)


# Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.

l2=[1,2,3,4,5,6]
k1=0
for i in l2:
    if i%3==0:
        k1+=1
        print(k1)

for i in range(11):
    if i!=3 and i!=6:
        print(i)

# Write a program to get the Fibonacci series between 0 to 20 using python.
# Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181

num1=0
num2=1
count=0

print("The Sequence is: ",end=" ")
while count<20:
    print(num1,end=" ")
    n3=num1+num2
    num1=num2
    num2=n3
    count+=1

''' 
Write a program that iterates the integers from 1 to 30 using  python. For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
For numbers that are multiples of both three and five print “FizzBuzz”. 
'''

for i in range(1,31):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")

# Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using  python.

d="SUBBU"

for i in d:
    if i.isupper():
        print(i.lower(),end=" ")
    else:
        print(i,end=" ")
print()
# Python loops program that accepts a string and calculates the number of digits and letters using python.

word ="python1234"
digit=0
character=0
for i in word:
    if i.isalpha():
        character+=1
    elif i.isnumeric():
        digit+=1

print("Digit",digit)
print("Character",character)


for i in range(1,101):
    if i%i==1:
        i+=1
        pass
print(i)


##################################################################

# while loop

num1 = 1
while num1 <=10:
    print(num1)
    num1 += 1

print("_"*50)

# Infinite Loop
"""
while True:
    num1 += 1
    #num1 = num1 + 1
    print(num1)
"""




# continue statement
a = 1
while a <= 10: # a = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    if a > 4 and a < 7: # 10 > 4 and 10 < 7
        a += 1 # a = 6, 7
        continue
    print(a) # 1, 2, 3, 4, 7, 8, 9, 10
    a += 1 # a= 2, 3, 4, 5, 8, 9, 10, 11


print("_"*50)
"""
# Break Statement
b = 1
while True:
    print(b)
    b += 1
    if b == 100000:
        break
"""
##############################################
print("_"*50)
# write a python program to find out given value is prime number or not.
n = 101
prime = True
for i in range(2, n//2):
    print(i)
    if n%i == 0:
        prime= False
        break
    else:
        continue

if prime:
    print("This is prime number", n)
else:
    print("This is not prime number", n)


print("_"*40)
# write a program to get list prime numbers from 1 to 100

for n in range(1, 100):
    prime = True
    for i in range(2, n):
        if n%i == 0:
            prime = False
            break
        else:
            continue
    if prime:
        print(n, end=' ')
    else:
        pass

print()
############################################

"""
*
* * 
* * *
* * * *
* * * * *

* * * * *
* * * *
* * *
* *
*

"""

for i in range(1, 6):
    for j in range(i):
        print(j, end=" ")
    print()

for i in range(6, 0, -1):
    for j in range(i):
        print(j, end=" ")
    print()


"""
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 21 
22 23 24 25 26 
27 28 29 30 
31 32 33 
34 35 
36 


"""
temp = 1
for i in range(1, 6):
    for j in range(i):
        print(temp, end=" ")
        temp += 1
    print()

for i in range(6, 0, -1):
    for j in range(i):
        print(temp, end=" ")
        temp += 1
    print()



# capital case ascii range 65-90, small case : 97- 122
"""
A 
B C 
D E F 
G H I J 
K L M N O 
P Q R S T U 
V W X Y Z 
[ \ ] ^ 
_ ` a 
b c 
d 


"""

ascii_value = 65
for i in range(1, 6):
    for j in range(i):
        print(chr(ascii_value), end=" ")
        ascii_value += 1
    print()

for i in range(6, 0, -1):
    for j in range(i):
        print(chr(ascii_value), end=" ")
        ascii_value += 1
    print()



print(ord("C")) # 67
print(ord("c")) # 99
