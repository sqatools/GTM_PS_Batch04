#1. Write a python python program to calculate sum of all the numbers in the string.
#str1= "Good 12 Morning 45 , Hope 2 you are 30 doing good"
#output = 89

str1="Good 12 Morning 45 , Hope 2 you are 30 doing good"
print("Good 12 Morning 45 , Hope 2 you are 30 doing good")
sum=0
x=str1.split()
print(x)
for i in x:
   if x.isnumeric():
       sum+=int(i)
       print(sum)



#2. Write a python Program to convert first and last character to upper case.
#str1= "python programming is very easy to learn"
#output = "PythoN ProgramminG IS VerY EasY TO LearN"

str= "python programming is very easy to learn"
i=str.split()
print(i)
for str1 in range(len(i)):
    str1=str1[0:1].upper()+str1[1:len(str1)-1]+ str1[len(str1)-1:len(str1)].upper()
print(str1);



#3. Write a Python Program to find out prime number from give list of values
#list1 = [13, 56, 77, 23, 29, 11]
#output = [13, 23, 29,

list1 = [13, 56, 77, 23, 29, 11]
prime=[]
flag=0
for i in range(list1):
    if i==0 or i==1:
        continue
    else:
    for j in range(2,int(i/2)+1):
        if i%j==0:
            break
        else:
x=prime.append(i)
print(x)


#4. Write a python program to create below output dictionary with given string.
#str1 = "India is best cricket teams"
#output = {5: "IndiA", 2: "IS", 4: "BesT", 7:"CrickeT", 5: "TeamS"}

