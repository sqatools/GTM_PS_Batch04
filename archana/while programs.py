num1= 10
while num1<=10:
    num1+=1
    print(num1)

print("-"*50)

print("-"*50)
a=1
while a<=10:
    if a>4 and a<7:
        a+=1
        continue
        a+=1
print(a)

print("-"*50)
n=11
prime= True
for i in range(2,n):
    print(i)
    if n%i==0:
        prime= False
        break
    else:
        continue

    if prime:
        print("this is a prime")
    else:
        print("this is not prime")

