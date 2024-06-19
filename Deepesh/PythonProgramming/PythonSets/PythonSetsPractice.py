set1 = {1, 4, 6, 7, 'a', 'b', 'c', 4, 6}

print(set1, type(set1))
# {1, 'b', 4, 'c', 6, 7, 'a'} <class 'set'>

"""
Properties:

-> Set is mutable data type.
-> Set contains only unique data, duplicate data is not allowed.
-> Only immutable data type can be member of set, e.g. int, float, string, tuple, boolean.
-> Set store data in random, it does not follow any sequencing.
"""

print("_"*50)
# apply loop on the set
set2 = {1, 4, 6, 7, 'a', 'b', 'c'}

for val in set2:
    print(val, end=" ")
# b 1 4 6 7 c a

###### Set Methods #############
print(dir(set))
"""
'add', 'clear', 'copy', 'difference', 'difference_update', 
'discard', 'intersection', 'intersection_update',
 'isdisjoint', 'issubset', 'issuperset', 'pop', 
 'remove', 'symmetric_difference',
  'symmetric_difference_update', 'union', 'update'
"""

print("_"*50)
######
# add method : this method helps to add data to the set.
set3 = {5, 7}
set3.add(56)
set3.add("Hello")
print("set3 :", set3)
#set3.add([4, 7, 8])  # can not add list as set member
#print("set3 :", set3)
# TypeError: unhashable type: 'list'

print("_"*50)
########
# union method : This method combine 2 sets and create new one.
set_a = {4, 6, 8, 9}
set_b = {'a', 'b', 'c', 'd'}

set_c = set_a.union(set_b)

print("set_C :", set_c)  #  {4, 6, 'a', 8, 9, 'c', 'd', 'b'}
print("set_a :", set_a)  #  {8, 9, 4, 6}
print("set_b :", set_b)  #  {'d', 'c', 'b', 'a'}

print("_"*50)
######
# update method : This method update the one set data to another set

set_x = {5, 7, 2, 8, 12}
set_y = {33, 55, 77, 88}
set_y.update(set_x)

print("set_x :", set_x)  # {2, 5, 7, 8, 12}
print("set_y :", set_y)  # {33, 2, 5, 7, 8, 12, 77, 55, 88}

###### Remove data from set #############

print("_"*50)
######
# remove method: this method remove specific data from set
set_p = {33, 2, 5, 7, 8, 12, 77, 55, 88}
set_p.remove(77)

print("set_p:", set_p) # {33, 2, 5, 7, 8, 12, 55, 88}

# try to remove value which is not available
# set_p.remove(99) # KeyError: 99

print("_"*50)
######
# discard method: This method remove data from set if it is available, if not then does not throw any error.

set_q = {33, 2, 5, 7, 8, 12, 55, 88}
set_q.discard(5)
print("set_q :", set_q)

# does not throw any error if target value in not available
set_q.discard(100)
print("set_q :", set_q)


print("_"*50)
######
# pop method : This method remove any random data from set and return it.
set_r = {33, 2, 7, 8, 12, 55, 88}
val = set_r.pop()
print("removed value:", val) # 33
print("set_r :", set_r)  # {2, 55, 7, 8, 88, 12}

print("_"*50)
######
# clear method : to clear all the data from set.
set_u = {33, 2, 7, 8, 12, 55, 88}

set_u.clear()
print("set_u :", set_u)  # set()

del set_u # remove it from memory
# print("set_u :", set_u)  # name 'set_u' is not defined

###########################################################
print("_"*50)
######
# difference method:  This method return difference between two sets.

set_A = {33, 2, 7, 8, 12, 55, 88}
set_B = {33, 2, 14, 18, 22, 15, 88}

diff_value_a_to_b = set_A.difference(set_B)
print("difference value :", diff_value_a_to_b)   # {8, 7, 12, 55}

diff_value_b_to_a = set_B.difference(set_A)
print("difference value :", diff_value_b_to_a)  # {18, 15, 22, 14}

print("set_A :", set_A)
print("set_B :", set_B)

print("_"*50)
#######
# difference_update method: this method update the target set with difference values

set_C = {33, 2, 7, 8, 12, 55, 88}
set_D = {33, 2, 14, 18, 22, 15, 88}

set_C.difference_update(set_D)  # {55, 7, 8, 12}
print("set_C :", set_C) # {55, 7, 8, 12}
print("set_D :", set_D)


print("_"*50)
##########
# intersection method: this method will return common values between two sets.

set_E = {33, 2, 7, 8, 12, 55, 88}
set_F = {33, 2, 14, 18, 22, 15, 88}

intersect_output = set_E.intersection(set_F)
print("intersect values :", intersect_output)  # {88, 33, 2}
print("set_E :", set_E)
print("set_F :", set_F)

# intersection update method: this update the target set with common values
set_E.intersection_update(set_F)

print("set_E :", set_E) # {88, 33, 2}










