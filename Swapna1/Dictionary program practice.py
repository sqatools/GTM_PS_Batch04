"""Python program to add elements to the dictionary"""
dic = {}
dic["Name"]="Swapna"
dic["Age"]="30"
dic["Location"]="Blore"
print(dic)
print("_" *50)
"""Print the square of all values in a dictionary."""

dic1={'a':2, 'b':3,'c':5}
for i in dic1:
    print(i,":",dic1[i]**2)
print("_" *50)


"""Move items from one dictionary to another."""

dic3={'Name':'Swapna', 'Location':'Blore','Working at':'TCS'}
dic4={}
for a in dic3:
    dic4[a]=dic3[a]
print(dic4)
print("_" *50)

"""Program to concatenate two dictionaries"""
d1={'name': 'Swapna', 'Age':'30'}
d2={'Coun  try':'India', 'passport':'Yes'}
d1.update(d2)
print(d1)
print("_" *50)

"""Program to get a list of odd and even keys from the dictionary"""
d4={1:'we',3:"qwe", 4:'poa',6:90}

for b in d4:
    if b%2==0:
        print("Even keys:",b,d4[b])
    else:
        print("Odd keys:",b,d4[b])

print("_" *50)
"""Python Program to create a dictionary from two lists."""
l1=["hi",3,'hello']
l2=[78,89,90]
dic0={}
for x,y in zip(l1,l2):
    dic0[y]=x
print(dic0)
print("_"*50)
"""Store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension."""
l0=[2,4,6,3,5]
d1={}
for y in l0:
    if y%2==0:
     d1[y]=y**2
    else:
        d1[y]=y**3
print(d1)
print("_"*50)

"""Python program to clear all items from the dictionary."""
a={'Name':'Swapna', 'Location':'Blore','Working at':'TCS'}
a.clear()
print(a)

print("_"*50)
"""Python program to remove duplicate values from Dictionary."""

a1={'Name':'Swapna', 'Location':'Blore','Working at':'TCS', 'Working at':'TCS'}
a2={}
for key, value in a1.items():
    if a1 not in a2.values():
        a2[key]=value
print(a2)
print("_"*50)





