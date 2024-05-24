"""
if <condition>:
    code
else:
    code
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


print("sangeeta")
