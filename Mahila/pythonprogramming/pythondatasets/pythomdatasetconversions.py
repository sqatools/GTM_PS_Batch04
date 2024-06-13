"""
Python Data Type

1. Number Data Type
    i).  Integer - float
         Integer - str
         Integer - bool (0-->false, nonzero -->true)
    ii). Float - int
         Float - str
         float - bool (0-->false, nonzero -->true)
    iii). Complex

2. Sequential Data Type


    i). String
        string -> int
        #### Can not convert word into number ###
        #### IF string is holding only number then the conversion is possible
        string -> float
        #### Can not convert word into number ###
        #### IF string is holding only number then the conversion is possible
        string -> list
        string -> Tuple
        string -> Dictionary #### direct conversion is not possible
        (import jason
        json.loads)
        string -> set
        string- > bool (0-->false, nonzero -->true)


    ii). List
        list --> str
        list -->tuple
        list -->dict ## direct conversion is not possible we need to use zip function
        to use zip function we need 2 list of values
        list -> set
        list --> bool (0-->false, nonzero -->true)


    iiI). Tuple
        tuple-> str
        tuple -> list
        tuple to dict ###direct conversion is not possible.
        so similar to list we can use zip
        tuple -->set (excluds duplicate values)
        tuple -->bool (0-->false, nonzero -->true)


3. Dictionary
        dict -> str
        dict - >list only give key values
        dict -->tuple only give key values
        dict --> set


        dict -->bool
4. Set
        set -> string
        set -> list  duplicate value removed
        set -> tuple  duplicate value removed
        set--> bool
5. Boolean
        bool -->int
        bool -->float
        bool -->str
"""

############# Integer #####

# int -> float

var1 = 664
v2 = float(var1)
print(v2, type(v2))  # 664.0
print(float(var1), type(float(var1)))

print("_" * 40)

####### int -> string  #######
var3 = 4567
s1 = str(var3)
print(s1, type(s1), s1[1])

##### int -> list ##### conversion is not possible
"""
var4 = 6789
l1 = list(var4)  # TypeError: 'int' object is not iterable
print(l1)
"""

### int -> tuple # conversion is not possible
### int -> dict # # conversion is not possible
### int -> set # conversion is not possible
print("_" * 50)
#### int -> boolean

n1 = 0
b1 = bool(n1)
print(b1, type(b1))  # False <class 'bool'>

n1 = 345
b2 = bool(n1)
print(b2, type(b2))  # True <class 'bool'>

################## Float ###############
print("_" * 50)

##### float -> int ########

v1 = 44.56
n1 = int(v1)
print(n1, type(n1))  # 44 <class 'int'>

print("_" * 50)

### Float -> String
v2 = 456.78
s2 = str(v2)
print(s2, type(s2), s2[4], s2[3])  # 456.78 <class 'str'> 7 .

print("_" * 50)
#### Float -> List # conversion is not possible.
#### Float -> Dict # # conversion is not possible
#### Float -> Tuple # # conversion is not possible
#### Float -> Set # # conversion is not possible

#### Float -> Boolean #

a1 = 0.0
b1 = bool(a1)
print(b1, type(b1))  # False <class 'bool'>

a2 = 56.789
b2 = bool(a2)
print(b2, type(b2))  # True <class 'bool'>

################# String Datatype Conversion ################

print("_" * 40)
### string -> int ###

#### Can not convert word into number ###
"""
str1 = "Hello"
n1 = int(str1)  # invalid literal for int() with base 10: 'Hello'
print(n1, type(n1))
"""

#### IF string is holding only number then the conversion is possible

str2 = "56546456456"
n2 = int(str2)
print(n2, type(n2))  # 56546456456 <class 'int'>
print(n2 * 2)  # 113092912912

print("_" * 40)
######## string -> float ########

"""
str_a = "Python Programming"
f1 = float(str_a)  # could not convert string to float: 'Python Programming'
print(f1)
"""

## string holding only float value then we can convert ##
str_b = "45.68"
f2 = float(str_b)
print(f2, type(f2))  # 45.68 <class 'float'>

