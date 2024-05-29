'''
if condition:
 else:
 code
''' '''
    

''
##Python program to check if given number is divisible by 3 or not##
a=6
if a%3 == 0:
 print("Number is divisible by 3")
else:
 print("Number is not divisible")

####
a=7
if a%3 == 0:
 print("Number is divisible by 3")
else:
 print("Number is not divisible")
'''

###How to get a number##
''''
num=int(input("Enter the value"))
if num%3 == 0:
 print("Number is divisible by 3")
else:
 print("Number is not divisible")
 '''
'''
#####if else program to assign grade as per total mark####
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marks


mark=int(input("Enter the mark"))
if mark<40:
    print("Fail")
elif mark>=40 and mark<50:
    print("Grade C")
elif mark>=50 and mark<60:
    print("Grade B")
elif mark >= 60 and mark < 70:
    print("Grade A")
elif mark >= 70 and mark < 80:
    print("Grade A+")
elif mark >= 80 and mark < 90:
    print("Grade A++")
elif mark >= 90 and mark <= 100:
    print("Grade Excellent")
else:
    print("Invalid Mark")
'''
##### Program to check if the number is divisible by 3 and 5#####
'''
num=int(input("Enter the number"))
if num%3==0 and num%5==0:
    print("Number is divisible by 3 and 5")
else:
    print("Number is not divisble by 3 and 5")
'''
#####Program to print the square of the number###
'''
num=int(input("Enter the number"))
if num%11==0:
    print("Square of the number is", num**2)
else:
    print("number is not divisible by 11")
    '''
####### program to check  given number is odd or even######

'''
num=int(input("Enter the number"))
if num%2==0:
    print("Even number")
else:
    print("Odd number")
'''

#####Check authentication of the user name and password########
'''
num1=str(input("Enter the user name:"))
num2=str(input("Enter the password:"))
if num1==num2:
    print("Valid")
else:
    print("Invalid")
    '''

####validate user_id in the list of user_ids###
'''
list_a=[4,7,8,9,34,89,23]
a=int(input("Enter the user id"))
if a in list_a:
    print("User id available")
else:
    print("User id is not available")
    '''
####### program to print a square or cube if the given number is divided by 2 or 3##
'''
num = int(input("Enter the number:"))
if num%2 == 0:
 print("Square of the given number is:",num**2)
elif num%3 == 0:
 print("Cube", num**3)
 '''
#######nested If else program to describe the interview process######
######Program to check whether a person eligible to vote######
'''
age=int(input("Enter the Age"))
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
'''
####### Check whether a student has passed the exam.#####
'''
mark=int(input("Enter the Mark: "))
if mark>=35:
    print("Pass")
else:
    print("Fail")
'''
###Check whether the given number is positive or not#####

num=int(input("Enter the number:"))
if num>=0:
    print("Number is positive")
else:
    print("Number is negative")



