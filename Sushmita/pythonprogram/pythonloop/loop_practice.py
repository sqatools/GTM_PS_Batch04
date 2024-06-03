#while loop
num=1
while num<=10:
    print(num,end=' ')
    num=num+1

print(" ")

print('_'*50)

#continue statement

a=1
while a<=10:
    if a>4 and a<7:
        a=a+1
        continue
    print(a)
    a=a+1

print('_'*50)

#Break statement

b=1
while True :
    print(b)
    b=b+1
    if b==100:
        break


print('_'*50)

#find out given number is prime or not

n=6
prime=True
for i in range(2,n//2):
    print(i)
    if n%i==0:
        prime=False
        break
    else :
        continue

if prime :
    print(f'{n} giveen value is prime number')
else:
    print(f'{n} giveen value not a prime number')



'''
n = 6
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
'''
print('_'*50)

for n in range(1,100):
    prime=True
    for i in range(2,n):
        if n%i==0:
            prime=False
            break
        else :
             continue
    if prime:
        print(n,end=' ')
    else:
        pass
print()

print('_'*50)

for i in range(1,5):
    for j in range(i):
        print('*',end=' ')
    print()
print('_'*50)

for i in range(6,-0,-1):
    for j in range(i):
        print(j,end=' ')
    print( )

print('_'*50)

temp=1
for i in range(1,6):
    for j in range(i):
        print(temp,end=' ')
        temp=temp+1
    print( )

for i in range(6,0,-1):
    for j in range(i):
        print(temp,end=' ')
        temp=temp+1
    print()

# capital case ascii range 65-90, small case : 97- 122
Asci_value=65
for i in range(1,6):
    for j in range(i):
        print(chr(Asci_value),end=' ')
        Asci_value+=1
    print( )

asci_value=97
for i in range(6,0,-1):
    for j in range(i):
        print(chr(asci_value),end=' ')
        asci_value=asci_value+1
    print( )

print(ord("C")) # 67
print(ord("c")) # 99
