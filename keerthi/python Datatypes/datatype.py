#integer:
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
#integer
"""
Properties of integer

- Integer is immutable data type, once it is defined we can not change it.
- Integer does not have any limit to defined the number. we can defined any long number
  as integer.
- Only whole will be consider as integer.
"""

a=78
b="helloworld"
c=3544658798090567689704656576

print("value of a:", type(a))
print("value of b:", type(b))
print("value of c:", type(c))

a=7.8
b=12.8
c=3445667.687989000243356
print("value of a:", type(a))
print("value of b:", type(b))
print("value of c:", type(c))

#float data type
a=2.0
b=90.7909
d=-29.789
e=67780099.89090999090
f=34565.7988099055879898675766
g=989008788788677777.6878898788
print("value of a:", a,type(a))
print("value of b:", b,type(b))
print("value of c:", c, type(c))
print("value of d:", d,type(d))
print("value of e:", e,type(e))
print("value of f:", f,type(f))
print("value of g:", g,type(g))

print("*"*50)
#complex numbers
#a+bi
#a=realnumber
#b=imaginary

a=20+10j
b=30+3.8j
c=a+b
print("value of c:",c)
print("*"*50)
var1=10+30j
var2=30+50j
var3=var1+var2
print("value of var3:", var3)
print("value of var1:", var1,type(var1))
print("value of var2:",var2,type(var2))

print('-'*50)
####sequential datatype
"""
# Properties of String
- String is immutable data type, once it is defined we can not change it.
- String follows both positive and negative indexing.
- String can contains any type of value in double/single quote
"""

str1='' #if we give '' it will consider this is a string
str2='678'
str3="helo"
str4="this is my pythonfirst program"
str5="i live in a SD road,near by the school."
str6='"hai, how are you"'
str7='''
Python Programs or Python Programming Examples for 
beginners and professionals with programs on basics, 
controls, loops, functions, native data types etc.
‎Python Arithmetic Operations · 
‎Hello Python Program · ‎Python Area Of Triangle
'''
str8='''
Python Programs or Python Programming
Examples for beginners and 
professionals with programs
on basics, controls, loops, 
functions, native data types etc.
64356546456456 ^&^*&%^&%^&%&^%&%^$^%$
'''
print("str1 of str:",type(str1),str1)
print("-"*50)
print("str2 of str:",type(str2),str2)
print("_"*50)
print("str3 of str:",type(str3),str3)
print("_"*50)
print("str4 of str:",type(str4),str4)
print("-"*50)
print("str5 of str:",type(str5),str5)
print("_"*50)
print("str6 of str:",type(str6),str6)
print("_"*50)
print("str7 of str:",type(str7),str7)
print("_"*50)
print("str8 of str:",type(str8),str8)

var1="python"
#  p   y   t   h   o   n
#  0   1   2   3   4   5
# -6  -5  -4  -3  -2  -1

# print(var1[2,1])
# print(var1[-3])

var2="Welcome"
print(var2[1])
print(var2[-5])

var3="35465"
print(var3[1])
print(var3[-2])

# ***********List**********"""
# """
# Properties of List
#
# - List if mutable data type, we can modify at any point of time
# - List follows positive and negative indexing as like string
# - List can contain any type of data like int, float, string, list, tuple, dict, set, Boolean.
# """

list1 = [1,2,3,[4,5,6],"welcome"]
print(list1, type(list1))

list2=[3,5,8,"hello",(4,5,6)]
print(list2, type(list2))

list3=[
    "hello",
    "This is hello world",
    2.3,4.6,7.9,
    [2,3,4,5],
    (6,7,8,9,10),
    {'a':112,'b':113,'end':'3578'}
]
print(list3,type(list3),list3[4])

s1=list3[0]
print(s1, type(s1),s1[0])
print(list3[-1],type(list3[-1]))

print('_'*50)
str1="hello \n welcome to \n python"
print(str1, type(str1))

str2="Good \t\t morning \t\t hyderabad"
print(str2, type(str2))

print('_'*50)

p=[2,3,4]
list1=[7,8,9,[8,9,6],p,0]
# print(list1, type(list1))
p2=list1[4]
print("value of p2:",p2)
p2.append(100)










