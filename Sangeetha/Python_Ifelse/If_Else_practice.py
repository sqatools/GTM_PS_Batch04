##program to check given number is divided by 3 or not.

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

print("_"*40)

#Python program to check authentication with the given username and password.

name=input("enter name : ")
password=input("password : ")
if name==password:
    print("it is  valid ")
else :
    print("it is not valid")

print("_"*40)

###Python program to validate user_id in the list of user_ids.



