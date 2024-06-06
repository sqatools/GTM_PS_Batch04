"""String is a sequantial data
it follows the posotive and negative index
anything declared in singl double and triple cotes is known as string"""

s1 = 'Hello'
s2 = "Hi"
s3 = "Hyfy"

print("s1",type(s1))
print("s2",type(s2))
print("s3",type(s3))

Str1 ="PROGRAMMING"

print(Str1[2])
print(Str1[-9])

for v in Str1:
    print(v)

#Sting formatting


name = "Rahul"
age = 25
city = "Mumbai"

#1. String concatination (We can add two string using + operator)

v1 = 'hello'
v2 = 'Good morning'
v3 = v1 + " " + v2
print(v3)

result = "My name is "+name+" and age is "+str(age)+" and i live in"+city
print(result)

# here we converted the integer data type into sring by str(age)

#2. Format method by using {}
result1 = "My name is {} and age is {} and i live in {}".format(name, age, city)
print(result1)

# 3. f string formatting:
result2 = f"My name is {name} and age is {age} and i live in {city}"
print(result2)

city_list = ['Mumbai', "pune","Delhi"]
result3 = f"My name is {name} and age is {age} and i live in {city_list[0]}"
print(result3)


# String slicing
#Rule1 : str1[strtingindex : ending indes]
#last index will always be trimmed

Str1 = "Python Programminng"
result4 = Str1[0:6]
print("result4:",result4)

#positive and negative index

output1 = Str1[1 :-1]
print(output1)


output2 = Str1[-6 :-1]
print(output2)





