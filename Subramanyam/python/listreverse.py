l=[2,4,5,6,1,3,8]
n=[]
for i in range(len(l)-1,-1,-1):
    n.append(l[i])
    #print(l[i],end=" ")
print(n)
print()
print("_"*100)

l1=[1,2,3,4,5,6,7,8,9]
count=len(l1)-1
m=[]
while count >=0:
    m.append(l1[count])
   # print(l1[count],end=" ")
    count-=1
print(m)
print()
print("_"*100)

l2=[1,4,7,2,5,8,3,6,9]
rev=l2[::-1]
print(rev)

print("_"*100)

print("Using reversed: ",list(reversed(l2)))
print("_"*100)
l3=[]
for i in l2:
    l3.append(i)
l3.reverse()
print(l2)
print("Using reverse: ",l3)

for i in l2:
    if i in l3:
        print(True,end=",")
print()
print("_"*100)

lt=[2,1,3,6,5,4,8,7,9]

lt1=[ele for (val,ele) in enumerate(lt) if val not in (2,4,6)]

print(lt1)

lt2=[j for (i,j) in enumerate(lt) if i%2!=0 ]
print(lt2)
print("_"*100)

le=[-1,2,-4,5,-3,6]
le1=[]
for i in le:
    if i >=0:
        le1.append(i)
print(le1)

print("_"*100)
le2=[]
for i in lt:
    if i%3==0 or i%7==0:
        le2.append(i)
print(le2)



str1="python"
for i in range(len(str1)-1,-1,-1):
    print(str1[i],end=" ")


var1=list(reversed(str1))
print(var1)

print("".join(var1))