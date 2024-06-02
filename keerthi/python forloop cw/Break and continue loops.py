# while loop

num1 = 1
while num1 <=10:
    print(num1)
    num1+=1

print('_'*50)

# Infinite Loop
'''
while True:
    num1 += 1
    #num1 = num1 + 1
    print(num1)
'''

#continue statement
a=1
while a<=10:
    if a > 5 and a < 10:
        a+=1
        continue
    print(a)
    a+=1

print("*"*50)
num2=1
while num2<=10:
    if num2>3 and num2<10:
        num2+=1
        continue
    print(num2, end=" ")
    num2+=1 #1 2 3 10

print()

#break statement
b=1
while True:
    print(b)
    b += 1
    if b == 100:
        break
print("*"*50)

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

for n in range(1,100):
    prime=True
    for i in range(2,n):
        if n%i==0:
          prime = False
          break
    else:
        continue
    if prime:
        print(n,end=' ')
    else:
        pass


for i in range(1,6):
    for j in range(i):
        print(j,end=' ')
    print()

for i in range(6,0,-1):
    for j in range(i):
        print(j,end=' ')
    print()


temp=1
for i in range(1,6):
    for j in range(i):
        print(temp, end=" ")
        temp += 1
    print()

for i in range(6,0-1):
    for j in range(i):
        print(temp,end=" ")
        temp+=1
        print()
