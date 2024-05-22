"""
Python Data Type

1. Number Data Type
    i).  Integer
    ii). Float
    iii). Complex

2. Sequential Data Type
    i). String
    ii). List
    iiI). Tuple

3. Dictionary
4. Set
5. Boolean
"""

#### Integer Data Type ####

a = 20
b = 12322
c = 623232323232323233
print("value a", a, type(a))
print("value b", b, type(b))
print("value c", c, type(c))

"""
Properties of integer

- Integer is immutable data type, once it is defined we can not change it.
- Integer does not have any limit to defined the number. we can defined any long number
  as integer.
- Only whole will be consider as integer.
"""

###### Float Data Type #######
p = 0.0
q = 12.34
r = 767676.323232323
s = 6565.56464365757
t = 83434545656.56

print("value of p :", p, type(p))  # 0.0 <class 'float'>
print("value of q :", q, type(q))  # 23.22 <class 'float'>
print("value of r :", r, type(r))  # 65456456.56456456 <class 'float'>
print("value of s :", s, type(s))  # 6785.888994432435  <class 'float'>
print("value of t :", t, type(t))  # 8.768657787878766e+22 <class 'float'>

"""
Properties of integer

- Float is immutable data type, once it is defined we can not change it.
- Float does not have any limit to defined the number. we can defined any long number
  as Float. total number of digit would be around 17 for pointer
- Only pointer values will be consider as float.
"""


print("_"*50)
########### Complex data type ###########
# x + yj
# x = real number
# y = imaginary number

var1 = 90 + 40j  # <class 'complex'>
var2= 40 + 5.4j  # <class 'complex'>

var3 = var1 + var2
print("value of var3 :", var3) # value of var3 : (40+34.4j)

print("value of var1  :", var1, type(var1))
print("value of var2  :", var2, type(var2))


###################### Sequentials data type ################
print("_"*60)
##### String Data Type #####

str1 = ''  # <class 'str'>
str2 = "H" # <class 'str'>
str3 = 'Hello How are you? hope you are doing good'
str4 = "Good Morning to everyone, hope you are enjoying the Python"
str5 = 'My name is "Rahul" and living is mumbai'
str6 = "My name is 'Aditya' and living is mumbai"
str7 = '''
Python Programs or Python Programming Examples for 
beginners and professionals with programs on basics, 
controls, loops, functions, native data types etc.
‎Python Arithmetic Operations · 
‎Hello Python Program · ‎Python Area Of Triangle
'''

str8 = """
Python Programs or Python Programming
Examples for beginners and 
professionals with programs
on basics, controls, loops, 
functions, native data types etc.
64356546456456 ^&^*&%^&%^&%&^%&%^$^%$
"""

print("str1 :", type(str1), str1)
print("_"*50)
print("str2 :", type(str2), str2)
print("_"*50)
print("str3 :", type(str3), str3)
print("_"*50)
print("str4 :", type(str4), str4)
print("_"*50)
print("str5 :", type(str5), str5)
print("_"*50)
print("str6 :", type(str6), str6)
print("_"*50)
print("str7 :", type(str7), str7)

print("_"*50)
print("str8 :", type(str8), str8)
print("_"*50)

var1 = "Hello"

"""
 0   1   2   3  4  #+ve
 H   e   l   l  o
-5  -4   -3  -2 -1 # -ve
"""
print(var1[0])  # H
print(var1[-5]) # H

print(var1[-1]) # 0
print(var1[4])  # 0


var2 = "Good Morning"

print(var2[5])  # M

"""
# Properties of String
- String is immutable data type, once it is defined we can not change it.
- String follows both positive and negative indexing.
- String can contains any type of value in double/single quote
"""

print("_"*50)
############ List ############

list1 = [12, 4.5, 'hello', [3, 6 ,7]]
print(list1, type(list1))  # <class 'list'>

