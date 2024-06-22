#Dictionary program to add elements to the dictionary.
dict={ }
dict['name']='sush'
dict['add']='shastri'
print(dict)

print('_'*50)
#Python Dictionary program to print the square of all values in a dictionary.
dict1={'a':5, 'b':3, 'c': 6, 'd':8}
for val in dict1:
    print(val,':',dict1[val]**2)


print('_'*50)
#Move items from one dictionary to another.
dict2={'a':'sush','b':'shastr'}
d2={}
for val in dict2:
     d2[val]=dict2[val]
print(d2)

print('_'*50)
#Program to concatenate two dictionaries
D1={'name':'sush','add':'lingasugur','b':50}
D2={'c':40,'e':90}

D2.update(D1)
print(D2)


print('_'*50)
#Python Program to create a dictionary from two lists

list1=['a','b','c','d']
list2=[20,30,40,43]
dict3={}

for k,v1 in zip(list1,list2):
    dict3[k]=v1
print(dict3)

print('_'*50)
#Store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.
list3=[4,5,3,2,1]
dict4={}

for val in list3:
    if val%2==0:
        dict4[val]=val**2
    else:
        dict4[val]=val**3
print(dict4)

print('_'*50)
#Python program to create a dictionary from the string.
string='python'
dict_a={}
for char in string:
    dict_a[char]=string.count(char)

print(dict_a)

print('_'*50)
#Python program to add a key in a dictionary.
dict_b={'a':10,'b':20}
dict_b.update({'c':40})
print(dict_b)

print('_'*50)
#Program to swap the values of the keys in the dictionary.
dict_c={'name':'sush','age':'25'}
d2={}
for key,value in dict_c.items():
    d2[value]=key
print(d2)

#Get the sum of all the items in a dictionary.
d1={'a':10,'b':20}
count=0
for val in d1.values():
    count=count+val
print(count)
