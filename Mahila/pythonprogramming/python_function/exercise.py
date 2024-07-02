#Python function program to add two numbers

# def add(a,b):
#     print("addition values :",a+b)
#
# a= int(input("Enter value for a :"))
# b= int(input("Enter value for b :"))
# add(a,b)

#############################################################
#Python function program to print the input string 10 times.

# def String(str1):
#     print(str1*10)
#
# strg = input("Enter a string: ")
#
# String(strg)

#Python function program to print a table of a number

# def table(num):
#     value = 0
#     for i in range (1,11,1):
#         value = i * num
#         print(i, "*", num, "=", value)
#
# table(6)

#Python function program to find the maximum of three numbers.

#Input: 17, 21, -9
#Output: 21

# def max(a,b,c):
#     if a>b:
#         if a>c:
#             print(f"{a} is greatest number")
#     elif b>a:
#         if b>c:
#             print(f"{b} is the greatest number")
#     else:
#         print(f"{c} is the greatest number")
# max(7,21,-9)

#Python function program to find the sum of all the numbers in a list.
#Input : [6,9,4,5,3]
#Output: 27

# def sum(list1):
#     total=0
#     for val in list1:
#         total = total + val
#     print(total)
#
# sum([6,9,4,5,3])

#Python function program to multiply all the numbers in a list.
#Input : [-8, 6, 1, 9, 2]
#Output: -864

# def mul(list2):
#     product = 1
#     for val in list2:
#         product = product * val
#     print(product)
#
# list2 = [-8, 6, 1, 9, 2]
# mul(list2)

#Python function program to reverse a string.
#Input: Python1234
#Output: 4321nohtyp

# def rev(str1):
#     a = str1[::-1]
#     print(a)
# str1 = "Python1234"
# rev(str1)

#Python function program to check whether a number is in a given range.
#Input : num = 7, range = 2 to 20
#Output: 7 is in the range

# def check(num):
#     if num in range(2, 20):
#         print("True")
#     else:
#         print("False")
# check(22)


#Python function program that takes a list and returns a new list with unique elements of the first list.
#Input : [2, 2, 3, 1, 4, 4, 4, 4, 4, 6]
#Output : [2, 3, 1, 4, 6 ]

# def unique(list1):
#     set1 = set(list1)
#     list2 =list(set1)
#     print(list2)
#
# unique([2, 2, 3, 1, 4, 4, 4, 4, 4, 6])

#Python function program that take a number as a parameter and checks whether the number is prime or not.
#Input : 7
#Output : True

# def prime(n):
#     count=0
#     for val in range(1,n):
#         if n%val==0:
#             count += 1
#     if count>1:
#         print(f"{n} is not a prime number")
#     else:
#         print(f"{n} is a prime number")
#
# prime(17)

#Python function program to find the even numbers from a given list.
#Input : [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Output : [2, 4, 6, 8]

# def even(list):
#     output = []
#     for val in list:
#         if val%2==0:
#             output.append(val)
#     print(output)
# even([1, 2, 3, 4, 5, 6, 7, 8, 9])

#  Python function program to create and print a list where the values are squares of numbers between 1 to 10.
# Input: 1 to 10
# Output: 1, 4, 9, 16, 25, 36, 49, 64, 81

# def squ():
#     for val in range(1,10):
#         print(val**2, end = ",")
#
# squ()

#Python function program to find the HCF of two numbers
#
# def hcf(num1,num2):
#     if num1 > num2:
#         smaller = num2
#     else:
#         smaller = num1
#
#     for i in range(1,smaller+1):
#         if ((num1%i==0) and (num2%i==0)):
#             hcf = i
#     print(hcf)
#
# hcf(24,54)

# Python function program to get the factorial of a given number.
# Input: 5
# Output: 120

def fact(n):
    factorial=1
    for val in range(n,0,-1):
        factorial = factorial *val
    print(factorial)
fact(6)


