list1=[3,5,7,1,8]

for i in list1:
    print(i,":",i**2 )

list2=[5,6,8,3,2,1]

output=list1+list2
print(output)

list1.extend(list2)
print(list1)

var=0

for val in list2:
    var+=val
print(var)

lst=[1,2,3,6,5,4]
var=1
for val in lst:
    var*=val

print(var)

list2.sort()
print("smallest: ",list2[0])
print("largest: ",list2[-1])

even_odd=[12,33,15,16,90,89]

even=[]
odd=[]

for i in even_odd:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print("even numbers: ",even)
print("odd numbers: ",odd)


lst1=[1,3,5,8,7,4,6,5,2]

stl=[]

for i in lst1:
    if i not in stl:
        stl.append(i)

print(stl)

import itertools

var1=10

vit=[]

for i in range(len(lst1)):
    for combi in itertools.combinations(lst1,i):
        if sum(combi)==var1:
            vit.append(combi)

print(vit)


even=[]
odd=[]

for i in lst1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

odd.extend(even)
print(odd)


dup1=[4,5,2,6,3,1]
dup2=[5,1,9,7,8,0]

com=[]

for i in dup1:
    if i  in dup2:
        com.append(i)


print(com)

for i in range(len(dup2)-1,-1,-1):
    print(dup2[i],end=" ")
print()
count = len(dup2)-1
while count >=0:
    print(dup2[count],end=" ")
    count-=1
print()
l=[2,3,4,5,6,7,8]
for i in l:
    if i%2==0:
        print(i,":",i**2)

print()

ls1=[2,3,4,5,6]

ls2=ls1[::-1]

print(ls2)


print("using reversed:",list(reversed(ls1)))

ls1.reverse()
print("using reverse: ",ls1)

l1=[]

for i in ls1:
    l1.append(i)
print(l1)

for i in dup1:
    if i in dup2:
        print(True)

lt=[3,5,7,8,6,9,2,1]

lt=[element for (value,element) in enumerate(lt) if value not in (2,4,6) ]

print(lt)

lt1=[1,2,3,-5,5,1,-6,-5,1]
for i in lt1:
    if i>=0:
        print(i,end=" ")
print()
lt2=[]
for i in lt:
    if i%3==0 or i%7==0:
        lt2.append(i)

print(lt2)


lista=[4,6,8,3,7,11,14]
output=[]

for i in lista:
    if i%2!=0:
        output.append(i**3)
    else:
        output.append(i**2)

print(output)


#lista.sort(reverse=True)
output1=[(num**2) if num%2==0 else (num**3) for num in lista]
print(output1)

listb=[2,3,4,5,2,3,4,6,7,8,9]
op=[]
for i in listb:
    if i not in op:
        op.append(i)
    else:
        continue
print(op)


op1=set(listb)
print(list(op1))


list2 = [2, -1, 5, -4, -7, 12.23, 51, 25, -8]
li=[]
for i in list2:
    if i>0:
        li.insert(0,i)
    else:
        li.append(i)

print(li)


list_b = [3, 30, 6, 20, 7, 80, 1, 4]

for i in range(len(list_b)):
    for j in range(i+1,len(list_b)):
        if list_b[i]>list_b[j]:
            temp=list_b[i]
            list_b[i]=list_b[j]
            list_b[j]=temp

print(list_b)

ls=[1,2,3,4,5]
count=1
for i in ls:
    count*=i

print(count)
# total=0
# while count<len(ls):
#     total+=ls[count]
#     count+=1
# print(total)
final=[]

for (a,b) in zip(lista,list_b):
    final.append(list((a,b)))

print(final)

print(["sqa{0}".format(value) for value in ls])