"""
# range function accept three parameter start_value and end_value and dofference.
then output for loop will always exclude the last_value

for i in range(start_value, end_value, difference)
    print(i)

"""

for i in range(1, 11, 2):
    print(i)

# range with two parameter, the default different value will be 1
print("_"*50)

for j in range(2, 20):
    print(j)

# range with one parameter, then the default initial value will be zero and difference is One
print("_"*50)
for k in range(5):
    print(k, end=" ")

print()
print("Hello world")
print("Python")


##### Print reverse numbers ###

for i in range(10, 0, -1):
    print(i)


########## print table of any given number ####
print("_"*50)
n = 6

for i in range(1, 11):
    print(n, "*", i, ":",i*n)


###### get all the even numbers from 1 to 20 ####
print("_"*50)

for j in range(1, 20):
    if j%2 ==0:
        print(j)

# apply loop of list of values
print("_"*50)
list1 = [3, 6, 1, 7, 22, 44]
for val in list1:
    #print(val)
    if val%2 == 0:
        print(val,":", val**2)
    else:
        print(val,":", val**3)


print("_"*50)
list_len = len(list1)
for i in range(-1, -list_len-1, -1):
    print(i, list1[i])
"""
-1 44
-2 22
-3 7
-4 1
-5 6
-6 3
"""


####### Apply loop on string values ######
print("_"*50)
str1= "Python Program"

for v1 in str1:
    print(v1,end="")

print()

str_len = len(str1)
print("total length :", str_len)
for i in range(-1, -str_len-1, -1):
    print(str1[i], end="")

"""
total length : 14
margorP nohtyP
"""


######### apply loop on dictionary #######
print("_"*50)
dict1 = {'a' : 123, 'b': 345, 'c' : 678}
for val in dict1.items():
    print(val)
"""
('a', 123)
('b', 345)
('c', 678)
"""


for k1, v1 in dict1.items():
    print("key :", k1, "value :", v1)
"""
key : a value : 123
key : b value : 345
key : c value : 678
"""


############# Nested Foor Loop #######
print("_"*50)

for i in range(1, 6):
    print("address :i:", i)
    for j in range(1, 4):
        print("package: j :", j)
        for k in range(1, 3):
            print("item: k :", k)

    print("_"*40)



print("_"*50)
dict1 = {
    'teaching': {
        'math' : ['m1', 'm2', 'm3', 'm3'],
        'physics' : "Programming",
        'hindi' : ('h1', 'h2', 'h3'),
    },
    'account' : {
        'account1' : '123',
        'account2' : ['acc2a', 'acc2b', 'acc2c'],
        'account3' : ['acc3a', 'acc3b', 'acc3c'],
    },
    'student' : {

        '9th' : ['9a', '9b', '9c'],
        '10th' : ['10a', '10b', '10c'],
        '11th' : ['11a', '11b', '11c']
    }
}


for keys, value in dict1.items():
    print(keys)
    for k1, v1 in value.items():
        print(k1)
        for data in v1:
            print(data, end=" ")
        print("="*40)

    print("="*50)


for i in range(1, 6):
    print(i*"@*@")
for i in range(4, -1, -1):
    print(i*"@*@")