#### string -> list #######
print("_" * 50)
str3 = "Python"
list1 = list(str3)
print(list1, type(list1))
# ['P', 'y', 't', 'h', 'o', 'n'] <class 'list'>

#### string -> Tuple #######
print("_" * 50)
str4 = "Programming"
tup2 = tuple(str4)
print(tup2, type(tup2))
# ('P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g') <class 'tuple'>


#### string -> Dictionary #### direct conversion is not possible
print("_" * 50)

"""
str4 = "Grow TechMind"
d1 = dict(str4)
print(d1)
# ValueError: dictionary update sequence element #0 has length 1; 2 is required
"""

import json

str5 = '{"Name" : "Rahul", "age" : 25, "address" : "Pune"}'
dict2 = json.loads(str5)
print(dict2, dict2['Name'])
# {'Name': 'Rahul', 'age': 25, 'address': 'Pune'} Rahul

### string -> set ####
print("_" * 50)

str5 = "Python Programming"
set1 = set(str5)
print(set1, type(set1))
# {'o', 'm', 'a', 'h', 'i', 'P', 'y', 'g', 'r', ' ', 't', 'n'} <class 'set'>

### string -> Boolean ####
print("_" * 50)

str_p = ""
b1 = bool(str_p)
print(b1, type(b1))  # False <class 'bool'>

str_q = "Hello"
b2 = bool(str_q)
print(b2, type(b2))  # True <class 'bool'>

############# List Data Type Conversion ########

### list -> int ### Conversion is not possible
### list -> float ### Conversion is not possible

### list -> String ###
print("_" * 50)
list_a = [4, 6, 8, 2]
str1 = str(list_a)
print(str1, type(str1), str1[0], str1[1], str1[-1])

### list -> tuple ###
print("_" * 50)
list_b = [1, 6, 8, 2]
tup2 = tuple(list_b)
print(tup2, type(tup2), tup2[2])

### list -> dict ###  conversion is not possible
print("_" * 50)
"""
list_c = [3, 6, 11, 33]
dict2 = dict(list_c)
print(dict2)
# TypeError: cannot convert dictionary update sequence element #0 to a sequence
"""
l1 = ['a', 'b', 'c', 'd']
l2 = [2, 5, 8, 1]

output = dict(zip(l1,  l2))
print(output)
#{'a': 2, 'b': 5, 'c': 8, 'd': 1}
print(output['a'])  #2

### list -> set ###
print("_" * 50)
list_d = [5, 8, 'a', 'b', 22, 55, 22, 8, 5,33.1, 7]
set_d = set(list_d)
print(set_d)
# {33.1, 5, 7, 8, 'b', 22, 55, 'a'}

#### list ->  boolean ###
print("_" * 50)
list_e = []
b1 = bool(list_e)
print(b1, type(b1))  # False <class 'bool'>

list_f = [4, 7, 8]
b2 = bool(list_f)
print(b2, type(b2))  # True <class 'bool'>


################# Tuple Datatype Conversion ###############

### tuple-> int   ###### conversion is not possible
# tup1 = ('4', '7', '8', '2')
# result = "".join(tup1)
# print(result, type(result), int(result))

### tuple-> float ###### conversion is not possible
### tuple-> string ######
print("_"*40)
tup_a = (4, 7, 2, 8)
str_a = str(tup_a)
print(str_a, type(str_a), str_a[0], str_a[4])
# (4, 7, 2, 8) <class 'str'> ( 7


### tuple -> list ###
print("_"*40)
tup_b = (5, 7, 2, 8)
list_b = list(tup_b)
print(list_b, type(list_b))
# [5, 7, 2, 8] <class 'list'>

### tuple -> dict ### direct conversion is not possible
print("_"*40)

tup_f = ('P','Q', 'R', 'S')
tup_c = (4, 7, 2, 1)
result = dict(zip(tup_f, tup_c))
print(result)
# {'P': 4, 'Q': 7, 'R': 2, 'S': 1}