list2 = [
    'Hello',            # 0 # -7
    'Good Morning',     # 1 #-6
    4534543,            # 2 # -5
    56.66,              # 3 # -4
    [4, 6, 7, 8],       # 4 # -3
    (4, 7, 2, 22),      # 5 # -2
    {'a': 123, 'b' : 345 }, # 6 # -1
]

print(list2)

s1 = list2[0]
print(s1, type(s1), s1[0]) # Hello <class 'str'> H

print(list2[6], type(list2[6]))  # {'a': 123, 'b': 345} <class 'dict'>

print("_"*50)
str1 = "Hello \n Good \n Morning"
print(str1)

str2 = "Hello \t \t Good \t\t Morning"
print(str2)

print("_"*50)
p = [44, 77, 88]

list3 = [4, 6, 7, [5, 7, 8], p, True]

p2 = list3[3]
print("p2 value :", p2)
p2.append(100)

print(list3)
print(list3[-1])

# get value of child list
print(list3[3][1]) # 7

"""
Properties of List

- List if mutable data type, we can modify at any point of time
- List follows positive and negative indexing as like string
- List can contain any type of data like int, float, string, list, tuple, dict, set, Boolean.
"""
print("_" * 50)
########## Tuple #############

tup1 = (2, 3.5, 'Hello', [3, 5, 6], (2, 3, 4), True)

print(tup1, type(tup1))

print(tup1[2])  # Hello
var1 = tup1[2]
print(var1, var1[0], type(var1))  # Hello H <class 'str'>

print(tup1[-2])  # (2, 3, 4)
var2 = tup1[-2]
print(var2, var2[1], type(var2))  # (2, 3, 4) 3 <class 'tuple'>

list1 = [4, 7, 8]
tup2 = (4, 6, 7, list1)
list1.append(100)

print("tup2 :", tup2)

"""
# properties of tuple
- Tuple is immutable data type, we can not modify it once it is defined.
- Tuple follows positive and negative indexing as like string and list
- Tuple can store all type of data, int, float, string, list, tuple, dict, set, boolean
- Tuple is faster than list.
- We can store duplicate data in the tuple and list
"""

print("_" * 50)
############## Dictionary ##########
# {'key' : 'value'}

dict1 = {'Name': 'Rahul', 'Age': 25, 'Address': 'Mumbai', 'Phone': 45645645}

print(dict1, type(dict1))  # <class 'dict'>

print(dict1['Name'])

dict1['email'] = 'rahul@gmail.com'
print(dict1)

"""
# properties of dictionary
- Dictionary is mutable data type, we can modify at any point of time
- Dictionary store the data in key value pair.
- Dictionary only contains unique key, duplicate keys are not allowed.
- Dictionary can contain duplicate values
- Only immutable data type can key in the dictionary e.g int, float, string
  tuple, boolean

- All type of data can be value in the dictionary, e.g int, float, string, list, 
  tuple, dictionary, set, boolean
"""
print("_" * 50)
dict2 = {
    123: 45.56,
    44.12: 'Good Morning',
    "Hello": [4, 7, 2, 8, 1],
    # [1, 2, 3] : 456            # unhashable type: 'list'
    (3, 6, 1): {'a': 123, 'b': 456},
    # {'a' : 111} : [45,66, 77]   # unhashable type: 'dict'
    123: 88888,

}

print("dict2 :", dict2)

print(dict2[44.12])  # Good Morning

print(dict2[(3, 6, 1)]['b'])  # 456

print("_" * 50)
######################## Set data Type ############################
set1 = {True, False, 1, 0, 3.5, 'Python', 4, 5, (5, 6, 7), 4, 3.5}  # <class 'set'>

print(set1, type(set1))  # {(5, 6, 7), 1, 3.5, 4, 5, 500, 'Python'}

set1.add(500)

print(set1)

"""
# Properties of set data type
- set only store unique data, duplicate data is not allowed.
- set can contains only immutable data type, like int, float, string, tuple, boolean
- set store data in random order.
- set does not follow any indexing/sequence
"""


