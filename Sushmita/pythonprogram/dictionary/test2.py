#Write a python Program to convert first and last character to upper case.
#str1= "python programming is very easy to learn"
#output = "PythoN ProgramminG IS VerY EasY TO LearN"
str1="python programming is very easy to learn"
str2=str1.title()
str3=str2.split()
#print(str3)
list1=[]
for char in str3:
    list1.append(char[0:-1]+char[-1].upper())

print(list1)
