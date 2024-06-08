str1 = 'Hello'
str2 = "Python Programming"
str3 = """
We are learning Python Programming
its very easy to learn
"""

print(str1, type(str1))
print("_" * 50)
print(str2, type(str2))
print("_" * 50)
print(str3, type(str3))

str5 = "PROGRAM"

"""
0  1  2  3  4  5  6  +ve
P  R  O  G  R  A  M
-7 -6 -5 -4 -3 -2 -1 -ve
"""

print(str5[3])  # G

print(str5[-4])  # G

print("_" * 50)

for var1 in str5:
    print(var1)

################
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

result = "My name is "+name+" and age is "+str(age)+" and I live in "+city
print(result)

# 2. format method:
result1 = "My name is {} and age is {} and I live in {}".format(name, age, city)
print(result1)

# 3. fstring formatting:
city_list = ['Mumbai', 'Pune', 'Bangalore']
result2 = f"My name is {name} and age is {age} and I live in {city_list[0]}"
print(result2)


print("_"*50)
########## slicing in the string ##########

# Rule1 : str1[start_index : end_index]
# In this rule the last index value is always going to ignore
# substring will contain data from left to right index position.

str1= "Python Programming"
result = str1[0:6]
print("result:", result) # Python

# positive and negative index
output2 = str1[1: -1]
print("output2 :", output2) # ython Programmin

output3 = str1[-1:1]
print("output3 :", output3)  # blank

output4 = str1[3: 9]
print("output4 :", output4)  # hon Pr

output5 = str1[-6:-1]
print("output5 :", output5) # ammin

output6 = str1[-6:-5] # blank
print("output6 :", output6) #


#################################
# Rule2 : str1[:last_index]
# In this rule default initiate index will be zero and last index will be excluded.

str_a = "Good Morning"
print(str_a[:5])  # Good
print(str_a[:-2]) # Good Morni

####################
print("_")
# Rule3 : str1[initial_index:]
# the default value of last index will be end of string.

str_b = "Learning Python"
print("output1:", str_b[4:])  # ning Python
print("output2:", str_b[-5:])  # ython

###########################
print("_"*50)
# Rule4 : str1[initial_index : end_index : difference]
# In this user to has to defined initial index, end index and difference value
# Here also output does not contain the end index value.

str_c = "India is best cricket team"
output1= str_c[2: 10: 1]
print("output1 :", output1)  # dia is b

output2 = str_c[-1: -15: -1] # maet tekcirc t
print("output2 :", output2)

output3 = str_c[-1: -15: -2] # me ecr
print("output3 :", output3)

# output4 = str_c[1: -10: 1]
# print("output 4 :", output4)  # ndia is best cr


######################
