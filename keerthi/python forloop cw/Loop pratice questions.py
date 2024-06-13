#1). Write a  Python loops program to find those numbers which are divisible by 7 and multiple of 5,
# between 1500 and 2700 (both included).

for i in range(1500,2701):
    if i%7==0 and i%5==0:
        print(i,end=" ")

print()

#2).Python Loops program to construct the following pattern, using a nested for loops.

# for i in range(6):
#     for j in range(i*"*"):
#         print(j,end=" ")
# print()
# for i in range(4,0,-1):
#     for j in range(i*"*"):
#         print(j,end=" ")
#
# print()

#Python Loops program that will add the word from the user to the empty string using  python.

word=input(str("Enter the word:"))
str=" "
for i in range(len(word)):
    str+=word[i]
print(str)

#Python Loops program to count the number of even and odd numbers
# from a series of numbers using
n=(1, 2, 3, 4, 5, 6, 7, 8, 9)
even=0
odd=0

for val in n:
    if val%2==0:
     even+=1
else:
     odd+=1

print("Number of even numbers:", even)
print("Number of odd numbers:", odd)
print()

# Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
for i in range(0,6):
    if i!=3 or i!=6:
        print(i, end=" ")

print()

#Write a program to get the Fibonacci series between 0 to 20 using python.
num1=0
num2=1
count=0

while count<20:
    print(num1,end=" ")
    n2=num1+num2
    num1=num2
    num2=n2
    count+=1

    print()

# Write a program that iterates the integers from 1 to 30 using  python. For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
#For numbers that are multiples of both three and five print “FizzBuzz”.

for i in range(1,31):
    if i%3==0 and i%5==0:
        print("FIZZBUZZ")
    elif i%3==0:
            print("Fizz")
    elif i%5==0:
                print("BUZZ")

    #changing uppercase to lowercase
char=input("enter the word:",)
result=' '
for char in input():
  if char.isupper():
      print(char.lower(),end="")
  else:
    print(char,end="")