##program to check given number is divided by 3 or not.

"""
num1=21

if num1%3==0:
    print("number is divisible by 3")
else:
    print("number is not divisible by 3")

print("_"*40)

##If else program to assign grades as per total marks.
mark=55

if mark < 40:
    print("student is failed")
elif 40 < mark <= 50:
    print("student is passed in C grade")
elif 50 < mark <= 60:
    print("student is passed in B grade")
elif 60 < mark <= 70:
    print("student is passed in A grade")
elif 70 < mark <= 80:
    print("student is passed in A+ grade")
elif 80 < mark <= 90:
    print("student is passed in A++ grade")
elif 90 < mark <= 100:
    print("student is passed in Excellent grade")
else :
    print ("Invalid marks")

print("_"*40)

### program to check the given number divided by 3 and 5.
num2=30
if num2%3 and num2%5 :
    print ("number is divisible by 3 and 5")
else:
    print("number is not divisible by 3 and 5")

print("_"*40)

##Python program to print the square of the number if it is divided by 11.

num3=int(input("Enter a number: "))
if num3%11 == 0:

    print(num3**2)
else:
    print("number is not divisible by 11")

print("_"*40)

##Python program to check given number is odd or even

num4=int(input("Enter the number: "))
if num4 % 2 == 0:
    print("number is even")
else:
    print("number is odd ")


#Python program to check authentication with the given username and password.
print("_"*40)

name=input("enter name : ")
password=input("password : ")
if name==password:
    print("it is  valid ")
else :
    print("it is not valid")
"""
"""
###Python program to validate user_id in the list of user_ids.
print("_"*40)

id_list=[1,2,3,4,5,6]
id_=input("enter id number :")
if int(id_) in id_list:
    print("valid id")
else :
    print("invalid id")

##program to print a square or cube if the given number is divided by 2 or 3 respectively

"""
"""
num4=int(input("enter a number : "))
if num4%2 == 0 :
    print("square :" , num4**2)
elif num4%3 == 0 :
    print ("cube : "  , num4**3)

"""
"""

####program to determine whether a given number is available in the list of numbers or not.

list1=[11,22,33,43,57,69,]
num = int(input("Enter a number: "))
if num==list1 :
    print("number is in the list")
else :
####Python program to describe the interview process.

"""
"""
round1="pass"
round2="pass"
round3="pass"
if round1=="pass" :
    print("congrats you cleared  round1")
    if round2 == "pass":
        print("congrats you cleared round 2")
        if round3 == "pass":
            print("congrats you cleared the interview , our HR will call you")
        else:
            print("you didn't clear the third round HR will get back to you")
    else:
        print("you didn't clear the second round hard luck next time")
else:
    print("you didn't clear the first round hard luck next time")

"""
# # check number is palindrome or not
# num1 = 232
# num2 = str(num1)
# if num1 == int(num2 [::-1]):
#     print("its a palindormic number")
# else :
#     print("its not a palindromic number")
#
# # check number is palindrome or not
#
# str1= "kayak"
# str2=str1[::-1]
# if str1==str2 :
#     print("its a palindromic word")
# else :
#     print ("its not a palindromic word ")

#program to get all the numbers divided by 3 from 1 to 30.

# for i in range (1,31):
# if i%3 == 0:
#     print(i, end="")

#program to check given number is a prime number or not
"""
fib=[0,1,2,3,4,5,6,7,8,9,10]
num=int (input ("enter a number: "))
if num in fib :
    print("it is a part of series  ")
else :
    print ("its not a part of series ")

"""

#given number is in the list or not

list1=[0,1,2,3,4,5]
num =int(input ("enter a number ; "))
if num in list1:
    print("its valid")
else:
    print("its not valid")

#programm to check the largest number

num1 =int(input("enter 1st number : "))
num2 =int(input("enter 2nd number : "))
num3 =int(input("enter 3rd number : "))
if num1>num2:
    if num1>num3:
        print("num1 is the greatest number")
    else:
        print("num3 is the greatest number")
        if num2>num3:
            print("num2 is the greatest number")
        else :
            print("num3 is the greatest number")













