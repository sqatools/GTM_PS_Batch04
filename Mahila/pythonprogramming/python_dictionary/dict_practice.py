"""#Python program to add elements to the dictionary

dict = {}
dict["name"] = "mahila"
dict["place"] = "kerala"
print(dict)



#Python Dictionary program to print the square of all values in a dictionary.
#Input : {‘a’: 5, ‘b’:3, ‘c’: 6, ‘d’ : 8}
#Output :
#a : 25
#b : 9
#c : 36
#d : 64

dic1= {'a': 5, 'b':3, 'c': 6, 'd': 8}
for val in dic1:
    print(val,":",dic1[val]**2)


#D1 TO D2
D1 = {'name':'john','city':'Landon','country':'UK'}
D2 ={}

for val in D1:
    D2[val] = D1[val]

print(D2)



#dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’}
#dict2 = {‘Age’ : 25, ‘salary’: ‘$25k’}
#Output :
#dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’, ‘Age’ : 25, ‘salary’: ‘$25k’}

dict1 = {'Name':'Harry','Rollno':345,'Address':'Jordan'}
dict2 = {'Age':25,'salary': '$25k'}

dict1.update(dict2)
print(dict1)

# Python Dictionary program to get a list of odd and even keys from the dictionary.
# Input :
# {1: 25, 5:’abc’, 8:’pqr’, 21:’xyz’, 12:’def’, 2:’utv’}
# Output :
# Even Key = [[8, ‘pqr’], [12, ‘def’], [2, ‘utv’]]
# Odd Key = [[1, 25], [5, ‘abc’], [21, ‘xyz’]]




dict1 = {1:25,5:'abc',8:'pqr',21:'xyz',12:'def',2:'utv'}
list1 = {}
list2 = {}

for key,value in dict1.items():
    if key%2==0:
        list1[key] = value
    else:
        list2[key] = value

print("Even :",list1)
print("odd :",list2)



# Python Dictionary Program to create a dictionary from two lists.
# Input :
# list1 = [‘a’, ‘b’, ‘c’, ‘d’, ‘e’]|
# list2 = [12, 23, 24, 25, 15, 16]
# Output :
# {‘a’: 12, ‘b’: 23, ‘c’: 24, ‘d’: 25, ‘e’: 15}

list1 = ['a','b','c','d','e']
list2 = [12, 23, 24, 25, 15, 16]

result = dict(zip(list1,list2))
print(result)

# #Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.
# Input :
# [4, 5, 6, 2, 1, 7, 11]
# Output :
# {4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}

list1 =  [4, 5, 6, 2, 1, 7, 11]
dict = {}

for val in list1:
    if val%2==0:
        dict[val]=val**2
    else:
        dict[val]=val**3
print(dict)


# Python
# Dictionary
# program
# to
# clear
# all
# items
# from the dictionary.

dict1= {4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}

dict1.clear()
print(dict1)

# Python Dictionary program to remove duplicate values from Dictionary.
# Input :
# {‘a’: 12, ‘b’: 2, ‘c’: 12, ‘d’: 5, ‘e’: 35, ‘f’: 5}
# Output :
# {‘a’: 12, ‘b’: 2, ‘d’: 5, ‘e’: 35}

dict1= {'a':12,'b':2,'c':12,'d':5,'e':35,'f':5}
dict2 ={ }

for key,value in dict1.items():
    if value not in dict2.values():
        dict2[key] = value
    else:
        continue
print(dict2)

"""
#
# Python Dictionary program to sort a dictionary using keys.
# Input = {‘d’ : 21, ‘b’ : 53,  ‘a’: 13, ‘c’: 41}
# Output =
# (‘a’, 13)
# (‘b’, 53)
# (‘c’, 41)
# (‘d’, 21)

#Python program to add a key in a dictionary.

dict1= {'a':12,'b':2,'c':12,'d':5,'e':35,'f':5}
dict1.update({3:'c'})
#dict1['h']=100
print(dict1)

