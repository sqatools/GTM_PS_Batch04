# #Remove duplicate data from list
#
# #Method 1 program with logic
# list1 = [3,6,7,8,1,3,4,6]
# # apply loop get each value
#
# #out put shoul be  list1 = [3,6,7,8,1,4]
# #make a blank output list add the duplicate values in it
#
# output = []
#
# for val in list1: #3,6,7,8,1,3,4,6
#     if val not in output:
#         output.append(val) #[3,6,7,8,1,skip,4,skip,]
#     else : # 3
#         continue
# print(output)
#
# #conver list into set  and remove duplicate
#
# result = set(list1)
# print(result)
# print(" set to List conversion :",list(result)) # sequance may change
#
# # do even odd programp using list
#
# print("_"*50)
# # WAPP to move all positive values left side an negative values in right side of the list
#
# list2 = [2,-1,5,-4,-7,12,51,25,-8]
# #Output = [25,51,12,5,2,-1,-4,-7,-8]
# output = []
#
# for value in list2:
#     if value > 0:
#         output.insert(0,value)
#     else:
#         output.append(value)
#
# print(output)
#
# print("_"*50)
#
# # WAPP to  print sequre of even value and cube of odd values in list
#
# print("_"*50)
#
# even = []
# odd = []
#
# list4 = [1,2,3,4,5,6,7,8,9,10]
# for values in list4:
#     if values%2 == 0:
#         even.append(values)
#         print("Even", values**2)
#     else :
#         odd.append(values)
#         print("odd", values**3)
#
#
# print("_"*50)
#
# list3 = [1,2,3,4,5,6,7,8,9,10]
# output = []
#
# for value in list3:
#     if value % 2 == 0:
#         output.append(value**2)
#     else:
#         output.append(value**3)
#
# print(output)

#using range

list4 = [1,2,3,4,5,6,7,8,9,10]


for i in list4:
    if i % 2 == 0:
        print(i**2)
    else :
        print(i**3)





