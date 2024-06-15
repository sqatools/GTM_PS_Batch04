 #1). Write a  Python program to get a string made of the first and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string
"""
str1=input("enter the string")
if len(str1) < 2:
     print(True)
else:
     print(str1[0:3] + str1[-2:])
"""
#2). Python string program that takes a list of strings and returns the length of the longest string.
"""
str2=["hello","hi","python","learning","is"]
#str2=list(str1)
print(str2)
longeststr=0
a=""
for char in str2:
    if len(char)>longeststr:
        longeststr=len(char)
        a=char
    else:
        continue
print(longeststr,a)

str1="hello i am learning python"
b=str1.split(" ")
print(b,str1)
"""
#string methods
"""
str1="Hi i am Nikhila Joy"
str2=" I am confident "
print(str1.upper())
print(str1.lower())
print(str1.title())
print(str1.istitle())
print("count of a in str1 is :",str1.count("a"))
print("index position of N is :",str1.index("N"))
print("index position of Nikhila is :",str1.index("Nikhila"))
print("index position of N is :",str1.find("N"))
print("index position of hii is :",str1.find("Hii"))
print(str1.split("i"))
print("-".join(str1))
print(str2)
print(str2.strip())
"""
#3). Python string program to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
"""
str1=input("enter the string")
if (len(str1)>=2):
    print(str1[(len(str1))-2:(len(str1))+1]*4)
"""

#4).  Python string program to reverse a string if it’s length is a multiple of 4.
"""
str1=input("enter the string")
a=len(str1)
print(a)
if a%4==0:
    print(str1[::-1])
else:
    print("not a multiple of 4")
 
#6).  Python string program to test whether a passed letter is a vowel or consonant.
str1=input("enter the letter")
v=["a","e","i","o","u"]

if str1 in v:
    print("entered letter is a vowel")
else:
    print("entered letter is a consonant")
"""
#7). Find the longest and smallest word in the input string.
"""
str1=input("enter the string")
a=str1.split(" ")
print(len(a))
longest=0
l=""
s=""
small=len(a)

for char in a:
    if len(char)>longest:
        l = char
        longest=len(char)
        #print(char)
print(longest,l)
for char in a:
    if len(char)<small:
        s = char
        small=len(char)
        #print(char)
print(small,s)
"""
#8). Print most simultaneously repeated characters in the input string.
str1=input("enter the string")  #whattt is ur nammmeeeeeee
#a=str1.split(" ")
#print(str1(1)
count=1
for i in range(len(str1)-1):
     if str1[i] == str1[i+1]:
         count+=1
     else:
         continue
print(count)