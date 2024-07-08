#3). Python function program to print a table of a given number
"""

def  table_fn(*i):
   for val in i:
       print(val)
       a=n*val
       print(n,"*",val,"=",a)
n=input("enter the number")
table_fn(1,2,3,4,5,6,7,8,9,10)
"""
#4). Python function program to find the maximum of three numbers.
"""

def maxi(a,b,c):
    if a>b and a>c:
        print("max is :",a)
    elif b>a and b>c:
        print("max is :", b)
    else:
        print("max is :", c)
maxi(-17,-3,-9)
"""
#5). Python function program to find the sum of all the numbers in a list. Input : [6,9,4,5,3] Output: 27
"""
def summ(list1):
    mul =1
    for i in list1:
        mul=mul*i

    print(mul)

l=[-8, 6, 1, 9, 2]
summ(l)
"""
#7). Python function program to reverse a string.

#Output: 4321nohtyp
#print(Input[::-1])
def reverse(input):
    for i in  input:
        print(i, end="")


Input = "Python1234"
reverse(Input)