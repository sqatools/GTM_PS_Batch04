#Python program to check given number is divided by 3 or not.

a = 32
if a%3 ==0:
   print("a is divisible by 3")
else:
    print("a is not divisible by 3")

#Python program to check whether the given number is negative or not.

a = -45
if a<0:
    print("Number is negative")
else:
    print("Number is positive")

#Using a python program take input from the user between 1 to 7 and
# print the day according to the number. 1 for Sunday 2 for Monday so on.

x = int(input("Enter a number: "))

if x == 1:
    print("Sunday")
elif x == 2:
    print("Monday")
elif x == 3:
    print("Tuesday")
elif x == 4:
    print("Wednesday")
elif x == 5:
    print("Thursday")
elif x == 6:
    print("Friday")
elif x == 7:
    print("Saturday")
else:
    print("Invalid number")

#Python program to check whether the citizen is a senior citizen or not.
#An age greater than 60 than the given citizen is a senior citizen.

age = int(input("Enter the age of citizen:"))
if age>60:
    print("Citizen is senior citizen")
else:
    print("Citizen is not senior citizen")

#Python program to print the largest number from two numbers.

a = 215
b = 45

if a>b:
    print("a is the largest number")
else:
    print("b is the largest number")