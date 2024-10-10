a=10
b=1680.009755
print(b,type(b))
print(a ,type(a))

c=1234782374900238778000002347877.98764
print('c:',type(c))
print(c)

a='sushmita shaasik'
print(a)

str='''python is programming langauage 
   it contains "list" ,"tuple"
    '''
print(str)

print('*'*50)

list=[1,2.4,'sum' , [1,2.5,'str1']]

print(list,type(list))
print(list[-1])        #[1, 2.5, 'str1']
print(list[-1][-1])  #str1
list[2]=78
print(list)
list.append(98)
print(list)

print('*'*50)
list3 = [4, 6, 7, [5, 7, 8], 'p', True]

p2 = list3[3]
print("p2 value :", p2)
p2.append(100)
list3.append(98)
print(list3)

##########tuple######

print("*"*50)
tuple=(3,45,6,7)

print(tuple,type(tuple))

print(tuple[1])

list1=[3,'sushmita']
tuple1=(45,[3,4,"Hello"],list1)
print(tuple1)

print(tuple1[2][1])

#############Dictionary################

print("*"*50)

dict={'name':'sushmit','29':'48', "add":"RAjajanagar"}
print(dict['add'],type(dict))
dict['age']=29
print(dict)

##############SET################################
set={1,'hello',(8,9,0)}
print(set,type(set))
