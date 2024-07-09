"Programs on String Lists and Dictonary"

#1). Python Dictionary program to add elements to the dictionary.

dict1 = {"a" : 1, "b" : 2, "c" : "Kirti", "d" :"True"}
print(dict1)

dict1["Age"] = 35
dict1["Name"] = "Raul"

print("Existing Dictonary : ",dict1)

print("_"*50)

# Adding elements into blank dictionary # How to add elemets of data type other than string and int

dict2 = {}

dict2["Name"] = "Kirti"
dict2["Age"] = 25
dict2["DOB"] = "20-05-1997"

print("Balnk Dictnoary : ",dict2)

print("_"*50)

"""
2). Python Dictionary program to print the square of all values in a dictionary.
Input : {‘a’: 5, ‘b’:3, ‘c’: 6, ‘d’ : 8}
Output :
a : 25
b : 9
c : 36
d : 64
"""
######### apply loop on dictionary #######
print("_"*50)
dict1 = {'a' : 123, 'b': 345, 'c' : 678}
for val in dict1.items():
    print(val)
"""
('a', 123)
('b', 345)
('c', 678)
"""


dict3 = {"a": 5, "b":3, "c": 6, "c" : 8}


for val in dict3:
    x = dict3[val]**2

    print("Square of the given numbers :",x)

"""
3.Python Dictionary program to move items from dict1 to dict2.
Input :
dict1 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}
dict2 = {}
Output :
dict1 = {}
dict2 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}"""

# printing in iteration not in singel line ?
# How dict1.items(): would work here ?

dict4 = {"Name" : "Jhon","City" :"London", "Country" : "UK"}
dict5 = {}

for val in dict4: # do i need to give custly braces here ? to print the out in dict form ?
    dict5[val] = dict4[val]
    print("Moved Dict :", dict5[val])

"""dict5.append(dict4[val])  # AttributeError: 'dict' object has no attribute 'append' ?
print(dict5)"""

"""4).  Python Dictionary program to concatenate two dictionaries.
Input :
dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’}
dict2 = {‘Age’ : 25, ‘salary’: ‘$25k’}
Output :
dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’, ‘Age’ : 25, ‘salary’: ‘$25k’}
"""

dict6 = {"Name" : "Kirti", "Aage" : 25}
dict7 = {"Name" : "Rahul", "Age" : 35}

# How to do using String concatination ?

# for val in dict7:   # Can we do like this adding both the dits to one output dict and printing it using for loop/range
#     Output = dict7[val]
#     print(Output)

dict6.update(dict7)
print(dict6)

print("_"*50)

"""5). Python Dictionary program to get a list of odd and even keys from the dictionary.
Input :
{1: 25, 5:’abc’, 8:’pqr’, 21:’xyz’, 12:’def’, 2:’utv’}
Output :
Even Key = [[8, ‘pqr’], [12, ‘def’], [2, ‘utv’]]
Odd Key = [[1, 25], [5, ‘abc’], [21, ‘xyz’]]"""



dict8  = {1 :25, 5:"abc", 8:"pqr", 21 :"xyz", 12 :"def", 2:"utv"}

#for val in dict8[val]:  # if i write like this then the out put is not coming
# how to print out put in dictionary format
# Need clarity once agina = "list1 = [[val,dict1[val]] for val in dict1 if val%2 == 0]"

for val in dict8:
    if val%2 == 0:
        #Even = val
        print("Even :", val)
    else :
        #odd = val
        print("Odd :", val)
print("_"*50)

"""6). Python Dictionary Program to create a dictionary from two lists.
Input :
list1 = [‘a’, ‘b’, ‘c’, ‘d’, ‘e’]
list2 = [12, 23, 24, 25, 15, 16]
Output :
{‘a’: 12, ‘b’: 23, ‘c’: 24, ‘d’: 25, ‘e’: 15}"""

l1 = ["a,","b","c","d","e"]
l2 = [12,23,24,25,15,16]

dict9 = {}

# dict9  = {} # Can we do it using update method ?
# dict9.update(l1)
# print(dict9)

for val1, val2 in zip(l1,l2):
    #zip(l1,l2)
    dict9[val1] = val2
   # print(dict9) # If i print it inside the for loop condition it will print all the iterations.
print(dict9)

"""7).  Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.
Input :
[4, 5, 6, 2, 1, 7, 11]
Output :
{4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}
"""

l3 = [4,5,6,2,1,7,11]
dict10 ={}

for val in l3:
    if val % 2 == 0:
        #print("Even :", val**2)
        dict10[val] = val**2
    else:
        #print("Odd :", val**3)
        dict10[val] = val**3
print(dict10)

"8). Python Dictionary program to clear all items from the dictionary."

dict11 = {'a':1, 'b':20}
dict11.clear()


print("_"*50)
"""9). Python Dictionary program to remove duplicate values from Dictionary.
Input :
{‘a’: 12, ‘b’: 2, ‘c’: 12, ‘d’: 5, ‘e’: 35, ‘f’: 5}
Output :
{‘a’: 12, ‘b’: 2, ‘d’: 5, ‘e’: 35}
"""


