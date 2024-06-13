list1 = [3, 6, 8, 12]

list1[1] = 600
print(list1)

#####
# Index method:
list2=[3,6,8,9,19]
print('Index of list:',list2.index(9)) #3

####
# count method : This method count the occurance of any element.
list3=[1,2,5,1,6,7,1,8,1]
print(list3.count(1)) #4

print("_"*50)
#####
#sort() method : This  method sort the list data in ascending and descending order and modify the
# original list

list4=[6,7,8,4,1,3,9]
#sort in ascending order
"""""
list4.sort()
print('ascendind order:',list4) #[1, 3, 4, 6, 7, 8, 9]

"""

#sort in descending order
list4.sort(reverse=True)
print('descnding order:',list4) #[9, 8, 7, 6, 4, 3, 1]

###########
# sorted() function: This function return the ascending and descending list data,
# sorted function doesn't modify the original list

list5=[3,4,7,2,1,8,9]

result1=sorted(list5)
print('ascending order:',result1) #[1, 2, 3, 4, 7, 8, 9]

result2=sorted(list5,reverse=True)
print('result2',result2)#[9, 8, 7, 4, 3, 2, 1]

print(list5) #[3,4,7,2,1,8,9]

print("_"*50)
####################
# reverse() method: This method reverse the list data and modify the original list
list6=[3,4,5,6,7,8]
list6.reverse()
print('reverse list:',list6) #[8, 7, 6, 5, 4, 3]

# reversed function : Reversed function return the reverse list data and does not
# modify the original list
list7 = [4, 7, 1, 88, 22, 55, 11, 33]
output=reversed(list7)
print('reversed list:',tuple(output)) #(33, 11, 55, 22, 88, 1, 7, 4)
#for val in output:
#    print(val,end=' ')
print('\nlist7:', list7) #[4, 7, 1, 88, 22, 55, 11, 33]


print("_"*50)
######## Deep copy and shallow copy ####
# shallow copy : consider we have two lists list_a and list_b, if we will assign list_a to list_b
# then update the list_b, data. the changes done in list_b will reflect in list_a as well
list_a=[3,4,67]
list_b=list_a
list_b.append(100)
list_b.insert(2,5)
print(list_b)
print("list_a :", list_a, id(list_a))
print("list_b :", list_b, id(list_b))


print("_"*50)
#### Deep copy ####

list_p = [3, 5, 2, 11, 23]
list_q = list_p.copy()
list_q.append(300)
list_q.insert(3, 600)

print("list p :", list_p, id(list_p))
print("list q :", list_q, id(list_q))

print("_"*50)
################################
# find the max and min and sum of values
list_m = [3, 6, 8, 33, 22, 12,]

print("Max number :", max(list_m))
print("Minimum value :", min(list_m))
print("sum of list value :", sum(list_m))


######################################
# list comphrehension

list_c = [3, 22, 45, 33, 2, 6, 8, 11, 23, 43]
result = [val for val in list_c if val%2==0]
print("All even number:", result)  # [22, 2, 6, 8]


result2 = [(val, "even") if val%2 ==0 else (val, "odd") for val in list_c]
print(result2)
# [(3, 'odd'), (22, 'even'), (45, 'odd'), (33, 'odd'), (2, 'even'), (6, 'even'), (8, 'even'), (11, 'odd'), (23, 'odd'), (43, 'odd')]

print('_'*50)
tuple2=(4,6,8,1,18,25,35)
print(tuple2[-1:5:1])
