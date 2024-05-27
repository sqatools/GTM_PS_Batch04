#converting int to float

num=23
var1=float(num)
print(var1,type(var1))

#int-string
num=890
var=str(num)
print(var,type(var))

#int-boolean
num=1
var2=bool(num)
print(var2,type(var2))

#conversion is not possible for
# int-list,tuple,set,dic

# convert float to int
float=678.976
num=int(float)
print(num,type(num))

# convert float to string
float=69.10
var_str=str(float)
print(var_str,type(var_str),var_str[2])

print('_'*50)
# conversion is not possible for float to list,tuple,dic,set
#convert float to bool

a2 = 879.67
b2 = bool(a2)
print(b2, type(b2))

b2 = 0
a2 = bool(b2)
print(a2, type(a2))

'''
#convert str-int
# cannot perform when the str is in word's
str = "welcome"
s2 = int(str)
print(s2, type(s2))
# ValueError: invalid literal for int() with base 10: 'welcome'
'''


str1 = "4567890"
p = int(str1)
print(p, type(p),str1[2])

'''
# #convert str to float
# str = "Welcome"
# var_str = float(str)
# print(var_str, type(var_str), var_str(3))  #not applicable
'''

# #this is not working.
# str_b="8965"
# f2_float = float(str_b)
# print(f2_float, type(f2_float))

# converting string to list
str1="welcome"
list1=list(str1)
print(list1,type(list1), list1[2])

str_list="welcome to python"
list2=list(str_list)
print(list2,type(list2),list2[-1])

print('_'*50)

#converting str to dict
str_val="Hello"
dict_val={str_val:len(str_val)}
print(dict_val, type(dict_val))

'''
 #direct string cannot be converted)
str_dict2="Hello world"
dict_val2 = dict(str_dict2)
print(dict_val2, type(dict_val2))
'''
import json

str6='{"name":"kaashu", "class":"4th", "school":"st.Anns", "Place:Hyderabad"}'
dict3 = json.loads(str6)
print(dict3, dict3["name"])






