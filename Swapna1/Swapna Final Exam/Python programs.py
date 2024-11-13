#1.Program to create a list of five consecutive numbers in list

res=[]
for i in range(4):
    val=[]
    for j in range(1,6):
       val.append(5*i+j)
    res.append(val)
print(res)


#2.Count integers

inp_list=["Hello",45,"sqa",23,5,"Tools",20]
count=0
for i in inp_list:
    if isinstance(i,int):
       count+=1
print("Integers count: ",count)


#3.Insert Element

inp_list=[3,5,7,8]
element_to_insert='a'
res=[]

for i in inp_list:
      res.append(element_to_insert)
      res.append(i)
print(res)


#5.Dictionary program- sum of all the items

dic_1={'x':23,'y':10,'z':7}
count=0
for i in dic_1.values():
    count+=i
print(count)



