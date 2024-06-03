# range function accept three parameter start_value and end_value and dofference.
# then output for loop will always exclude the last_value
#
# for i in range(start_value, end_value, difference)
#     print(i)
# (first val,end value, difference)

for i in range(1,10):
    print(i)

# range with two parameter, the default different value will be 1
print("_"*50)
for i in range(10):
    print(i)

for i in range(10,1):
    print(i)

# range with one parameter, then the default initial value will be zero and difference is One
print("_"*50)
for k in range(5):
    print(k, end=" ")

print()
print("Hello world")
print("Python")

##### Print reverse numbers ###
for i in range(10,2,-1):
    print(i)

for i in range(20,1-2):
    print(i)

########## print table of any given number ####
n=3

for i in range(1,11):
    print(n,"*", i,":",i*n)

###### get all the even numbers from 1 to 20 ####
    print()
for k in range(1, 20):
    if k % 2 == 0:
        print(k,end=" ")

print()

print("_"*50)
# apply loop of list of values
list=[1,2,3,4,5,6,7,8,9,10]
for i in range(1, 10):
    print(i,end=" ")

print("*" * 50)

list1 = [3, 6, 1, 7, 22, 44]
for val in list1:
    #print(val)
    if val%2 == 0:
        print(val,":", val**2)
    else:
        print(val,":", val**3)


print("*" *50)

list2=[9,2,6,4,12,3,18]
for val in list2:
    if val%3==0:
        print(val,":", val**2)
else:
    print(val, ":", val**1)
#for getting list to be printed in reverse order
print("*"*50)
list_len=len(list2)
for i in range(-1,-list_len-1, -1):
    print(i,list2[i])

'''
-1 18
-2 3
-3 12
-4 4
-5 6
-6 2
-7 9
'''

print("*" *50)

Eg:2
tuple=(4,8,9,2,1,5,0)
tuple_len=len(tuple)
for i in range(-1, -tuple_len-1,-1):
    print(i,tuple[i])
'''
-1 0
-2 5
-3 1
-4 2
-5 9
-6 8
-7 4
'''
#apply loop on string values:
print('*' *50)
str1="python programming"
for i in str1:
    print(i, end=" ")

print()

#p y t h o n   p r o g r a m m i n g

str_len=len(str1)
print("total length:", str_len)
for i in range(-1, -str_len-1, -1):
    print(i,str1[i])

str2=[7,5,8,3,4,1]
str_len=len(str2)
print("total length:",str_len)
for i in range(-1,-str_len-1,-1):
    print(i,str2[i])

#for loop in dict.
dict1 = {'a' : 123, 'b': 345, 'c' : 678}
for val in dict1.items():
    print(val)

print(' '*50)
dict2 = {'x' : 123, 'y' : 765, 'z' : 890}
for j in dict2.items():
    print(j)

for k1, v1 in dict1.items():
    print("key:", k1, "value:", v1)

print("_"*50)
for i in range(1,4):
    print("address:i:",i)
    for j in range(1,4):
        print("package:j:", j)
        for k in range(1,3):
            print("item:")
print("_"*50)

print()
dict1={
    'teaching':
        {
         'maths':  ['m1','m2','m3','m4','m5'],
          'science': "python programming",
            'hindi': ('h1','h2','h3'),

           },
    'account':
    {
       'account1' :'456',
       'account2' : ['23fd', 'df67','87ygth'],
        'account3' :{'hgty', 'ythui', 'itee',},
    },
    'student':
    {
            '9th':{'9a','9b','9c'},
            '10th':['6a','6b','6c'],
            '11th':('8a','8b','8c'),
    }


 }

for keys, value in dict1.items():
    print(keys)
    for k1, v1 in value.items():
        print(k1)
        for data in v1:
            print(data, end=" ")
print()

dict2={
    'employee1':
        {
            'Name':'xyz',
            'ID':['4567'],
        }
    'employee2',
    'employee3',

for i in dict2.items():
    print(dict2)









