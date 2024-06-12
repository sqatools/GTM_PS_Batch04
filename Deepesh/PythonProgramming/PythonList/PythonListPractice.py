list1 = [2, 3.4, 'Hello', [3, 5, 6], (1, 3, 5), {'a': 123, 'b' : 345}, {3, 7, 1, 4}, True]

print(list1, type(list1))  # <class 'list'>

print(list1[4]) # (1, 3, 5)

print(list1[-2])  # {1, 3, 4, 7}

print(list1[5]['a'])  # 123

print(list1[3][1])  # 5

print("_"*50)
# apply loop on list values

for val in list1:
    print(val)


print("_"*50)
# program to print all the even number from given list
lista = [3, 6, 2, 7, 1, 4, 8]
for val in lista:
    if val%2 == 0:
        print(val)

print("_"*50)
for i in range(len(lista)):
    #print(i,lista[i])
    if lista[i]%2 ==0:
        print(lista[i], end=" ")



############## List Slicing ################

lista = [4, 7, 2, 8, 12, 56, 23]

print(lista[3:6])  # [8, 12, 56]

print(lista[1:6])  # [7, 2, 8, 12, 56]

print(lista[1:-1])  # [7, 2, 8, 12, 56]

print(lista[2:-2: 1])  # [2, 8, 12]

print(lista[::-2]) # [23, 12, 2, 4]

print(lista[::-1]) # [23, 56, 12, 8, 2, 7, 4]

############################ list methods #########################
print(dir(list))
#  'append', 'clear', 'copy', 'count', 'extend',
#  'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

print("_"*50)
##### add data to the list #####
# append method: This method add one data at time in list at the end.
list_c= [4, 6, 8, 1]
list_c.append(100)
list_c.append('Python')
print("list_c :", list_c) # [4, 6, 8, 1, 100, 'Python']


#-----------
# insert() method : This method add data to the specific index position.
list_d = [3, 55, 22, 66]
list_d.insert(2, 500)
print("list_d :", list_d)  # [3, 55, 500, 22, 66]


print("_"*50)
##########
# extend method : This method helps to insert one list data to another list
list_p = ['a', 'b', 'c', 'd']
list_q = [3, 6, 8, 1]

list_q.extend(list_p)
print("list p :", list_p)
print("list q :", list_q)

print("_"*50)
###############
# list concatenation:
list_a = ['p', 'q', 'r']
list_b = ['x', 'y', 'z']

list_c = list_a + list_b
list_d = list_a
print("list_c :", list_c)
print("list_a :", list_a)
print("list_b :", list_b)
list_a.append(700)

print("list_d :", list_d)
print("list_c :", list_c)

###################################
# list repeatation
list_h = [4, 6, 7]
list_k = list_h*5
print("list_k :", list_k)  # [4, 6, 7, 4, 6, 7, 4, 6, 7, 4, 6, 7, 4, 6, 7]

################## Remove data from list ####################
print("_"*50)
# remove method : this method remove any specific data from the list and does not return it.
list_11 = [4, 6, 8, 22, 55, 12]
result = list_11.remove(55)
print("Result :", result)
print("list_11 :", list_11)

print("_"*50)
# pop method : This method remove data from list using index position and return it, and the default
#                index is -1

list_3 = ['a', 'b', 'c', 'd', 5, 8]

# remove with default index -1
val1 = list_3.pop()
print("val:", val1) # val: 8
print("list_3", list_3) #  ['a', 'b', 'c', 'd', 5]

# remove with specific index
val2 = list_3.pop(1)
print("pop value :", val2)
print("list_3 :", list_3)  # ['a', 'c', 'd', 5]

###########
print("_"*50)
# clear method : This method remove all the data from the list.
list_4 = [3, 6, 7, 1, 3]
list_4.clear()
print("list_4 :", list_4)  # []

#########
# del : this will remove complete list variable from the memory

list_5 = [4, 7, 33, 22]
del list_5
# print("list_5 :", list_5)  # NameError: name 'list_5' is not defined. Did you mean: 'list_c'?

# remove specific number of elements using slicing in del
list_6 = [5, 7, 2, 5, 12, 34]

del list_6[1:3]
print("list_6:", list_6)  #  [5, 5, 12, 34]

list_7 = [25, 7, 12, 15, 12, 34]
del list_7[1:-1]
print("list_7:", list_7)  # [25, 34]



list_a=[4,6,8,3,7,11,14]
output=[]

for i in range in (list_a):
    if i%2==0:
        print(i, i**2)
    else:
        print(i, i**3)




















