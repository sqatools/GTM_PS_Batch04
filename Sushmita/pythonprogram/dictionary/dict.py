list1=[4,7,2]
dict={}
for i in list1:
    if i%2==0:
       dict[i]=i**2
    else:
        dict[i]=i**3

print(dict)
