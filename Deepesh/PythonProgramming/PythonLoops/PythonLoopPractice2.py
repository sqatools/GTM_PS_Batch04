
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
    print() #---------------------------doubt

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
