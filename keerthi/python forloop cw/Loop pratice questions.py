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

#Python Loops program to count the number of even and odd numbers from a series of numbers using



