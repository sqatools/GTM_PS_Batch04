str1="Hello Good Morning,Hope you are enjoying learning"
list1=str1.split(" ")
print(list1)
result= {}
for word in list1:
    word_len= len(word)
    result[word]= word_len
print(result)

print("-"*50)

list1=[4,7,3,4,2,1,9]
result= {}
for val in list1:
    if val%2==0:
        result[val]= val**2
    else:
        result[val]=val**3
print(result)

print("-"*50)
dict={}
dict["name"]="archana"
dict["age"]="21"
print (dict)

print("-"*50)
dict1= {'a':5,'b':3,'c':6,'d':8}
for i in dict1:
    print(i,dict1[i]**2)

print("-"*50)
dict2= {'name':'john','city':'London','country':'uk'}
dict3={}
for i in dict2:
    dict3[i]= dict2[i]
print(dict3)

print("-"*50)
dict4={'Name':'Harry','Rollno':345,'address':'Jordan'}
dict5={'age':25,'salary': '25000'}
dict4.update(dict5)
print(dict4)

print("-"*50)
dict5= {1:25,5:'abc',8:'pqr',21:'xyz',12:'def',2:'utv'}
list2= [[i,dict5[i]] for i in dict5 if i%2==0 ]
list3= [[i,dict5[i]] for i in dict5 if i%2!=0]
print("even key:",list2)
print("odd key:",list3)

print("-"*50)
list4=['a','b','c','d','e']
list5= [12,23,45,3,4]
dict6={}
for a,b in zip(list4,list5):
    dict6[a]=b
print(dict6)

print("-"*50)
list6= [4,5,3,2,1,3]
dict7={}
for i in list6:
    if i%2==0:
        dict7[i]=i**2
    else:
        dict7[i]=i**3
print(dict7)

print("-"*50)
dict8={'name':'harry','rollno':123,'address':'jordan'}
dict8.clear()
print(dict8)

print("-"*50)
str6="sqatools"
dict9={}
for char in str6:
    dict9[char]=str6.count(char)
print(dict9)

print("-"*50)
dict10= {'d':21,'b':53,'c':41,'a':13}
for key in sorted(dict10):
    print(key,dict10[key],end=" ")

print("-"*50)
dict11= {1:'a',2:'b'}
dict11.update({3:'c'})
print(dict11)

print("-"*50)
dict12= {'name':'yash','city':'pune'}
dict13= {'course':'python','institute':'sqatools'}
dict12.update(dict13)
print(dict12)

print("-"*50)
dict13= {'name':'yash','city':'pune'}
dict14={}
for key,value in dict13.items():
    dict14[value]=key
print(dict14)

print("-"*50)
dict15={'x':23,'y':10,'z':7}
total=0
for val in dict15.values():
    total+=val
print(total)

print("-"*50)
dict16={'city':'pune','state':'maharastra','country':'india'}
count=0
for key in dict16.keys():
    if key==('country'):
        count+=1

if count>0:
    print("key exists")
else:
    print("key does not exists")

print("-"*50)
dict17={'food':'burger','type':"fast food"}
for val in dict17:
    print(val,dict17[val])

print("-"*50)
dict18={'course':'python','institute':'sqatools'}
dict19= {'name':'omkar'}
dict19.update(dict18)
print(dict19)

print("-"*50)
dict20={}
for i in range(1,6):
    dict20[i]=i**2
print(dict20)

print("-"*5)
dict21={'a':2,'b':4,'c':5}
result= 1
for val in dict21.values():
    result*=val
print(result)

print("-"*50)
dict22={'a':2,'b':4,'c':5}
dict22.popitem()
print(dict22)

print("-"*50)
dict23={'a':2,'b':4,'c':5}
dict24={}
for key,val in dict23.items():
    if key!='c':
        dict24[key]=val
print(dict24)

print("-"*50)

list25=['name','sport','rank','age']
list26= ['virat','cricket',1,32]
new_dict = tuple(zip(list25,list26))
print(new_dict)

print("-"*50)
dict25={'a':10,'b':44,'c':60,'d':25}
list27=[]
for val in dict25.values():
    list27.append(val)
list27.sort()

print("min",list27[0])
print("max",list27[-1])

