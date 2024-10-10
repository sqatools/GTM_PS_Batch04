"""
lista=[4,6,8,3,7,11,14]
output=[]
for char in lista:
    if char%2==0:
        output.append(char**2)
    else:
        output.append(char ** 3)
print(output)

lista=[4,6,8,3,7,11,14]
listb=[3,30,6,20,7,80,1,4]
listc=lista+listb
print(listc)
"""
#5). Python program to find the minimum and maximum elements from the list.
"""
lista=[4,6,8,3,7,11,14]
#print(min(lista))
max=0
min=len(lista)
#print(min)
for char in lista:
    if char>max:
        max=char
    elif char<min:
        min=char
    else:
        continue
print("maximum value:",max)
print("minimum value:",min)
"""
#7). Python program to remove all duplicate elements from the list.

lista=[4,6,8,3,4,8,14]
a=[]
for val in lista:
    if val not in a:
        a.append(val)



print(a)

