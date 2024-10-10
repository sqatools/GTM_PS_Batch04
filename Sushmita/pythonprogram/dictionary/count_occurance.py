# a='aaaabbbbccddaa'
# dictionary=dict()
#
# for char in a:
#     dictionary[char]=a.count(char)
# print(dictionary)

string1 = "I Love India"
str1 = string1.split()
str1.reverse()
"".join(str1)
print(str1)
# string = "Cricket Plays Virat"
#
# #Converting to a list
# List = string.split()
# List.reverse()
#
# #Printing output
# #
# print(List)
list1=[1,2,3,4]
list2=[1,2,5,6]
list3=[]

for num in list1:
    if num in list2:
        list3.append(num)

print(list3)
