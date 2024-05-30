'''
#1). Write a  Python loops program to find those numbers which are divisible
#by 7 and multiple of 5, between 1500 and 2700 (both included).

for i in range(1500,2701):
    if i%7==0 and i%5==0:
        print(i,end =' ')


#2). Python Loops program to construct the following pattern, using a nested for loops.

#3). Python Loops program that will add the word from the user to the empty string using python
a = input("enter the string")
for i in range(a, end=' '):
    print(i)
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

#6). Write a program to get the Fibonacci series between 0 to 20 using python.