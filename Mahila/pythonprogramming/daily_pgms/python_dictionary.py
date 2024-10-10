# 95)Python program to sum unique elements from dictionary list values.
# Input = { ‘a’ : [ 6, 7, 2, 8, 1], ‘b’ : [2, 3, 1, 6, 8, 10], ‘d’ : [1, 8, 2, 6, 9] }
# Output :
# 46

# D1 = {'a':[6,7,2,8,1],'b':[2,3,1,6,8,10],'d':[1,8,2,6,9]}
# l = [ ]
#
# for val in D1.values():
#     for num in val:
#         if num not in l:
#             l.append(num)
#
# print ("sum of the list : ", sum(l))
#----------------------------------------------------------------------------

# Python program to reverse each string value in the dictionary and add an underscore before and after the Keys.
# Input  = {“a” : “Python”, “b”: “Programming”, “c”: “Learning”}
# Output = {“_a_”: “nythonP”, “_b_” : “gnimmargorP”, “_c_”: “gearninL”}

# D1 = {'a':'Python','b':'Programming','c':'Learning'}
# D2 = {}
#
# for k,v in D1.items():
#     D2['_'+k+'_'] = v[::-1]
#
# print(D2)
#---------------------------------------------------------------------------