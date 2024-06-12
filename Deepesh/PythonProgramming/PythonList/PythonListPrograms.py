# write a python program to remove duplicate data
list1 = [3, 6, 7, 8, 1, 3, 4, 6]
# output = [3, 6, 7, 8, 1, 4]

# method1 : solve program with logic
output = []

for val in list1: # 3, 6, 7, 8, 1, 3, 4
    if val not in output:
        output.append(val) # [3, 6, 7, 8, 1, 4]
    else:
        continue

print("output :", output)

print("_"*50)
# convert list into and set and remove duplicate

result = set(list1)
print(result)
print("set conversion result :", list(result))


######
print("_"*50)
# write a python program to move all the positive value left side and negative value in right
# side of the list

list2 = [2, -1, 5, -4, -7, 12.23, 51, 25, -8]
# output = [25, 51, 12, 5, 2, -1, -4, -7, -8]

output = []
for val in list2:
    if val > 0:
        output.insert(0, val)
    else:
        output.append(val)

print("output :", output)

print("_"*50)
#####################################################

# write a python program to print square of even and cube of odd value in the list

list_a = [4, 6, 8, 3, 7, 11, 14]
#  output = [4**2, 6**2, 8**2, 3**3 ....]


print("_"*50)
########################################################
# write a python program to sort the list values without using sort() method.
#         i         j
list_b = [3, 30, 6, 20, 7, 80, 1, 4]
#            i     j
#        [1, 3, 30, 20, 7, 80, 6, 4]

for i in range(len(list_b)):
    for j in range(i+1, len(list_b)):
        if list_b[i] < list_b[j]:
            temp = list_b[i]
            list_b[i] = list_b[j]
            list_b[j] = temp
            #print(list_b)

print(list_b)
