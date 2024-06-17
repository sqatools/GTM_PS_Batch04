list1 = [3, 6, 8, 12]

list1[1] = 600
print(list1)

#####
# Index method:
list2 = [3, 6, 8, 13, 44, 22, 12]
print("index position of 13 :", list2.index(13))  #  3


#####
# count method : This method count the occurance of any element.
list3 = [4, 6, 2, 7, 2, 5, 2, 6]
print(list3.count(2))  # 3

print("_"*50)
#####
#sort() method : This  method sort the list data in ascending and descending order and modify the
# original list
list4 = [4, 8, 2, 7, 1, 6, 9]
# sort list in ascending order
""""
list4.sort()
print("sorted list4 :", list4) # [1, 2, 4, 6, 7, 8, 9]
"""

# sort list in descending order
list4.sort(reverse=True)
print("sorted list4 :", list4) # [9, 8, 7, 6, 4, 2, 1]

###########
# sorted() function: This function return the ascending and descending list data,
# sorted function doesn't modify the original list

list5 = [4, 7, 22, 88, 1, 44, 12]

# ascending order list
result1 = sorted(list5)
print("ascending order :", result1)  # [1, 4, 7, 12, 22, 44, 88]

# descending order list
result2 = sorted(list5, reverse=True)
print("descending order :", result2)  # [88, 44, 22, 12, 7, 4, 1]

print("list 5:", list5)  # [4, 7, 22, 88, 1, 44, 12]


print("_"*50)
####################
# reverse() method: This method reverse the list data and modify the original list
list6 = [4, 6, 1, 7, 1, 5, 22]
list6.reverse()
print("revered list data :", list6)


# reversed function : Reversed function return the reverse list data and does not
# modify the original list
list7 = [4, 7, 1, 88, 22, 55, 11, 33]
output = reversed(list7)
# for val in output:
#     print(val , end=" ")
print("output :", tuple(output)) # [33, 11, 55, 22, 88, 1, 7, 4]
print("list7 :", list7)  # [4, 7, 1, 88, 22, 55, 11, 33]

print("_"*50)
print(dir(list))

#'append',
# 'clear',
# 'copy',
# 'count',
# 'extend',
# 'index',
# 'insert',
# 'pop',
# 'remove',
# 'reverse',
# 'sort']

print("_"*50)
######## Deep copy and shallow copy ####
# shallow copy : consider we have two lists list_a and list_b, if we will assign list_a to list_b
# then update the list_b, data. the changes done in list_b will reflect in list_a as well

list_a = [5, 7, 2, 8, 1]
list_b = list_a
list_b.append(100)
list_b.insert(2, 500)

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