dict12 = {"a" : 12, "b" : 2, "c" : 12, "d" : 5, "e" : 35, "f" : 5}

dict13 = {}


for key,val in dict12.items():
    print("key :", key, "value :", val)
    if val not in dict13.values():
        print("Value is : ",val)
        dict13[key] = val # Need explanation
        print("New Dict :", dict13)

print("New Dict :", dict13)

print("_"*50)

"""10). Python Dictionary program to create a dictionary from the string.
Input  = ‘SQATools’
Output = {‘S’: 1, ‘Q’: 1, ‘A’: 1, ‘T’: 1, ‘o’: 2, ‘l’: 1, ‘s’: 1}
"""

Str  = 'SQATools'

dict14 = {}

for val in Str:
    #if val not in dict14:
       # dict14[val] = val why this is wrong ?
        dict14[val] = Str.count(val)
print(dict14)

print("_"*50)

"""11). Python Dictionary program to sort a dictionary using keys.
Input = {‘d’ : 21, ‘b’ : 53,  ‘a’: 13, ‘c’: 41}
Output =
(‘a’, 13)
(‘b’, 53)
(‘c’, 41)
(‘d’, 21)"""

# need to execute this again
# dict15 = {"d" : 21, "b" :53, "a" :13, "c" : 41}
#
# for key  in sorted(dict15):
#     print(key,dict15[key])

"""14). Python Dictionary program to concatenate two dictionaries.
Input:
D1 = {‘name’ : ’yash’, ‘city’ :  ‘pune’}
D1 = {‘course’ : ’ python’, ‘institute’ : ’sqatools’}
Output :
{ ‘name’ : ’yash’, city: ‘pune’, ‘course’ : ’python’, ‘institute’ : ’sqatools’ }
"""


dict15 = {"a": 1, "b" : 2, "c" : 4}
dict16 = {"x" : "Kirti", "y" : "Ram"}

dict15.update(dict16)

print(dict15)

print("_"*50)


"""15). Python Dictionary program to swap the values of the keys in the dictionary.
Input = {name:’yash’, city: ‘pune’}
Output = {name:’pune’, city: ‘yash’}"""


dict17 = {"Name"  :"Kirti", "Age" : 25}
#dict18 = {"Name" : "Ram", "Age" : 35}  how to interchange the values of two dicts

dict19 = {}

for key,value in dict17.items():
    dict19[value] = key
print(dict19)


"""16).  Python Dictionary program to get the sum of all the items in a dictionary.
Input = {‘x’ : 23, ‘y’ : 10 , ‘z’ : 7}
Output = 40"""

dict18 = {"x" : 23, "y" :10, "z" : 7}
Total = 0
for values in dict18.values():
    print(values)
    Total += values
print("TOTAL : ",Total)

import sys
D1 = {'name':'virat','sport':'cricket'}

print("Size of dic1: " + str(sys.getsizeof(D1)) + "bytes")


"String programs"
"""Get all the email id’s from the given string"""


string = """We have some employee whos john@gmail.com email id’s are randomly distributed jay@lic.com we want to get hari@facebook.com all the email mery@hotmail.com id’s from this given string"""

list = string.split(" ")
print(list,end="\n")
list1 = []

for char in list:
    for val in char:
        if val == "@":
            list1.append(char)
print(list1, end="\n")


"""Write a program to get a list of all the mobile numbers from the given string using  python.
Input str = “”” We have 2233 some employee 8988858683 whos 3455 mobile numbers are randomly distributed 2312245566 we want 453452 to get 4532892234 all the mobile numbers 9999234355  from this given string.””
"""
print("_"*50)

string =  """"We have 2233 some employee 8988858683 whos 3455 mobile numbers are randomly distributed 2312245566 we want 453452 to get 4532892234 all the mobile numbers 9999234355  from this given string"""

list2 = string.split(" ")
print(list2,end="\n")

list3 = []

for val in list2:
    if len(val) == 10 and val.isnumeric():
        list3.append(val)
print(list3, end="\n")

print("_"*50)

"character on new line"

str1 = "python"
for char in str1:
    print(char, end="\n")

"Print the given string 3 times"

string5 = "Kirti"

print(string5*3)

"""102). Write a program to remove repeated characters in a string and replace it with a single letter using  python.
Input = ‘aabbccdd’
Output = ‘cabd’"""


# string6 = "aabbccdd"
#
# string7 = string6.split("")
# print(string7)

"""101). Write a program to swap cases of a given string using  python.
Input = ‘Learning  Python’
Output = ‘lEARNING pYTHON’"""

string8 = "Learning  Python"

string9 = string8.upper()
print(string9)

string10 = string9.lower()
print(string10)

string11 = string8.swapcase()
print(string11)


"""100). Write a program to find the first repeated character in a string and its index.
Input = ‘sqatools’
Output = (s,0)"""

string12 = "sqatools"
characters = []

for char in string12:
    if char not in characters:
        characters.append(char)
print(characters)

"List Programs"
