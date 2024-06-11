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
