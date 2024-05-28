#### Python Program to check number is divisible by 3 or not #######
"""
num = int(input("Please enter number :"))
if num%3 == 0:
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 3")

####################

marks = int(input("Enter marks: "))
if marks<40:
   print("Fail")
elif 40<marks<=50:
    print("Grade C")
elif 50<marks<=60:
   print("Grade B")
elif 60<marks<=70:
   print("Grade A")
elif 70<marks<=80:
    print("Grade A+")
elif 80<marks<=90:
    print("Grade A++")
elif 90<marks<=100:
    print("Excellent")
else:
    print("Invalid marks")


#################### program to check given no is prime no or not ####

num =  int(input("Enter a number: "))
count = 0
for i in range(2,num):
  if num%i == 0:
       count += 1
if count > 0:
  print("It is not a prime number")
else:
   print("It is a prime number")

#############
"""

id_list = [38,78,89,5,9,10,8]

id_ = int(input("Enter ID number: "))
if id_ in id_list:
   print("Valid ID")
else:
   print("Invalid ID")
