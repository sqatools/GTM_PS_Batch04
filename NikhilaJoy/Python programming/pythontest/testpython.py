#1. Write a python python program to calculate sum of all the numbers in the string.
"""
str1= "Good 12 Morning 45 , Hope 2 you are 30 doing good"
output = 0

str2=str1.split(" ")
print(str2)
for char in str2:
    if char.isnumeric()==True:
        a=int(char)
        output =output+a
    else :
        continue
print(output)
"""
#2. Write a python Program to convert first and last character to upper case.
"""
str1= "python programming is very easy to learn"
output =" "
val=" "

str2=str1.split(" ")
print(str2)
for char in str2:
       val=output+char[0].upper()+char[1:-1]+char[-1].upper()
       print(val,end=" ")
"""

#3. Write a Python Program to find out prime number from give list of values

list1 = [13, 56, 77, 23, 29, 11]
#output = [13, 23, 29, 11]
output=[]
#count = 0

for n in list1:
   count = 0
   for i in range(2,n):
        if n%i==0:
           count +=1
   if count==0:
     output.append(n)
print(output)

"""
list1 = [13, 56, 77, 23, 29, 11]

output = [13, 23, 29, 11]

list1 = [13, 56, 77, 23, 29, 11]

list2 = []

for value in list1:

    count = 0

    for i in range(2, value):

        if value % i == 0:
            count += 1

    if count == 0:
        list2.append(value)

print(list2)

O / p: [13, 23, 29, 11]
"""

"""
#4. Write a python program to create below output dictionary with given string.
str1 = "India is best cricket teams"
#utput = {5: "IndiA", 2: "IS", 4: "BesT", 7:"CrickeT", 5: "TeamS"}
str2=str1.split()
print(str2)
output = {}
for char in str2:
    output[len(char)] = char[0].upper()+char[1:-1]+char[-1].upper()
print(output)

"""


