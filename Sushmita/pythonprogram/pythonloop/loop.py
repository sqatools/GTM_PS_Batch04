"""
# range function accept three parameter start_value and end_value and dofference.
then output for loop will always exclude the last_value

for i in range(start_value, end_value, difference)
    print(i)

"""

for i in range(1, 11, 2):
    print(i)

# range with two parameter, the default different value will be 1
print("_" * 50)

for j in range(2, 20):
    print(j)

# range with one parameter, then the default initial value will be zero and difference is One
print("_" * 50)
for k in range(5):
    print(k, end=" ")

print()
print("Hello world")
print("Python")

##### Print reverse numbers ###

for i in range(10, 0, -1):
    print(i)

########## print table of any given number ####
print("_" * 50)
n = 6

for i in range(1, 11):
    print(n, "*", i, ":", i * n)

###### get all the even numbers from 1 to 20 ####
print("_" * 50)

for j in range(1, 20):
    if j % 2 == 0:
        print(j)

print('-' * 50)

for i in range(1, 20):
    print(i, end=' ')
print(" ")

print(" -" * 50)

list = [1, 2, 3, 4]
len1 = len(list)

print(len1)
for i in range(-1, -len1 - 1, -1):
    print(i, list[i])

print('-' * 50)

str='Sushmita'
for char in str :
    print(char,end=" ")

print(' ')

str1=len(str)
print(str1)
for i in range(-1 ,-str1-1,-1):
    print(i,str[i])

print('_'*50)

dict={'a':123,'b':'sushmita'}
for val in dict.items() :
    print(val)

for k1 ,v1 in dict.items() :
    print("key:",k1 ,'value :',v1)

print('-'*50)

for i in range(1,5):
    print('adress : ',i)
    for j in range(1,4):
        print('package:',j)
        for k1 in range(1,3):
            print('item :', k1)
    print("-"*50)

print('-'*50)

dict2={
    'car' :{
        'suzuki':['s1','s2','s3'],
         'hyundi': ['h1','h2','h3'],
         'Benz':['B1','b2','b3']
            },

    'Bike': {
        'Access':['A1','A2','A3'],
        'Herohond':['H1','H2','H3'],
        'KTM':['k1','k2','k3']

           },

    'Aeroplane':{
        'Indigo':['I1','I2','I3'],
        'Air asisa':['As1','AS2','As3'],
        'Vistara':['v1','v2','v3']
                 }
}

for k1,v1 in dict2.items():
    print(k1)
    for val1,val2 in v1.items():
        print(val1)
        for data in val2:
            print(data)
