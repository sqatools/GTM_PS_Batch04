"""
1). Write a  Python program to get a string made of the first and the last 2 chars
from a given string.
If the string length is less than 2, return instead of the empty string

Input:Sunita
Output:Suta

Input:S
Output:empty string
"""

string1="Sunita"
first_str=string1[0:2]
last_str=string1[-2:]
if len(string1)<2:
    print("Empty String")
else:
    print(first_str+last_str);

string1="S"
first_str=string1[0:2]
last_str=string1[-2:]
if len(string1)<2:
    print("Empty String")
else:
    print(first_str+last_str);

"""
2). Python string program that takes a list of strings and returns the length of the longest string.

input:I am learning python
output: learning
"""
str2=["I","am","learning","python"]
str=0
for i in str2:
    if len(i)>str:
        str=len(i)
    print(str)

"""
1>0 =1
2>1=2
8>2=8
6>8=8

3). Python string program to get a string made of 4 copies of the last two characters 
of a specified string (length must be at least 2).

"""
str3="S"
if len(str3)<2:
    print("length must be at least 2")
else:
    print(str3[-2:]*4)

str3="Sunita"
if len(str3)<2:
    print("length must be at least 2")
else:
    print(str3[-2:]*4)

"""
4).  Python string program to reverse a string if it’s length is a multiple of 4.
"""

str4="Done"
if len(str4)%4==0:
    print(str4[::-1])
else:
    print("Length is not a multiple of 4")

"""
5). Python string program to count occurrences of a substring in a string.
"""
str5="Zoological"
print(str5.count("o"))

"""
6).  Python string program to test whether a passed letter is a vowel or consonant.
"""

str6="zoological"
for char in str6:
    if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
        print(f"{char} is a vowel")
    else:
        print(f"{char} is a consonant")

"""
7). Find the longest and smallest word in the input string.
"""
str7="I am learning python"
str8=str7.split(" ")
print("Longest word :",max(str8))
print("Longest word :",min(str8))


str7="I am learning python"
str8=str7.split(" ")
print("Longest word :",max(str8,key=len))
print("Longest word :",min(str8,key=len))

"""
#output is same for both code 
Longest word : python
Longest word : I
Longest word : learning
Longest word : I

8). Print most simultaneously repeated characters in the input string.

"""

str9="Hellllooo Frrreeennndzzz"
max_str_total=0
max_str=''
count=1

for i in range(len(str9)-1):
    if str9[i]==str9[i+1]:
        count +=1
        if count>max_str_total:
            max_str_total=count
            max_str=str9[i]
    else:
        count = 1
print("repeated characters", max_str)
print("repeated characters", max_str_total)

#







