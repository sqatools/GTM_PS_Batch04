#Problem to add elements to set in python
a={1,2,3,4,5}
a.add(6)
print('set elements:',a)

print('_'*50)
#Python program to remove an element from a set.
b={1,2,3,4,7}
result=b.remove(4)

print('set elements:',b)

print('_'*50)
#Python program to find the length of a set.
c={1,2,3,5}
length=len(c)
print(length)

print('_'*50)
#Python program to find the union of two sets.
a1={2,3,'Hello'}
a2={4,5,6,7}
a3=a1.union(a2)
print('union set:',a3)

print('_'*50)
#Python program to find the intersection of two sets.

b1={1,45,66,77,23}
b2={23,66,2,7}
print('intersection of set:',b1.intersection(b2))

print('_'*50)
#Python program to find the difference of two sets.
print('difference os set:',b1.difference(b2))
print('difference os set:',b2.difference(b1))

print('_'*50)
#Python program to find the symmetric difference of two sets.
print('symetric differnce:',b1.symmetric_difference(b2))

print('_'*50)
#Python program to show if one set is a subset of another set.
c1={1,2,3,4,5}
c2={3,4}
print('subset:',c2.issubset(c1))

print('_'*50)
#Python program to convert a list to a se

list1=[2,3,4,5]
print('set:',set(list1))

print('_'*50)
#Python program to find the sum of elements in a set.
set1={2,3,4,1}
sum=0
for ele in set1:
    sum=sum+ele
print('sum:',sum/len(set1))

print('_'*50)
#Problem to check if elements in a set are prime
set1={33,44,61,2}
prime=[]
for ele in set1:
    count=0
    for num in range(2,ele):
        if ele%num==0:
           count=count+1
    if count==0:
        prime.append(ele)
#print(prime)
if len(prime)==len(set1):
    print('All the elements in set are primre')
else:
    print('all the elements in set are not prime')

print('_'*50)
#Add multiple element to set:
a={1,2,3,4}
b={5,6,7}
for ele in b:
    a.add(ele)
print('added ele:',a)

#find the longest word in a set
set1={'I','AM','Learning','Python'}
max_len=0
max_word=0
for word in set1:
    if len(word)>max_len:
        max_len=len(word)
        max_word=word
print(max_word)
print(max_len)
