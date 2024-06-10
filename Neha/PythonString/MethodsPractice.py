a = "Hi"
print(a, type(a))


b = 'Good Morning'
print(b, type(b))

c = """
I am Neha and
I am living in Nagpur
"""
print(c, type(c))

d = '''
I am Smera and
I am living in Nagpur'''
print(d, type(d))

Str_1 = "PROGRAMMING"
print(Str_1[2])             #O
print(Str_1[-2])            #N

print("_"*50)
for var1 in Str_1:
    print(var1)

print("_"*50)
a = 'Hi'
b = 'Have a good day'
c = a+" "+b
print(c)                    #Hi Have a good day

name = "Neha"
age = "28"
city = "Nagpur"

Result = "My name is "+name+" and age is "+str(age)+" and i live in "+city
print(Result)
Result1 = "My name is {} and age is {} and i live in {}".format(name, age, city)
print(Result)
Result2 = f"My name is {name} and age is {age} and i live in {city}"
print(Result)
#My name is Neha and age is 28 and i live in Nagpur

print("_"*50)
