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
