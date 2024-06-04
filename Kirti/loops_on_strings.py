# Python Loops program to construct the following pattern, using a nested for loops.


for i in range (1,6,):
    print(i*"*")
for i in range (6,-1,-1):
    print(i*"*")

print("_"*50)

#Count the number of even and odd numbers # not working

num = [1,2,3,4,5,6,7,8,9,10]

even = 0
odd =0

print("To chek if number is even or odd ")
for n in num:
    if n%2 == 0 :
        even += 1
        print("Number is even",even)
    else :
        odd += 1
        print("Number is odd, odd")

print("_"*50)

#Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.   # error in solution
print("_"*50)


for i in range (1,10):
    if i != 3 and i != 6:
        print(i,end=" ")
print("")

#Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.

print("_"*50)

a = 0
b = 1

count = 0

while count < 20:
    print(a,end=" ")
    n = a+b
    a = b
    b = n
    count += 1

    print("")

print("_"*50)

#Python for loop program to print the alphabet pattern ‘O’ using python.

for i in range (0,3):
    if i == 0 and i == 1 :
        print(" ")
    else :
        print("*")


'''Write a program to construct the following pattern, using a nested for loop in Python.
Output :
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5'''

