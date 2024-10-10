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

dict1={'a':100,'b':200 ,'c':300}
print(dict1,type(dict1))

dict1['d']=300

print(dict1) #{'a': 100, 'b': 200, 'c': 300, 'd': 300}

dict1['b']=500
print(dict1) #{'a': 100, 'b': 500, 'c': 300, 'd': 300}

dict1['true']='program'
dict1[1,2,3]={'name':'sushmita','add':'shastri'}

print(dict1) #{'a': 100, 'b': 500, 'c': 300, 'd': 300, 'true': 'program', (1, 2, 3): {'name': 'sushmita', 'add': 'shastri'}}

print(dict1['true']) #program

print("_" * 50)
#################### Apply loop on the dictionary ################
dict2 = {"Name": 'Rahul', 'age': 30, 'DOB': "01/10/2000"}
print(dict2)

for val in dict2.items():
    print(val)

for k,v in dict2.items():
    print('key:',k,'value:',v)

#################### Methods of Dictionary ################
print(dir(dict))

# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop',
# 'popitem', 'setdefault', 'update', 'values']

####
# get() method : Get value on the basis of key
dict_a = {'city': 'Mumbai', 'country': 'India', 'Address': 'Juhu'}
print('key value:',dict_a.get('city')) #Mumbai

#####
print("_" * 50)
# keys() method : This method list of keys in the dictionary
print(dict_a.keys()) # dict_keys(['city', 'country', 'Address'])

# values() method : This method return the list of values in the dictionary
print('values list:',dict_a.values()) #dict_values(['Mumbai', 'India', 'Juhu'])

#####
print("_" * 50)
# update method : update one dictionary to another dictionary
dict_b = {'a': 234, 'b': 456, 'c': 678}
dict_c = {'p': 555, 'q': 333, 'r': 777}

dict_c.update(dict_b)
print('dict b',dict_b)
print('dict c',dict_c)

print("_" * 50)
######## remove data from dictionary ######

dict3 = {'p': 555, 'q': 333, 'r': 777, 'a': 234, 'b': 456, 'c': 678}
# pop method: This method remove data from dictionary with the help key and return value

print(dict3.pop('a')) #234

print(dict3) #{'p': 555, 'q': 333, 'r': 777, 'b': 456, 'c': 678}

# popitem() : This method remove the key value from dictionary and return.
# last key value pair will remove first and return as tuple of key value pair

print(dict3.popitem()) #('c', 678)

print("_" * 50)
##########################

# clear() : This method clear all the data from dictionary
dict_q = {'Name': 'John', 'Age': 35, 'Address': 'Pune'}
dict_q.clear()

print(dict_q)

print("_" * 50)
###################
# Del
dict_r = {'Name': 'John', 'Age': 35, 'Address': 'Pune'}

'''
del dict_r
print(dict_r)
'''
del dict_r['Age']
print(dict_r) #{'Name': 'John', 'Address': 'Pune'}

print("_" * 50)
########################
# copy method
# Shallow copy

p = {'name':'Abc','age':25}
q=p
q['city']='bangalore'

print('p dict:',p)
print('q dict:',q)

# Deep Copy:
print("_" * 50)
a={'a':300,'b':200}
b=a.copy()
b['c']=100

print('a:',a)
print('b:',b)
