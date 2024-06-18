# 1 Dictionary program to add elements to the dictionary
dictionary = {}
dictionary["Name"] = "sangeetha"
dictionary["Age"] = "27"
print(dictionary)

# 2 Input : {‘a’: 5, ‘b’:3, ‘c’: 6, ‘d’ : 8}

dictionary= {"a":5,"b":3,"c":6,"d":8}
for val in dictionary:
    print(dictionary[val]**2)

#move items from dict1 to dict2.
d1 = {"name": "john", "city": "Landon", "country": "UK"}
d2 = {}
for val in d1:
    d2[val] = d1[val]
print(d2)

#Dictionary program to concatenate two dictionaries.
dict1 = {"Name": "Harry", "Rollno":345, "Address": "Jordan"}
dict2 = {"Age" : 25,"salary": "$25k"}
dict1.update(dict2)
print(dict1)

##get a list of odd and even keys from the dictionar
dict1={1: 25, 5:'abc', 8:'pqr', 21:'xyz', 12:'def', 2:'utv'}
list1 = [[val,dict1[val]] for val in dict1 if val%2 == 0]
list2 = [[val,dict1[val]] for val in dict1 if val%2 != 0]

print("Even key = ",list1)
print("Odd key = ",list2)

#Dictionary Program to create a dictionary from two lists.

list1 = ["a","b","c","d","e"]
list2 = [12, 23, 24, 25, 15, 16]
dict1={}
for a,b in zip(list1,list2):
    dict1[a] = b

print(dict1)

#store squares of even and cubes of
# odd numbers in a dictionary using dictionary comprehension
list=[4, 5, 6, 2, 1, 7, 11]
dict2={}
for val in list:
    if val % 2 == 0:
        dict2[val] = val ** 2
    else:
        dict2[val] = val ** 3
print(dict2)

#clear items
d1 = {"name": "john", "city": "Landon", "country": "UK"}
d1.clear()
print(d1)

#remove duplicate values
dict5={"a": 12, "b": 2, "c": 12, "d": 5, "e": 35, "f": 5}
dict6={}
for key,val in dict5.items():
    if val not in dict6.values():
        dict6[key] = val
print(dict6)
#create a dictionary from the string.

str="SQATOOLS"
dictionary={}
for char in str:
    dictionary[char]=str.count(char)
print(dictionary)