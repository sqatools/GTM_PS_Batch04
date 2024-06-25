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

dict15 = {"d" : 21, "b" :53, "a" :13, "c" : 41}

for key  in sorted(dict15):
    print(key,dict15[key])