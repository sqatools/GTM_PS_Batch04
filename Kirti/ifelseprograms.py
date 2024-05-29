# ************************************ 1
print("if else programs and for loop programs")

a = 30
if a%3 == 0:
    print("Number is divisible by 3")
else :
    print("Number is not divisible by 3")

# ************************************ 2

print("_"*30)

print("Program to get all numbers divided by 3 between 1 to 30")


for i in range(1,30):
    if 1%3 == 0:
        print(i)

# ************************************ 3

print("_ marks "*30)

marks = 41

if marks< 40 :
    print("FAIL")
elif 40 <= marks <= 50:
    print("Grade C")
elif 50 <= marks <= 60:
    print("Grade B")
elif 60 <= marks >= 70:
    print("Grade A")
elif 70 <= marks >= 80:
    print("Grade A+")
elif 80 <= marks >= 90:
    print("Grade A++")
elif 90 <= marks >= 100:
    print("Excelent")
else :
    print("INVALID")
# ************************************ 4

print("_"*50)

print("Python program to print the square of the number if it is divided by 11")

a = 22

if a%11 == 0:
    print("Sauare of number divided by 11 is :", a**2)
# ************************************ 5

print("_"*50)
print(" Python program to check given number is a Even or odd")

a = 3

if a%2 ==0:
    print("Given number is even")
else :
    print("Given Number is odd",a)
# ************************************ 6

print("_"*50)
print("program to check the given number is divisible by 3 and 7")

a = 22

if a%3 == 0 and a%7 ==0 :
    print("Number is divisible by 3 and 7 both",a)
else :
    print("Number is not divisible by 3 and 7 both")

# ************************************ 7
print("_"*50)
print("interview process")

r1 = "pass"
r2 = "Fail"

if r1 == "pass" :
    print("Eligible for round 2")
    if r2 == "pass":
        print("Congrats placed")
    else:
        print("Better luck next time")

else :
    print("Not eligible for round 2")


# if r2 == "pass" :
#     print("Congrats placed")
# else :
#     print("Better luck next time")

# ************************************ 8

