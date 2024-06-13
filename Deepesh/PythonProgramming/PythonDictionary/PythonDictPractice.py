"""
Properties :
->  Dictionary define with curly braces.
-> dict store data in key value pair.
-> dictionary is a mutable data type
-> Duplicate keys are not allowed in the dictionary.
-> Index and slicing is not available in dictionary
-> Dict can have duplicate values
-> Only immutable data type can be add as key e.g. int, float, string, tuple, boolean.
-> All type of data type can value in the dictionary
"""

dict1 = {'a': 123, 'b': 345, 'c': 464, 'a': 500}
print("dict1 :", dict1, type(dict1))


dict1['d'] = 600
print(dict1)  # {'a': 500, 'b': 345, 'c': 464, 'd': 600}
# adding duplicate values
dict1['e'] = 600

print("dit with duplicate value :", dict1)
# dict with duplicate value : {'a': 500, 'b': 345, 'c': 464, 'd': 600, 'e': 600}

print("_" * 50)
dict1[20] = [4, 6, 7]
dict1[True] = 'Python Programming'
dict1[4.5] = 55
dict1[(1, 2, 3)] = {'Name': 'Rahul', 'age': 25}

print("updated dict1 :", dict1)

print(dict1[(1, 2, 3)])  # {'Name': 'Rahul', 'age': 25}

# dict1[[3, 5, 6]] = 'Python'
#  unhashable type: 'list'

print("_" * 50)
#################### Apply loop on the dictionary ################
dict2 = {"Name": 'Rahul', 'age': 30, 'DOB': "01/10/2000"}
print(dict2)

print(dict2.items())
for data in dict2.items():
    print(data)

for k, v in dict2.items():
    print("Key :", k, "value :", v)


#################### Methods of Dictionary ################
print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop',
# 'popitem', 'setdefault', 'update', 'values']

####
# get() method : Get value on the basis of key
dict_a = {'city' : 'Mumbai', 'country' : 'India', 'Address' : 'Juhu'}
print("get city name :", dict_a.get('city'))  # Mumbai

#####
print("_"*50)
# keys() method : This method list of keys in the dictionary
key_list = dict_a.keys()
print("Keys list :", key_list, type(key_list)) # dict_keys(['city', 'country', 'Address'])
print(list(key_list))

# values() method : This method return the list of values in the dictionary
print("values list :", dict_a.values())

#####
print("_"*50)
# update method : update one dictionary to another dictionary
dict_b = {'a' : 234, 'b': 456, 'c': 678}
dict_c = {'p' : 555, 'q': 333, 'r' : 777}

dict_c.update(dict_b)
print("dict_c :", dict_c)
print("dict_b :", dict_b)

print("_"*50)
######## remove data from dictionary ######

dict3  = {'p': 555, 'q': 333, 'r': 777, 'a': 234, 'b': 456, 'c': 678}
# pop method: This method remove data from dictionary with the help key and return value.

val = dict3.pop('a')
print("value of a :", val) # 234
print("updated dictionary :", dict3)  # {'p': 555, 'q': 333, 'r': 777, 'b': 456, 'c': 678}


# popitem() : This method remove the key value from dictionary and return.
# last key value pair will remove first and return as tuple of key value pair
result = dict3.popitem()
print("removed item :",result)  # ('c', 678)
print("Updated dict3 :", dict3)  # {'p': 555, 'q': 333, 'r': 777, 'b': 456}

