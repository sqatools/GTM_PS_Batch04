"""
list=[4,6,8,3,7,11,14]
output = [ ]

for i in list:
    if i%2==0:
        output.append(i**2)
    else:
        output.append(i**3)
print("output list :", output)


#Python program to calculate the square of each number from the given list.

list_1 = [1,2,3,4,5,7,8]

for val in list_1:
    print(val**2 , end= ", ")

print()


#combine two lists
list1 = [3, 6, 7, 81, 2]
list2 = [11, 15, 17, 13]

#print(list1+list2)   #concatenation method

list1.extend(list2)    #.extend method
print(list1)
print(list2)


#Problem to print the sum of all elements in a list.
list1 = [2,5,8,0,1]
count = 0

for val in list1:
    count = count + val
print(count)


#Problem to get product of all elements in a list

list1 = [3,6,9,2]
product = 1

for val in list1:
    product = product*val
print(product)



#Python program to find the minimum and maximum elements from the list.

list1 = [2,9,0,1,4,56,7]
list1.sort()
print("min value from the list : ", list1[0])
print("max value from the list : ", list1[-1])

#print("max value from the list : ", max(list1))
#print("max value from the list : ", min (list1))

# Python program to differentiate even and odd elements from the given list.

list = [23,11,78,90,34,55]

even = []
odd = []

for val in list:
    if val%2==0:
        even.append(val)
    else:
        odd.append(val)
print(odd)
print(even)


#Python program to remove all duplicate elements from the list.

list = [23,11,78,90,34,55,55,11,56,90,11,12,12,12,12,12,12]
list_new = [ ]

for val in list:
    if val not in list_new:
        list_new.append(val)
    else:
        continue
print(list_new)


#Python program to print a combination of 2 elements from the list whose sum is 10.

list_1=[1,2,3,8,5,4]
list= []
var=10

for val in list_1:
    for num in list:
        if sum(var,num):
            append.list(val+num)
        else:
            continue
print(list)


#Python program to split the list into two-part, the left side all odd values and the right side all even values.
#Input = [5, 7, 2, 8, 11, 12, 17, 19, 22]
#Output = [5, 7, 11, 17, 19, 2, 8, 12, 22]

list_1 = [5, 7, 2, 8, 11, 12, 17, 19, 22]

odd=[]
even=[]

for val in list_1:
    if val%2==0:
        even.append(val)
    else:
        odd.append(val)

odd.extend(even)
print(odd)

#Python program to get common elements from two lists.
#Input =
#list1 = [4, 5, 7, 9, 2, 1]
#list2 = [2, 5, 8, 3, 4, 7]
#Outputt : [4, 5, 7, 2]

list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]

list3=[]

for val in list1:
    if val in list2:
        list3.append(val)
    else:
        continue
print(list3)



#Python program to reverse a list with for loop.

list1 = [4, 5, 7, 9, 2, 1]

for val in range(len(list1)-1,-1,-1):
    print(list1[val],end=" ")



#Problem to print true if common elements between lists

list1 = [2,4,7,8,3]
list2 = [4,5,0]

for value in list1:
    if value in list2:
        print("True")

#Problem to print list after removing certain elements  , 1st, 3rd, and 6th
list1 = [3,4,8,7,0,1,6,9]
val=list1.pop(1)
print(val)

"""
#Python Program to get a list of words which has vowels in the given string.
#Input: “www Student ppp are qqqq learning Python vvv”
#Output : [‘Student’, ‘are’, ‘learning’, ‘Python’]

str_b = "www Student ppp are qqqq learning Python vvv"
str = str_b.split()
vowels=["a","e","i","o","u"]
list = [ ]

for word in str:
    for char in word:
        if char in vowels:
            list.append(word)
print(list)

