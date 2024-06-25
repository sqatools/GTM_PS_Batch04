list1=[3,5,2,4]
for val in list1:
    print(val,':',val**2)

print('_'*50)

list2=[2,4,5]
list3=[4,5,6]
list2.extend(list3)
print(list2)

print('_'*50)

list_a=[3,4,5,6]
var=0
for val in list_a:
    var=var+val
print(var)


#Differentiate even and odd number in list:
print('_'*50)
list_b=[2,5,90,32,33,54]
odd=[]
even=[]

for val in list_b:
    if val%2==0:
        even.append(val)
    else:
        odd.append((val))
print(even)
print(odd)

#remove all the duplicate elements from a list.

print('_'*50)

list_c=[2,4,5,6,2,5,8,4]

list3=[]

for val in list_c:
    if val not in list3:
        list3.append(val)
print(list3)

#get common elements from two lists.

list_1=[1,4,3,2,8,10]
list_2=[10,3,5,4,2,6]

common_list=[]

for val in list_1:
    if val in list_2:
        common_list.append(val)
print(common_list)


#get a list of words which has vowels in string.

string1='the woed is vowel'
vowel=['a','e','i','o','u']
emp_string=[]
string_a=string1.split()

for word in string_a:
    for char in word:
        if char in vowel:
            emp_string.append(word)
print(emp_string)
