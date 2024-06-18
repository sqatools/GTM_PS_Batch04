tup=(1,5,4,6,7,6,5.6,'Hello',[1,2,3])

print(tup,type(tup)) #(1, 5, 4, 6, 7, 6, 5.6, 'Hello', [1, 2, 3]) <class 'tuple'>

print('_'*50)
# Loop with tuple values
for i in tup:
    print(i,end=' ')
print( ) # 1 5 4 6 7 6 5.6 Hello [1, 2, 3]

print('_'*50)
# Loop with indexing
for val in range(len(tup)) :
    print(val,tup[val])

print(dir(tuple)) #'count', 'index'

print("_"*50)
################ Slicing in tuple #############
tup1=(2,3,5,6,8,9,10)

print(tup1[-1:-3:-1]) #(10, 9)

print(tup1[-1:-3]) #()

print(tup1[-1:3:-2]) #(10, 8)

print(tup1[1::-1]) #(3, 2)

print(tup1[4::-2]) #(8, 5, 2)

print(tup1[-1::1]) #(10,)

print(tup1[-1:4:-1]) #(10, 9)

print(tup1[-1::-2]) #(10, 8, 5, 2)

print(tup1[::-1]) #(10, 9, 8, 6, 5, 3, 2)
print(tup1[-4::1])#6, 8, 9, 10)

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
