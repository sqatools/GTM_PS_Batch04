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


for i in range (10): #1
    for j in (i-1):
    #i = i + (n-1)
     print(j)
    #n +=1