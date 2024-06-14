#print(dir(tuple))
'''
tup1=(1,23,4,5,3,3,3,4)
#print(tup1.count(3))
print(tup1.index(4))-------------doubt


for i in range(len(tup1)):
    print(i,tup1[i])
'''
tup2=(4,6,8,1,18,25,35)
print(tup2[2:7])
print(tup2[1:7:2])
print(tup2[-1:5:1])
print(tup2[-3::1])

tup4= (4,6,8,1,18,2,6,2,6,2,7)
#del tup4[2:5]

dict1= {'a': 123,'b': 45,'c':  464}
dict1['d'] = 600
print(dict1)

for i in dict1.items():
    print(i)

print(dir(dict))

print(dict1.get('a'))
print(dict1.keys())
print(dict1.values())
dict2={ 'p':111,'q':222,'r':333}
dict2.update(dict1)
print(dict2)
print(dict1)

dict2.pop('p')
print(dict2)
dict2.popitem()
print(dict2)