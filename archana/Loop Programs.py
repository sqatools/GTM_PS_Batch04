'''
#1). Write a  Python loops program to find those numbers which are divisible
#by 7 and multiple of 5, between 1500 and 2700 (both included).

for i in range(1500,2701):
    if i%7==0 and i%5==0:
        print(i,end =' ')


#2). Python Loops program to construct the following pattern, using a nested for loops.

#3). Python Loops program that will add the word from the user to
the empty string using python
a = input("enter the string")
for i in range(a, end=' '):
    print(i)
'''
'''
#4). Python Loops program to count the number of even and odd
#numbers from a series of numbers using  python.
numbers = (1,2,3,4,5,6,7,8,9)
even = 0
odd =0
for i in numbers:
    if i%2==0:
        even +=1
    else:
        odd +=1
print("number of even numbers :",even)
print("number of odd numbers:",odd)

#5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
for i in range(0,11):
    if i! =3 or i ! =6:
        print(i,end =" ")
'''
'''
#6). Write a program to get the Fibonacci series between 0 to 20 using python.
num1=0
num2=1
count=0

while count< 20:
    print(num1,end=' ')
    n2= num1+num2
    num1= num2
    num2=n2
    count=count+1
'''
'''
#7). Write a program that iterates the integers from 1 to 30 using
#python. For multiples of three print “Fizz” instead of the number and
#for multiples of five print “Buzz”.
#For numbers that are multiples of both three and five print “FizzBuzz”.
for i in range(1,31):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3==0 and i % 5==0:
        print("FizzBuzz")
'''
'''
#11). Python Loops program to print all natural numbers from
#1 to n using a while loop in  python.
#1,2,3,4,5,6,...

n = int(input("enter the number"))
count= 1
while count<=n:
    print(count,end=" ")
    count+=1
'''
'''
#12). Write a program to
#print all natural numbers in reverse (from n to 1) using a while loop in  python.
#n............6.5.4.3.2.1

n= int(input("enter the value"))
count = n
while (count != 0):
    print(count,end=" ")
    count-=1
'''
'''
#14)Python Loops program to print all even numbers between 1 to 100 in python.
#2,4,6,8,..100

for i in range(1,101):
    if i%2==0:
        print(i)
    else:
        pass
'''
'''
#15)Python Loops program to print all odd numbers between 1 to 100 using python.
#1,3,5,7,.......99

for i in range(1,101):
    if i%2!=0:
        print(i,end=' ')
   '''
'''
#16). Python Loops program to find the sum of all natural numbers between 1 to n using python.
#1,2,3,4,...n

n= int(input("enter the value"))
count =0
for i in range(1,n+1):
    count= count+i
print(count)
'''
'''
#17). Python program to find the sum of all even numbers between 1 to n using  python.
#2,4,6,8.......n

n= int(input("enter the value "))
count = 0
for i in range(1,n+1):
    if i%2==0:
        count=count+i
print(count)
'''
'''
#18). Python Loops program to find the sum of all odd numbers between 1 to n using python.
n= int(input("enter the value "))
count = 0
for i in range(1,n+1):
    if i%2 != 0:
        count=count+i
print(count)
'''
'''
#19)Write a program to count the number of digits in a number using python.
#1 2 3 4 5
count = 0
n =int(input("enter the value"))
for i in range(1,n+1):
    count= count+i
print(count)
'''
'''
#length of string
num= '123456789sddddddsdddddsds////........'
print(len(num))
'''
'''
#20)Write a program to find the first and last digits of a number using python.

n = 12345
b= str(n)
for i in range(len(b)):
    if i == 0:
        print("first digit",b[i])
    elif i == len(b)-1:
        print("last digit",b[i])
'''
'''
n = 12347
b= str(n)
c= len(b)
for i in range(c):
    if i == 0:
        print("first digit",b[i])
    elif i == c-1:
        print("last digit",b[i])
'''
'''
#21). Write a program to find the sum of the first and last digits of a number using python.

n= 123456
a = str(n)
b = len(a)
total = 0
for i in range(b):
    if i==0:
        total += int(a[i])
    elif i==b-1:
        total+=int(a[i])

print("sum of first and last digits",total)
'''
'''doubt
n= "abcde"
a = str(n)
b = len(a)
total = 0
for i in range(b):
    if i==0:
        total += a[i]
    elif i==b-1:
        total+= a[i]

print("sum of first and last digits",total)
'''
'''
#22). Write a program to calculate the sum of digits of a number using  python.

n= 12345 doubt
a= str(n)
total =0
'''
#24). Python loops program to enter a number and print its reverse using python.

n = 12345
a = str(12345)
for i in range(len(a),-1,1):
    print(a[i])



