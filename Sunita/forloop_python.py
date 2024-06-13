#1). Write a  Python loops program to find those numbers which are divisible by 7
# and multiple of 5, between 1500 and 2700 (both included).

for i in range(1500,2701):
    if i%7==0 and i%5==0:
        print(i," is divisible by 5 and 7")
    #else:
     #   print(i," is not divisible by 5 and 7")

"""
2).  Python Loops program to construct the following pattern, using a nested for loops.
Output :
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(4,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

"""
4). Python Loops program to count the number of even and odd numbers from a series of numbers using  python.
Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
Output :
Number of even numbers: 4
Number of odd numbers: 5
"""

print("*"*50)
i=(1, 2, 3, 4, 5, 6, 7, 8, 9)
even=0
odd=0
if i%2==0:
    even +=1
    print(i, "Even numbers")
else:
    odd +=1
    print(i, "odd numbers")

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0

for val in numbers:
    if val % 2 == 0:
        even += 1
    else:
        odd += 1

print("Number of even numbers: ", even)
print("Number of odd numbers: ", odd)