###### tuple -> set ######
tup_d = (4, 7, 8, 'a', 11, 4, 7, 'a')
set_d = set(tup_d)
print(set_d)
# {4, 7, 8, 11, 'a'}

#### tuple -> boolean ###
tup_e = ()
bool_e = bool(tup_e)
print(bool_e, type(bool_e))  # False <class 'bool'>


tup_f = (4, 7, 8)
bool_f = bool(tup_f)
print(bool_f, type(bool_f))  # True <class 'bool'>


################## Dictionary Data Type Conversion #########

# dict -> int # conversion is not possible
# dict -> float # conversion is not possible
# dict -> string
print("_"*40)
dict1 = {'a' : 123, 'b' : 345}
str1 = str(dict1)
print(str1, type(str1), str1[2])  # {'a': 123, 'b': 345} <class 'str'> a

#### dict -> list ####
print("_"*50)
dict2 = {'a' : 123, 'b' : 345, 'c' : 444}
list1 = list(dict2)
print(list1, type(list1)) # ['a', 'b', 'c'] <class 'list'>

#### dict -> tuple ###
print("_"*50)
dict2 = {'a' : 123, 'b' : 345, 'c' : 444, 'd': 132}
tupl1 = tuple(dict2)
print(tupl1, type(tupl1))  # ('a', 'b', 'c', 'd') <class 'tuple'>


#### dict -> set #######
dict_a = {'a' : 123, 'b' : 345, 'c' : 444, 'd': 132}
set1 = set(dict_a)
print(set1, type(set1)) # {'d', 'c', 'a', 'b'} <class 'set'>

#### dict -> Boolean ###

dict_b = {'P': 123, 'Q': 456, 'R': 333}
b1 = bool(dict_b)
print(b1, type(b1))  # True <class 'bool'>

dict_c = {}
b2 = bool(dict_c)
print(b2, type(b2))  # False <class 'bool'>

print(dict_b.values())


################## Set Data Type #########################
# set -> int # conversion is not possible
# set -> float # conversion is not possible

### set -> string ####
print("_"*50)
set1 = {4, 7, 2, 5, 1, 4, 'a', 'b'}
s1= str(set1)
print(s1, type(s1), s1[0], s1[1]) # {1, 2, 4, 5, 7, 'a', 'b'} <class 'str'> { 1


#### set -> list ###

set2 = {4, 7, 2, 7, 12, 2, 4}
list1 = list(set2)
print(list1, type(list1))  # [2, 4, 12, 7] <class 'list'>

### set -> tuple ###
set3 = {4, 7, 2, 7, 12, 2, 4}
tup2 = tuple(set3)
print(tup2, type(tup2))  # (2, 4, 12, 7) <class 'tuple'>

### set -> dict ### # conversion is not possible
"""
set4 = {4, 7, 2, 7, 11, 44}
d1 = dict(set4)
print(d1)
"""
# TypeError: cannot convert dictionary update sequence element #0 to a sequence

### set -> boolean ###

set4 = set()
b1 = bool(set4)
print(b1, type(b1))  # False <class 'bool'>

set5 = {4, 6, 2, 6, 7, 2}
b2 = bool(set5)
print(b2, type(b2))  # True <class 'bool'>

################### Boolean Data Type Conversion ##########
# bool -> int
print("_"*50)
b1 = True
n1 = int(b1)
print(n1, type(n1))  # 1 <class 'int'>

######## bool -> float ##########
print("_"*50)
bool2 = False
b2 = float(bool2)
print(b2, type(b2))  # 0.0 <class 'float'>

#### Bool - string ###
b3 = True
s1 = str(b3)
print(s1, type(s1), s1[0])  # True <class 'str'> T

#### Bool - List ### : conversion  is not possible
"""
b4 = False
l4 = list(b4)
print(l4)
"""
# TypeError: 'bool' object is not iterable

### bool -> tuple ###  : conversion  is not possible
#### bool -> dict #### : conversion  is not possible
"""
b5 = False
di1 = dict(b5)
print(di1, type(di1))
"""
#### bool -> set #### : conversion  is not possible

b5 = False
di1 = dict(b5)









