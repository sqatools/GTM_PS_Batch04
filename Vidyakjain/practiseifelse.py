num=3
if num%3==0:
    print("number is divisible by 3")
else:
    print("number is not divisible by 3")

############Program to get all numbers divided by 3 between 1 to 30##########

for i in range(1,31):
    if i%3==0:
        print(i,end=" ")

print("_"*50)

##################
"""
Marks less than 40: Fail
Marks between 40-50: Grade C
Marks between 51-60: Grade B
Marks between 61-70: Grade A
Marks between 71-80: Grade A+
Marks between 81-90: Grade A++
Marks between 91-100: Excellent
"""
marks=99
if 40 < marks <=50:
    print("grade is C")
elif 50 < marks <=60:
    print("grade is B")
elif 60 < marks <= 70:
    print("grade is A")
elif 70 < marks <= 80:
    print("grade is A++")
elif 80 < marks <= 90:
    print("grade is A")
elif 90 < marks <= 100:
    print("grade is Excellent")
elif marks >100:
    print("invalid")
else:
    print("fail")


###########range from 1 to 30
for i in range(1, 30):
    print(i)
for k in range(5):
    print(k)
for j in range(1,20,2):
    print(j)





