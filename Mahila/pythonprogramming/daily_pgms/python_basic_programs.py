# #40). Python program to perform mathematical operations on two numbers
#
# a = float(input("Enter first number : "))
# b = float(input("Enter second number : "))
# operation = input("Enter operation of your choice : ")
#
# if operation == "+":
#     print(a+b)
# elif operation == "-":
#     print(a-b)
# elif operation == "*":
#     print(a*b)
# elif operation == "/":
#     print(a/b)
# else:
#     print("Invalid operation entered")

#-----------------------------------------------------------------------------------
#
# 39). Python program to calculate the volume of a sphere.
# Formula = (4/3*pi*r^2)
# r = radius
# pi = 3

# r = float(input("Enter the radius of sphere :"))
# pi = 3.14
#
# volume = 4/3*pi*(r**2)
# print(volume)
#-------------------------------------------------------------------------------------
#38) Program to find the square root of a number
# import math
#
# num1 = 9
# num2 = math.sqrt(num1)
# print(num2)

#---------------------------------------------------------------------------------
#37) Program to fin LCM of two number

# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
#
# if num1 > num2:
#        greater = num1
# else:
#     greater = num2
#
# #greater=max(num1,num2)
#
# while(True):
#     if((greater % num1 == 0) and (greater % num2 == 0)):
#         lcm = greater
#         break
#     else:
#         greater += 1
#
# print(f"L.C.M of {num1} and {num2}: {lcm}")

#using function

# def lcm(a,b):
#     greatest = max(a,b)
#     while(True):
#         if ((greatest%a==0) and (greatest%b==0)):
#             lcm = greatest
#             break
#         else:
#             greatest +=1
#     print(lcm)
# a=int(input("Enter a num1: "))
# b=int(input("Enter a num2: "))
# lcm(a,b)
#----------------------------------------------------------------------------


