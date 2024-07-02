#Dictionary program to group the same items into a dictionary value.
#list = [1,3,4,4,2,5,3,1,5,5,2,]
#Output = {1 : [1, 1], 2 :[2, 2], 3 : [3, 3], 4 : [4, 4], 5 : [5, 5, 5]}
#from collections import defaultdict
list1=[1,3,4,4,2,5,3,1,5,5,2]
dict1={}
#dict1 = defaultdict(list)
print(dict1)
for val in list1:
    if val in dict1:
        dict1[val].append(val)
    else:
        dict1[val] = [val]
print(dict1)
