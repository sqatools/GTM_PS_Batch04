#Write a python python program to calculate sum of all the numbers in the string.
#str1= "Good 12 Morning 45 , Hope 2 you are 30 doing good"
#output = 89

str1= "Good 12 Morning 45 , Hope 2 you are 30 doing good"
str2=str1.split()
list1=[]
sum=0
for val in str2:
    if val.isdigit():
        list1.append(val)

print(list1)

