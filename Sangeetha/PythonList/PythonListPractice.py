#Python Lists

# a = list()
# print("empty list",a)

# a=list[10,20,"hello",'a']
# print("list",a)

#string to list convertion
str="sangeetha"
print(str)
strlist=list(str)
print(strlist)

#set to list convertion
set1=(10,20,28)
print(set1)
setlist=list(set1)
print(list(set1))

#dictionary to list convertion
mydict={"name":"sangeetha","age":"24","degree":"BSC"}
print(list(mydict))

#list methods
#  'append', 'clear', 'copy', 'count', 'extend',
#  'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

#insert method

#in this we can add the element in the specific index postion only

list_a = [3, 55, 22, 66]
list_a.insert(2,400)
print("list_a:", list_a)

#append method

#in this we can add the element in the end of the list

mylist=[100,200,300,400]
mylist.append("sangeetha")
mylist.append(800)
print("mylist:" ,mylist)

#extend function
#in this we insert one list data to another list

list_p = ['a', 'b', 'c', 'd']
list_q = [3, 6, 8, 1]
list_p.extend(list_q)
print("list_p:" , list_p)
print("list_q :", list_q)

list_p = ['a', 'b', 'c', 'd']
list_q = [3, 6, 8, 1]
list_q.extend(list_p)
print("list_p:" , list_p)
print("list_q :", list_q)

#pop method
# remove data from list using index position and return it, and the default index is -1

list1 =[1,45,60,70]
list1.pop(2)
print("list1:",list1)

list2=[14,26,69]
list2.pop()
print("list2:",list2)

#remove method
# this method remove any specific data from the list and does not return it.
a=[29,78,3.45]
a.remove(3.45)
print("a:",a)

#reverse method
#This method reverse the list data and modify the original list

b=[13,45,67,90]
b.reverse()
print("b:",b)

#sort method
#this is used to chnage the numbers in ascending to descending order
c=[12,4,7,8,21,]
c.sort()
print("c:",c)

# sort list in descending order
list4=[24,36,87,99,45,63]
list4.sort(reverse=True)
print("sorted list4 :", list4) #

###########
# sorted() function: This function return the ascending and descending list data,
# sorted function doesn't modify the original list

# clear method : This method remove all the data from the list.
d=[12,56,78]
d.clear()
print(d)



#index method
#this method tell us to know the index position of the particular value

list2=[1,2,3,4,5,6,7,8,13]
print("index position of 13 :", list2.index(13))

#count method
#This method count the occurance of any element.
list3 = [4, 6, 2, 7, 2, 5, 2, 6]
print(list3.count(2))

######## Deep copy and shallow copy ####
# shallow copy : consider we have two lists list_a and list_b,
# if we will assign list_a to list_b then update the list_b, data. the changes done in list_b
# will reflect in list_a as well

list_a = [5, 7, 2, 8, 1]
list_b = list_a
list_b.append(100)
list_b.insert(2,500)
print("list_a :", list_a, id(list_a))
print("list_b :", list_b, id(list_b))


list_p = [3, 5, 2, 11, 23]
list_q = list_p.copy()
list_q.append(300)
list_q.insert(3, 600)

print("list p :", list_p, id(list_p))
print("list q :", list_q, id(list_q))




