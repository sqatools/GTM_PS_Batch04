"""
if <condition>:
    code
else:
    code
"""
"""
a = 60
b = 60
print(a == b)
if a == b:
    print("A and B both have same value")
else:
    print("A and B both have different value")


# check given number is divisible by 3 or not
num1 = 51

if num1%3 == 0:
    print("num1 is divisible by three")
else:
    print("num1 is not divisible by three")

print("_"*50)

# program to check given number is even or odd
print("_"*50)
input_value = input("Please enter the value :")
print(input_value, type(input_value))

if int(input_value)%2 == 0:
    print("This is even number")
else :
    print("This is odd number.")


# program to check the given number is divisible by 3 and 7
print("_"*40)
n1 = 20
if n1%3 == 0 and n1%7 == 0:
    print("n1 is divisible by three and seven")
else:
    print("n1 is not divisible by three and seven")
"""
"""
AND condition
cond1 and cond2

TRUE and False : False
False and True : False
False and False : False
True and True : True

OR condition
cond1 or cond2

True or False : True
False or True : True
True or True : True
False or False : False

> : greater than operator
< : less than operator
>= : greater than equal to
<= : less than equal to 
!= : not equal to
== : equal to operator
in contains operator:
"""
""""""

print("_"*50)
num = 22
if num%3 == 0 and num%7 == 0 or num%10 == 0:
    print("number can be divisible by 3 and 7 or 10")
else:
    print("number is not divisible by given values")

########## If-elif-else ###########
"""
if cond1:
    code
elif cond2:
    code
elif cond:
    code
else:
    code
"""

# write a python program to find the greater value among three variables
print("_"*50)
"""
a = 113
b = 500
c = 500

if a > b and a > c:
    print("a has greater value :", a)
elif b > a and b > c:
    print("b has greater value :", b)
elif c > a and c > b:
    print("c has greater value :", c)
else:
    print("No one has greater value")
"""
"""
a = 70
b = 50
c = 77
if a > b or a > c:
    print("a has greater value :", a)
elif b > a or b > c:
    print("b has greater value :", b)
elif c > a or c > b:
    print("c has greater value :", c)
else:
    print("No one has greater value")
"""

####
# write a python to decide the grade as per marks percentage of the student
marks = 105

if marks > 100:
    print("Marks can not be more than 100")
elif 30 < marks <= 40:
    print("Passed with C grade")
elif 40 < marks <= 50:
    print("Passed with B grade")
elif 50 < marks <= 60:
    print("Passed with A grade")
elif 60 < marks <= 80:
    print("Passed with A+ grade")
elif 80 < marks <= 90:
    print("Passed with A++ grade")
elif 90 < marks <= 100:
    print("Passed with Excellent grade")
else:
    print("student failed in examination")

################### Nested If condition ##########

"""
if cond1:
   code
   if cond2:
       code
   else:
       code
else:
   code
"""
print("_"*50)
# write a python program to define the nested if condition

round1 = "pass"
round2 = "pass"
round3 = "pass"

if round1 == "pass":
    print("Congrats first round is cleared.")
    if round2 == "pass":
        print("Congrats 2nd round is cleared.")
        if round3 == "pass":
            print("Congrats for your selection, here is your offer letter")
        else:
            print("Failed in third round, hard luck try next time")
    else:
        print("Failed in second round, try next time")
else:
    print("Failed in first round, try next time")

#####################################
print("_"*50)
list1= [5, 7, 3, 8, 22]
num = 8
if num in list1:
    print("number is available in the list")
else:
    print("number is not available in the list")

str1 = "We are Learning Python Programming"

if "python" in str1:
    print("Python is available in str1")
else:
    print("Python is not available in str1")


print("_"*50)
# one single line if condition
n1 = 51
result = "Even" if n1%2 == 0 else "Odd"
print("result is:", result)

n2 = 61

result = True if n2 in [3, 6, 22, 60, 12] else False
print("result :", result)
""""""
# 1 program to check given number is divided by 3 or not.#
print("_"*50)

num = 30
if num % 3 == 0:
    print("number is divisible by 3")
else:
    print("number is Not divisible by 3")

# 2 Python program to check the given number divided by 3 and 5.#
print("_"*50)

num = 15
if num % 3 == 0 and num % 5 == 0:
    print("number is divisible by 3 and 5")
else:
    print("number is Not divisible by 3 and 5")

# 3 Python program to check given number is odd or even.#

print("_"*50)

num = 15
if num % 3 == 0 or num % 2 == 0:
    print("Given number is Odd ")
else:
    print("Given number is Even ")

# 4 Python program to check authentication with the given username and password.#

print("_"*50)

str1 = "Chetan"
str2 = "Chetan@123"
if str1 == "Chetan" and str2 == "Chetan@123":
    print("authentication is successful")
else:
    print("Invalid user or Password")

# 5 Python program to validate user_id in the list of user_ids.#

print("_"*50)

userid_list = [1, 2, 3, 12, 34, 16]
ide = 12
if ide in userid_list:
    print("Id is present in List")

else:
    print("Id is not present in List")

# 6 Python program to check any person eligible to vote or not#
print("="*50)

Age = 16

if Age >= 18:
    print("Eligible for Voting")
else:
    print("Not Eligible for Voting")

# 7 Python program to Check greater among three Number#

print("="*50)

num1 = 100
num2 = 67
num3 = 89

if num1 > num2 and num1 > num3:
    print("num1 is Greater")
elif num2 > num1 and num2 > num3:
    print("num2 is Greater")
elif num3 > num1 and num3 > num2:
    print("num3 is Greater")
else:
    print("Id is not present in List")

# 8 Python Program to Check whether the given number is negative or not#
print("="*50)
Number = -23

if Number < 0:
    print("Given number is Negative")
else:
    print("Given number is not Negative")
"""
9 Python program to check whether a student has passed the exam 
 If marks are greater than 35 students have passed the exam
"""
print("="*50)

Student_Marks = 50

if Student_Marks > 35:

    print("students have passed the exam")
else:
    print("students have failed the exam")

# 10 Program to check whether the number is Int#
print("="*50)
Digit = 12
if type(Digit) == int:
     print("Digit is Integer")
else:
    print("Digit is Not an Integer")

# 11 Python program to assign grades as per total marks #
print("="*50)
Mark = 1011
if Mark < 30:
    print("failed")
elif 30 < Mark < 40:
    print("Garde C")
elif 40 < Mark < 50:
    print("Garde B")
elif 50 < Mark < 60:
    print("Garde B +")
elif 60 < Mark < 70:
    print("Garde A")
elif 70 < Mark < 80:
    print("Garde A+")
elif 80< Mark < 90:
    print("Garde A++")
elif 90 < Mark < 100:
    print("Garde Merit")
else:
    print("Invalid Grade")
