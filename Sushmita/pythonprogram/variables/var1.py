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
#########Integer#############
##########int->float#########
v1=45
v2=float(45)
print(v2)


#int->string

v3=str(v1)
print(v3 ,type(v3))

#int->tuple conversion is not possibe
#int->list conversion is not possibe
#int->dict conversion is not possible
#int->set conversion is not possible

v4=bool(v1)
print(v4,type(v4))

############float##############
print("-"*50)
#float->int
f1=43.2
f2=int(f1)
print(f2,type(f2))

#float->string

f3=str(f1)
print(f3,type(f3))

#float->list is not possible
#float->tuple is not possible
#float->dict is not possible
#float->set is not possible

#float->bool

f5=0.0
f5=bool(f5)
print(f5,type(f5))

################String#####################

print('-'*50)

#string->int

#If string contains only number conversion is possible

s1='456'
s2=int(s1)
print(s2,type(s2))

#str->float

s3=float(s1)
print(s3,type(s3))

#str->list

s4='string'
s5=list(s4)
print(s5,type(s5))
print(s5[4])

#str->tuple
s6=tuple(s4)
print(s6,type(s6))

#str->dict

#string to dict direct conversion is not possible
import json

str5 = '{"Name" : "Rahul", "age" : 25, "address" : "Pune"}'
dict2 = json.loads(str5)
print(dict2, dict2['Name'])

#str->set

str1="program"
s6=set(str1)
print(s6,type(s6))
