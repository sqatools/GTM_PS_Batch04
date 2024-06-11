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
"""

str2="I am learning python"
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
"""


