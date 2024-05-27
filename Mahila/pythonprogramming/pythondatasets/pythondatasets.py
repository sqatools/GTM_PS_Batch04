
# Integer Data Type ####

I1 = 40
I2 = 345465

print ("value of I1 :",I1 , type(I1))
print ("value of I2 :",I2, type(I2))



print ("-"*50)
"""
Properties of integer

- Integer is immutable data type, once it is defined we can not change it.
- Integer does not have any limit to defined the number. we can defined any long number
  as integer.
- Only whole will be consider as integer.
"""
print ("-"*50)
############################Float Data Type #######
f1 = 0.1
f2 = 23.22
f3 = 4876484.3764844545454
f4 = 5.458476584734354657687879898900
f5 = 23245454667576878798988989.345465

print("value of f1 : ",f1,type(f1))  #0.1 <class 'float'>
print("value of f2 : ",f2,type(f2))  #23.22 <class 'float'>
print("value of f3 : ",f3,type(f3))  #4876484.376484455 <class 'float'>
print("value of f4 : ",f4,type(f4))  #5.458476584734354 <class 'float'> around 17 numbers will be displayed.
print("value of f5 : ",f5,type(f5))  #2.324545466757688e+25 <class 'float'> if it exceeds 17,shows as exponential.
print ("-"*50)
"""
Properties of integer

- Float is immutable data type, once it is defined we can not change it.
- Float does not have any limit to defined the number. we can defined any long number
  as Float. total number of digit would be around 17 for pointer
- Only pointer values will be consider as float.
"""

print("_" * 50)
########### Complex data type ###########
# x + yj
# x = real number
# y = imaginary number

c1 = 20 + 10j  # <class 'complex'>
c2 = 30 + 4.4j  # <class 'complex'>

c3 = c1 + c2
print("value of c1 :",c1,type(c1))  #(20+10j) <class 'complex'>
print("value of c2 :",c2,type(c2))  #(30+4.4j) <class 'complex'>
print("value of c3 :",c3,type(c3))  #(50+14.4j) <class 'complex'>

###################### Sequentials data type ################
print("_" * 50)
##### String Data Type - sequence of characters enclosed in a quotes ' & "  ################

str1 = ''  # <class 'str'>   --- null value also inside cots,considered as string
str2 = "2"  # <class 'str'>
str3 = 'Hi using python for programming'    #string inside single cots
str4 = "is learning python easy? yes it is.."  #string inside double cots
str5 = 'My name is "Rahul" and living is mumbai' #string inside single cot with a word inside double cots.
str6 = "My name is 'Aditya' and living is mumbai"
#we cannot use same cots for both scenario. eg:if ur giving single cots for writing string then inside the string you can only use double cots.. otherwise it will throw error.
str7 = '''
Python Programs or Python Programming Examples for 
beginners and professionals with programs on basics, 
controls, loops, functions, native data types etc.
‎Python Arithmetic Operations · 
‎Hello Python Program · ‎Python Area Of Triangle
'''
#to print paragraphs in our own order we can use ''' or """
str8 = """
Python Programs or Python Programming
Examples for beginners and 
professionals with programs
on basics, controls, loops, 
functions, native data types etc.
64356546456456 ^&^*&%^&%^&%&^%&%^$^%$
"""
str9 ="D"
str10 ='hello python learner "rahul",hope you are doing well........'
print("str1 :", type(str1), str1)
print("_" * 50)
print("str2 :", type(str2), str2)
print("_" * 50)
print("str3 :", type(str3), str3)
print("_" * 50)
print("str4 :", type(str4), str4)
print("_" * 50)
print("str5 :", type(str5), str5)
print("_" * 50)
print("str6 :", type(str6), str6)
print("_" * 50)
print("str7 :", type(str7), str7)
print("_" * 50)
print("str8 :", type(str8), str8)
print("_" * 50)
print("str9 :", type(str9), str9)
print("_" * 50)
print("str10 :", type(str10), str10)
print("_" * 50)

str1 = "pycharm"

"""
#string has positive index and as well as negative index. positive index starts with 0,1,2... and
#negative index starts with -1,-2.....
0   1  2   3  4  5  6  #+ve index
p   y  c   h  a  r  m 
-7 -6 -5 -4 -3 -2 -1  #-ve index
"""
print(str1[1])  #y
print(str1[3])  #h
print(str1[5])  #r
print(str1[-2]) #r
print(str1[-4])  #h
print(str1[-7])  #p
print(str1[0])  #p

print("_" *50)

str2 = "Good Morning"

print(str2[4])   #  space
print(str2[0])   #G
print(str2[-2])  #n
print(str2[-5])  #r
#if we have any space between the strings the spaces will also count for index positions.
"""
# Properties of String
- String is immutable data type, once it is defined we can not change it.
- String follows both positive and negative indexing.
- String can contains any type of value in double/single quote
"""

print("_" * 50)


############ List ############

lis1 = [ 2, 0.2 , "hello" , [3,4,5], (2.3,"hello")]
print (lis1 , type(lis1))
print (lis1[-1],type(lis1[-1]))  #(2.3, 'hello') <class 'tuple'>
print(lis1[2],type(lis1[2]))     #hello <class 'str'>
print("_" * 50)

list2 = [
    'Hello',  # 0 # -7
    'Good Morning',  # 1 #-6
    4534543,  # 2 # -5
    56.66,  # 3 # -4
    [4, 6, 7, 8],  # 4 # -3
    (4, 7, 2, 22),  # 5 # -2
    {'a': 123, 'b': 345},  # 6 # -1
]

print(list2)  #['Hello', 'Good Morning', 4534543, 56.66, [4, 6, 7, 8], (4, 7, 2, 22), {'a': 123, 'b': 345}]
s1 = list2[0]
print(s1, type(s1), s1[0])  # Hello <class 'str'> H
print(list2[6], type(list2[6]))  # {'a': 123, 'b': 345} <class 'dict'>

print("_" * 50)
str1 = "Hello \n Good \n Morning"   #\n for next line
print(str1)

str2 = "Hello \t \t Good \t\t Morning"  #\t for tab space
print(str2)

print("_" * 50)

p = [44, 77, 88]
list3 = [4, 6, 7, [5, 7, 8], p, True]
p2 = list3[3]
print("p2 value :", p2)
p2.append(100)   #appending value to 100 af position 3

print(list3)
print(list3[-1])

# get value of child list
print(list3[3][1])  # 7

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
set1 = {1, True, False, 0, 3.5, 'Python', 4, 5, (5, 6, 7), 4, 3.5}  # <class 'set'>

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
