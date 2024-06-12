tup1 = (3, 6, 7, 3.6, 'Hello', [3, 6, 8])

print(tup1, type(tup1))
# (3, 6, 7, 3.6, 'Hello', [3, 6, 8]) <class 'tuple'>

print(dir(tuple))  # 'count', 'index'

print("_"*50)
# Loop with tuple values
for val in tup1:
    print(val)

print("_"*50)
# Loop with indexing
for i in range(len(tup1)):
    print(i, tup1[i])

print("_"*50)
################ Slicing in tuple #############
tup2 = (4, 6, 8, 1, 18, 25, 35)

print(tup2[2: 7])  # (8, 1, 18, 25, 35)

print(tup2[1:7:2]) #  (6, 1, 25)

print(tup2[-1: 2: -1]) # (35, 25, 18, 1)

print(tup2[-3:: 1]) # (18, 25, 35)

tup3 = (45,)
print(tup3, type(tup3))

################### Delete tuple variable #########

tup4 = (4, 6, 8, 1, 18, 2, 6, 2, 6, 2, 7)

# del tup4  : This will delete the tuple variable from memory
# print(tup4)
# del tup4[2:5]  # 'tuple' object does not support item deletion

# count method :
print(tup4.count(6))  # 3

# index method :
print("Index of 18 :", tup4.index(18))  # 4

############# Get max, min, and sum of values #######
print("_"*50)
tup5 = (22, 44, 55, 12, 25, 26)

print("max value :", max(tup5))  # 55
print("Min value :", min(tup5))  # 12
print("Sum value :", sum(tup5))  # 184




