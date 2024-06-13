#1). Write a  Python loops program to find those numbers which are divisible by 7 and multiple of 5,
# between 1500 and 2700 (both included).Input1:1500Input2:2700
"""
for i in range (1500,2700+1):
    if i % 7 == 0 and i % 5 ==0:
        print(i)
        Output :
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
"""
#2).  Python Loops program to construct the following pattern, using a nested for loops.

for i in range(5):
    for j in range (i):
      print("*",end="")
    print()
for i in range(5,-1,-1):
    for j in range (i):
      print("*",end="")
    print()

"""   
#55). Write a program to construct the following pattern, using a nested for loop in Python.
Output :
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
"""
for i in range(1,6):
    for j in range(i):
        print(i, end="")
    print()
"""
#56). Write a program to get the Fibonacci series between 0 to 10 using  Python Loops.Output = 0 1 1 2 3 5 8 13 21 34 55
#0,1,1,2,3,5,8,13
"""
count = 0
num1, num2 = 0, 1
print("Sequence is: ", end=" ")
while count < 11:
    print(num1, end=" ")
    n2 = num1 + num2
    num1 = num2
    num2 = n2

    count += 1
"""
#41).  Python loops program to print the pattern T using Python Loops.
"""
for i in range(2):
    for j in range(9):
      print("*", end="")
    print()
for i in range(5):
    for j in range(9):
        if j>2 and j<6:
            print("*",end="")
        else:
            print(" ",end="")
    print()
"""
#42).  Write a program to print number patterns using  Python Loops.
"""
n=1
for i in range(1,6):
    for j in range(i):
        print(n,end=" ")
        n +=1
    print()
"""
#43). Write a program to print the pattern A using Python Loops.
"""
    Output :
      *  *  *
    * * * * * *
    * *     * *
    * *     * *
    * * * * * *
    * * * * * *
    * *     * *
    * *     * *
    * *     * *
"""
"""
for i in range(1):
    for j in range (6):
        if j>0 and j<4:
            print("*" ,end="  ")
        else:
            print(" ",end=" ")
    print()
for i in range(1):
    for j in range (6):
        print("*" ,end=" ")
    print()
for i in range(2):
    for j in range (6):
        if j>1 and j<4:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
for i in range(2):
    for j in range (6):
        print("*" ,end=" ")
    print()
for i in range(3):
    for j in range (6):
        if j>1 and j<4:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
"""
#44). Write a program to print the pyramid structure using  Python Loops.
"""
 
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

n1=4
n2=6
for i in range(1,6):
    for j in range (1,10):
        if j>n1 and j<n2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    n1=n1-1
    n2=n2+1
    print()
"""
#46). Write a program to count the total numbers of odd numbers between 1-100 using Python Loops.
"""
count = 0
for i in range(1,101):
    if i % 2 == 0 :
        count += 1
    else:
        continue
print(count)
"""
#57). Write a program to check the validity of password input by users using  Python Loops.
#60). Write a program to print a table of 5 using for loop using  Python Loops.

