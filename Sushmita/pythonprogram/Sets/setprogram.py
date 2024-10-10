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
    print(val,end=" ")

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
set1={34,'a'}
set1.add(54)
print(set1) #{34, 'a', 54}

#set3.add([4, 7, 8])  # can not add list as set member
#print("set3 :", set3)
# TypeError: unhashable type: 'list'

print("_"*50)
########
# union method : This method combine 2 sets and create new one.
set2={3,4,'a'}
set3={'Hello',45,89,20}
set4=set2.union(set3)
print(set4) #{3, 4, 20, 'Hello', 89, 45, 'a'}

print("_"*50)
######
# update method : This method update the one set data to another set
set2={3,4,'a'}
set3={'Hello',45,89,20}
set3.update(set2)
print('set2:',set2) #{3, 4, 'a'}
print('set3:',set3) #{3, 20, 4, 'a', 'Hello', 89, 45}

###### Remove data from set #############

print("_"*50)
######
# remove method: this method remove specific data from set
set5={'a','b',34,23,45,77}
set5.remove(34)
print(set5) #{'b', 45, 77, 'a', 23}

# try to remove value which is not available
#set_p.remove(99) # KeyError: 99

print("_"*50)
######
# discard method: This method remove data from set if it is available, if not then does not throw any error.
set5={'a','b',34,23,45,77}
set5.discard(23)
print(set5) #{'a', 34, 45, 77, 'b'}

# does not throw any error if target value in not available
set5.discard(100)
print("set5 :", set5)
set5.discard(99)

print("_"*50)
######
# pop method : This method remove any random data from set and return it.
set_r = {33, 2, 7, 8, 12, 55, 88}
val=set_r.pop()
print('val:',val) #33
print(set_r) #{2, 7, 8, 12, 55, 88}

print("_"*50)
######
# clear method : to clear all the data from set.
set_u = {33, 2, 7, 8, 12, 55, 88}
set_u.clear()
print(set_u) #set()

del set_u # remove it from memory
#print("set_u :", set_u)  # name 'set_u' is not defined

###########################################################
print("_"*50)
######
# difference method:  This method return difference between two sets.

set_A = {33, 2, 7, 8, 12, 55, 88}
set_B = {33, 2, 14, 18, 22, 15, 88}

diff_value=set_A.difference(set_B)
print(diff_value) #{8, 12, 55, 7}

diff_value1=set_B.difference(set_A)
print(diff_value1) #{18, 22, 14, 15}

print("_"*50)
#######
# difference_update method: this method update the target set with difference values
set_C={24,34,2,10,90,43,19}
set_D={19,43,45,23,20,67,89}

diff=set_C.difference_update(set_D)
print(diff)
print('set_C:,',set_C) #{34, 2, 10, 24, 90}
print('set_D:,',set_D) #{67, 43, 45, 19, 20, 23, 89}

print("_"*50)
##########
# intersection method: this method will return common values between two sets.

set_E = {33, 2, 7, 8, 12, 55, 88}
set_F = {33, 2, 14, 18, 22, 15, 88}
intersection=set_E.intersection(set_F)
print(intersection) #{88, 33, 2}

print("set_E :", set_E)
print("set_F :", set_F)

# intersection update method: this update the target set with common values
set_E.intersection_update(set_F)

print("set_E :", set_E) # {88, 33, 2}

print("_"*50)
#########
# symmetric_difference : this method return the difference values from both sets.

set_g = {33, 2, 7, 8, 12, 55, 88}
set_h = {33, 2, 14, 18, 22, 15, 88}
result=set_g.symmetric_difference(set_h)
print(result) #{7, 8, 12, 14, 15, 18, 22, 55}

######################



# symmetric_difference_update: This method update the set with difference value of the both the sets.

set_g.symmetric_difference_update(set_h)
print("set_g :", set_g)
print("set_h :", set_h)

####### subset and super set ############

set_j = {33, 2, 7, 8, 12, 55, 88}
set_k = {2, 7, 8}
set_l = {7, 33, 66}

print(" is super set:", set_j.issuperset(set_k))  # True
print(" is sub set:", set_k.issubset(set_j)) # True

print("is superset :", set_j.issuperset(set_l)) # False
print("is subset :", set_l.issubset(set_j)) # False

print("_"*50)

######## Copy ##########

# shallow copy
set_r = {5, 7, 2, 8}
setp=set_r
setp.add(100)
set_r.add(34)
print(set_r) #{2, 34, 100, 5, 7, 8}
print(setp) #{2, 34, 100, 5, 7, 8}

print("_"*50)
# Deep copy
sets={2,3,4,5}
seth=sets.copy()
seth.add(100)
print(seth) #{2, 3, 100, 4, 5}
print(sets) #{2, 3, 4, 5}

