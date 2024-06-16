"""
Python program to calculate the square of each number from the given list.
"""
# Using For loop

l1=[3,4,5,6,7,8]
for var in l1:
    sqr=var**2
    print("Square of given number:", sqr)
#Using While loop ???
print("_"*50)
"""Problem to add elements from list1 to list2."""
list1=[1,2,3]
list2=[4,5,6]
list3=list1+list2
print(list3)

#using extend method

lis1=[1,2,3]
lis2=[4,5,6]
lis1.extend(lis2)
print(lis1)
print("_"*50)
"""Problem to print the sum of all elements in a list."""
#using For loop
ls=[1,2,3,4,5]
count=0
for a in ls:
    count+=a
    print(count)
print("_"*50)

#using Sum()

ls1=[5,5,10]
print(sum(ls1))
print("_"*50)
"""Problem to get product of all elements in a list"""
ls2=[10,2,3]
val=1
for var in ls2:
    val*=var
    print(val)
print("_" * 50)

"""Problem to find minimum and maximum elements from a list"""
#USing Sort()
ls3=[1,2,3,4]
ls3.sort()
print("Smallest number:",ls3[0])
print("Largest number:",ls3[-1])
print("_" * 50)

# Using inbuilt function min() and max()
ls4=[23,56,90]
print("Largest number:", max(ls4))
print("Smallest number:",min(ls4))
print("_" * 50)

"""Problem to differentiate even and odd elements from a list."""
ls5=[2,4,3,7,9]
odd=[]
even=[]
for a in ls5:
    if a%2==0:
        even.append(a)
    else:
        odd.append(a)

print("Even number:", even)
print("Odd numbers:", odd)

print("_"*50)
"""Problem to remove all the duplicate elements from a list."""
ls6 =[2, 8, 3, 8, 2, 9, 0, 5, 3]
emp = []
for b  in ls6:
  if b not in emp:
     emp.append(b)

print(emp)
print("_"*50)

""" Problem to print squares of even numbers from a list."""
a=[2,4,5]
for b in a:
    if b%2==0:
        print(b,":",b**2)
    else:
        print(b,":",b**3)
print("_"*50)








