"""1. Write a python python program to calculate sum of all the numbers in the string.
str1= "Good 12 Morning 45 , Hope 2 you are 30 doing good"
output = 89"""


str1 = "Good 12 Morning 45 , Hope 2 you are 30 doing good"

str2 = str1.split(" ")
print(str2)
Total=0

for val in str2:
    if val.isnumeric():
        print(val)
        print(type(val))
        x1 = int(val) # conversion not possible hence addition not possible
        print(type(val))

        Total += x1

print(Total)

"""2. Write a python Program to convert first and last character to upper case.
str1= "python programming is very easy to learn"
output = "PythoN ProgramminG IS VerY EasY TO LearN"
"""

str3= "python programming is very easy to learn"
Newstr = ""

# for i in  str3:
#     if i[0] ==
#     print(i, end="")



# str4 = str3.split(" ")
# print(str4)
#
# print(str4[0:-1])



# print(str3.index("p"))
#
# for char in str3:
#     if char in


# str4 = str3.split(" ")
# print(str4)

# str4 = ""
#
# for char in str3:
#     if char is str[0]:
#     str4 = str3.swapcase()
#     print(str4)

#for char in str3:
#print(str3[:-1])



"""3. Write a Python Program to find out prime number from give list of values
list1 = [13, 56, 77, 23, 29, 11]
output = [13, 23, 29, 11]"""


list1 = [13, 56, 77, 23, 29, 11]
list2 = []

for value in list1:
    prime=0
    for num in range(1,value):
        if value%num == 0:
            prime += 1
    if prime == 1:
        list2.append(value)

print(list2)

"""4. Write a python program to create below output dictionary with given string.
str1 = "India is best cricket teams"
output = {5: "IndiA", 2: "IS", 4: "BesT", 7:"CrickeT", 5: "TeamS"}
"""

str10 = "India is best cricket teams"

dict = {}

str11 = str10.split(" ")

print(str11)
L1 = str11
