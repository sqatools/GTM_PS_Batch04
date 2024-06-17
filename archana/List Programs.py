list1=[1,2,3,4]
for val in list1:
    print(val**2)


list2=[2,3,4,5]
list3=[4,56,7,9]
output= list2+list3
print(output)

list4=[3,4,5,6,7,8]
sum1= sum(list4)
print(sum1)

list5= [1,2,3,4]
var= 1
for i in list5:
    var= var* i
print(var)

list6=[34,56,43,22]
b= max(list6)
c= min(list6)
print(b)
print(c)

list7= [2,1,3,5]
even=[]
odd=[]
for i in list7:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

list8= [3,2,3,4,5,2]
list9=[]
for val in list8:
    if val not in list9:
        list9.append(val)
print(list9)

print("-"*50)
list10=[1,2,6,4,5,9]
for i in list10:
    if i%2==0:
        print(i**2)

print("-"*50)
lista=[1,2,3,4,5,6,7]
even=[]
odd=[]
for i in lista:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
odd.extend(even)
print(odd)

list11= [4,5,7,9,2,1]
list12=[ 2,5,8,3,4,7]
common_list=[]
for val in list11:
    if val in list12:
        common_list.append(val)

print(common_list)

print("-"*50)
list13= [3,4,5,3,2,8]
for i in range(len(list13)-1,-1,-1):
    print(list13[i],end=" ")

print("-"*50)
list14= [1,2,3,4,5,6,8]
count= len(list14)-1
while(count>=0):
    print((count))
    count=count-1

print("-"*50)
list15=[1,2,3,4,5,6]
list15.reverse()
print(list15)

print("-" *50 )
output= (list(reversed(list15)))
print(output)

list16= [2,3,4,5,6,7]
list17=[]
for u in list16:
    list17.append(u)
print(list17)

list18=[2,3,4,5,6,8]
list19=[2,3,4,6]
for i in list18:
    if i in list19:
        print("True")

list20= [1,2,3,4,5,6,7]

list21= [3,5,-1,-2,3,-5]
for u in list21:
    if u>=0:
        print(u,end=",")

print("-"*50)
list22= [3,7,6,4,3,2]
list23=[]
for i in list22:
    if i%3==0 or i%7==0:
        list23.append(i)
print(list23)


