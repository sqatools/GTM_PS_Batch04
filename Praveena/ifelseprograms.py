# divisble by 3

# Take input
i = int(input("Please enter number :"))
# Check whether the number is divisible by 3
if i % 3 == 0:
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 3")

print("-" * 50)
# program to get all the numbers divided by 3 from 1 to 30
# Iterate over numbers from 1-30
for i in range(1, 31):

    # Check whether number is divisible by 3
    if i % 3 == 0:
        # Print output
        print(i)

print("-" * 50)

# Marks of students

marks = int(input("Please enter marks:"))

if marks < 40:
    print("Failed")

elif marks >= 40 and marks <= 50:
    print("C")

elif marks >= 50 and marks <= 60:
    print("B")

elif marks >= 60 and marks <= 70:
    print("A")

elif marks >= 70 and marks <= 80:
    print("A+")

elif marks >= 80 and marks <= 90:
    print("A++")

elif marks >= 90 and marks <= 100:
    print("Excellent")

elif marks > 100:
    print("Invalid")

print("-" * 50)

# check whether given number is div by 3 and 5

no = int(input("please enter number:"))

if no % 3 == 0 and no % 5 == 0:
    print("div by 3 and 5")
else:
    print("not div by 3 and 5")

print("-" * 50)

# check the given number is odd and even

a = int(input("enter number:"))

if a%2==0:
    print(" a is even")
else:
    print("a is odd")

print("-" * 50)

# authenticate username and password

username = input("name:")
password = input("password:")

if username == password:
    print("It is valid")
else:
    print("It is not valid")

print("-"*50)