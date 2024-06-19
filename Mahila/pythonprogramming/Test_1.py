# Write a python python program to calculate sum of all the numbers in the string.
# str1= "Good 12 Morning 45 , Hope 2 you are 30 doing good"
# output = 89

# str1= "Good 12 Morning 45 , Hope 2 you are 30 doing good"
# output = []
# str = str1.split(" ")
# print(str)
#
# for word in str:
#     if word.isnumeric():
#         output.append(word)
#
# result = " ".join(output)
# print(sum(output))


# Write a python Program to convert first and last character to upper case.
# str1= "python programming is very easy to learn"
# output = "PythoN ProgramminG IS VerY EasY TO LearN"
#
# str1= "python programming is very easy to learn"
# str = str1.split(" ")
# print(str)
#
# for char in str:
#     print(char[0].upper() + char[1:-1] + char[-1].upper(),end = " ")

#  Write a Python Program to find out prime number from give list of values
# list1 = [13, 56, 77, 23, 29, 11]
# output = [13, 23, 29, 11]

list1 = [13, 56, 77, 23, 29, 11]
list2 = []

for value in list1:
    c=0
    for j in range(1,value):
        if value%j == 0:
            c += 1
    if c == 1:
        list2.append(value)

#Write a python program to create below output dictionary with given string.
#str1 = "India is best cricket teams"
#output = {5: "IndiA", 2: "IS", 4: "BesT", 7:"CrickeT", 5: "TeamS"}

str1 = "India is best cricket teams"
#utput = {5: "IndiA", 2: "IS", 4: "BesT", 7:"CrickeT", 5: "TeamS"}
str2=str1.split()
print(str2)
 output = {}
for char in str2:
 output[len(char)]=char[0].upper()+char[1:-1]+char[-1].upper()
print(output)

l
