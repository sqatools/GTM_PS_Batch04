#for loop
#can assign 3 parameters: initial value,end value and difference (difference between each values)
"""
for i in range(1,26,2):
  print (i ,end=" ")    #1,3,5,7,9,11,13,15,17,19,21,23,25,

print()
for n in range(1,6):
    print(n,end="")
print()
for n1 in range(5):
    print(n1,end="")
print()
for n2 in range(10,1,-2):
    print(n2,end="")
print()

n = 5
for i in range(1, 11):
    print(i , "*" , n , ":", (i*n))


#1 Write a  Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
#Input1:1500
#Input2:2700


for num in range(1500,2701):
    if num%7==0 and num%5==0:
        print(num ,end=" ")


#2construct the pattern

for i in range(6):
    print(i*"*")
for i in range(4,-1,-1):  #Use for loop with range function but in reverse order to print the last 4 rows of the pattern
    print(i*"*")

#3Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.

for i in range(0,7):
    if i!=3 and i!=6:
        print(i,end=" ")


#4Write a program that iterates the integers from 1 to 30 using  python. For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
#For numbers that are multiples of both three and five print “FizzBuzz”.

for i in range(1,31):
    if i%3==0 and i%5==0:
        print(i,"fizzbuzz")
    elif i%3==0:
        print(i,"fizz")
    elif i%5==0:
        print(i, "buzz")



#5Loops program to print all even numbers between 1 to 100 in python.

for num in range(1,101):
    if num%2==0:
        print(num ,end=",")


#Python Loops program to print all natural numbers from 1 to n

num = int(input("Enter value for num : "))
for i in range(1,num):
    print(i)

#6) Python Loops program to print all even numbers between 1 to 100 in python.

for i in range(1,101):
    if i%2==0:
        print(i ,end=" ,")

"""
#7)odd numbers

for i in range(1,101):
    if ((i%2)!=0):
        print(i , end=",")


