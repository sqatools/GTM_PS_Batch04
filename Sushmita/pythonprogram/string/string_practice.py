str1='sushmita'
str2="shastti"
str3=""" python program
esy to learn
"""


print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print('_'*50)
str4='PROGRAm'

print(str4[4])
print(str4[-4])

#-------------------------------
for char in str4:
    print(char,end=' ')

# string formatting

name = 'Mohit'
age = 25
city = "Mumbai"

# My name is rahul and age is 25 and I live in mumbai

# 1. string concatenation
v1= 'hello'
v2 = 'good morning'
v3 = v1 +" "+ v2
print(v3)

result="my name is rahul"+name+" and is "+str(age)+" and i live in"+city
print(result)

#2.format method
result1='my name is {} and age is {} and i live in {}'.format(name,age,city)
print(result1)

#3.fsting format method
city_list=['mumbai','delhi']
result2=f'my name is{name} and age is {age} and i live in {city_list}'
print(result2)
print('_'*50)
########## slicing in the string ##########

# Rule1 : str1[start_index : end_index]
# In this rule the last index value is always going to ignore
# substring will contain data from left to right index position.

str5='PYthon program'
''' P Y t h o n p r o g r a m
    0 1  2 3 4 5 6 7 8 9 10 11
   -12-11-10-9 -8 -7   -6  -5  -4  -3    -2  -1'''
s1=str5[0:6]
print(s1)
print('_'*50)

s2=str5[-4:-1]
print(s2)
print('_'*50)
s3=str5[6:11]
print(s3)
print('_'*50)
s4=str5[-7:-6]
print(s4)
print('_'*50)
s6 = str5[-6:-5]
print(s6)

str7= "Python Programming"
output6 = str7[-6:-5] # blank
print("output6 :", output6) #
#################################
# Rule2 : str1[:last_index]
# In this rule default initiate index will be zero and last index will be excluded.

str_a = "Good Morning"
print(str_a[:5])  # Good
print(str_a[:-2]) # Good Morni

####################
print("_"*50)
# Rule3 : str1[initial_index:]
# the default value of last index will be end of string.
str_b = "Learning Python"
s8=str_b[8:]
print(s8)
s9=str_b[-1:]
print(s9)
s10=str_b[-5:]
print(s10)
s11=str5[-5:]
print(s11)

##########################
print("_"*50)
# Rule4 : str1[initial_index : end_index : difference]
# In this user to has to defined initial index, end index and difference value
# Here also output does not contain the end index value.

str_c = "India is best cricket team"
s12=str_c[0:6:1]
print(s12)

print('*'*50)

s13=str_c[-2:-7:-1]
print(s13)
print('_'*50)
#####################
# Rule 5:  str[:end_index:difference]
# default initial index will be zero if difference is positive
# default initial index will be -1 if difference is negative

print('output:',str_c[:6:1])
print('output1:',str_c[:-5:-1])

print("_"*50)
############################
# Rule 6: str1[initial_index::difference]
# default end index would be end of the string if different is +ve
# default end index would be start of the string if different is -ve

str_6="Good Morning"

print('op:',str_6[-1::2]) #g
print('op1:',str_6[3::-1]) #dooG
print('op1:',str_6[1::-1]) #oG

print("_"*50)
###################################
# Rule 7: str1[::difference]
# In this rule default initial index would be zero and
#            end index would be end of string if difference is +ve
# In this rule default initial index would be -1 and
#            end_index would be start of string if difference is -ve

str_7='Good Morning'
print('op2:',str_7[::1])
print('op2:',str_7[::-1])


###################################################
print("_"*50)

# Q1:
str1 = "Python Programming"
# Output1 = "gython ProgramminP"
# Output2 = "PPPython Programminggg"
# Output3 = "Programming Python"

str1='Python Programming'
first_char=str1[0]
last_char=str1[-1]
remchar=str1[1:-1]
str_op=f'{last_char}{remchar}{first_char}'
print('str_op:',str_op)
#"gython ProgramminP"

print('_'*50)

# Output2 = "PPPython Programminggg"
str_op1=f'{first_char*3}{remchar}{last_char*3}'
print(str_op1)
str1 = "Python Programming"
# Output3 = "Programming Python"
first=str1[0:7]
last=str1[7:]
result=f'{last} {first}'
print(result)
