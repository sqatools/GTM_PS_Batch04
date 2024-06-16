# output=[]
# list_a=[4,6,8,3,7,11,14]
# for val in list_a:
#     if val%2==0:
#         output.append(val**2)
#     else:
#         output.append(val**3)
# print("output :", output)
#
# #  output = [4**2, 6**2, 8**2, 3**3 ....]
#
# namelist=['harsh', 'pratik','bob']
# print(namelist[1][-1])
#
# list_a = [4, 6, 8, 2]
# str1 = str(list_a)
# print(str1, type(str1), str1[0], str1[1], str1[-1])
#
# list_b = [1, 6, 8, 2]
# tup2 = tuple(list_b)
# print(tup2, type(tup2), tup2[2])
#
# l1 = ['a', 'b', 'c', 'd']
# l2 = [2, 5, 8, 1]
#
# output = dict(zip(l1,  l2))
# print(output)
#
# print("_" * 50)
#
# list_d = [5, 8, 'a', 'b', 22, 55, 22, 8, 5,33.1, 7]
# set_d = set(list_d)
# print(set_d)
#
# print("_" * 50)
# list_e = []
# b1 = bool(list_e)
# print(b1, type(b1))  # False <class 'bool'>
#
# list_f = [4, 7, 8]
# b2 = bool(list_f)
# print(b2, type(b2))  # True <class 'bool'>
#
# list1 =[1,45,60,70]
# list1.pop(2)
# print("list1:",list1)
#
# list2=[14,26,69]
# list2.pop()
# print("list2:",list2)
#
# a=["sangeetha",20,48,3.14]
# a.remove("sangeetha")
# print(a)
#
# list_x=[1,2,3]
# list_y=[4,5,6,7]
# result=list(zip(list_x ,list_y))
# print(result)
#
# c=[12,4,7,8,21,]
# c.sort()
# print("c:",c)
#
# list4=[24,36,87,99,45,63]
# list4.sort(reverse=True)
# print("sorted list4 :", list4)

#### Programm Practice #######
"""
#1 calculate the square of each number from the given list.

list1=[1,2,3]
for val in list1:
    print(val , val**2)

#2 combine 2 list

a=[1,2,3]
b=[3,4,5]
a.extend(b)
print(a)

#3 calculate the sum of all elements from a list

list2=[1,2,3]
print(sum(list2))

#4 product of all elements from a given list

list3=[1,2,3]
for val in list3:
    print(val,val*2)

#5 minimum and maximum elements from the list
list4=[1,2,3,4]
print(min(list4))
print(max(list4))

#6 square and cube of number and odd and even
# output=[]
# list5=[1,2,3]
# for val in list5:
#     if val%2==0:
#         output.append(val**2)
#     else:
#         output.append(val**3)
# print(output)

list5=[1,2,3,4]
even=[]
odd=[]
for val in list5:
    if val%2==0:
        even.append(val)
    else:
        odd.append(val)
print(odd)
print(even)

#7 remove all duplicate elements from the list.

list1=[5,7,8,2,5,0,7,2]
list2=[]
for value in list1:
    if value not in list2:
        list2.append(value)
print(list2)

#10 split the list into two-part, the left side
# all odd values and the right side all even values.
a=[5, 7, 2, 8, 11, 12, 17, 19, 22]

odd=[]
even=[]
for value in a:
    if value%2==0:
        even.append(value)
    else:
        odd.append(value)
odd.extend(even)
print(odd)

"""

# #get common elements from two lists.
# list1 = [4, 5, 7, 9, 2, 1]
# list2 = [2, 5, 8, 3, 4, 7]
# list3=[]
# for val in list1:
#     if val in list2:
#         list3.append(val)
# print(list3)

#program to reverse a list with for loop

# list3=[1,2,3,4,5]
# list3.reverse()
# print(list3)

# list3=[1,2,3,4]
#
# for i in range(len(list3)-1,-1,-1):
#     print(list3[i], end=" ")
"""
#program to reverse a list with a while loop

list4=[1,2,3,4,5]
count=len(a)-1
while count >=0 :
    print((value[count], end="")
    count-=1
"""
####program to reverse a list using index slicing

# list1=[1,2,3,4,5]
# list2 = list1[::-1]
# print(list2)
#
# #reverse a list with reversed and reverse methods.
#
# list3=[1,2,3,4]
# list3.reverse()
# print(list3)
#
# list4=[1,2,3,4,5,6,7]
# output=reversed(list4)
# print(list(reversed(list4)))
#
# #16  copy or clone one list to another list.

# list1=[1,2,3,4]
# list2=[5,6,7,8]
# list1.append(list2)
# print(list1)

#17). Python program to return True if two lists have any common member.

list3=[1,2,3,4]
list4=[4,5,6]
for val in list3:
    if val in list4:
        print("true")

#22
string = "www Student ppp are qqqq learning Python vvv"
string2=string.split()

list1=[]
for words in string2:
    for char in words:
        if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
            list1.append(words)
            break
print(list1)




