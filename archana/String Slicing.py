a= "Python Programming"
output1= a[1:8]
print(output1)

o2= a[1:-1]
print(o2)

o3= a[-1:1]
print(o3)

o4=a[-6:-5]
print(o4)

o5= a[-6:-10]
print(o5)

o6= a[1:-10:1]
print(o6)

o7= a[1:-10:-1]
print(o7)

#1). Write a  Python program to get a string made of the first and the last 2 chars from a given string.
#If the string length is less than 2, return instead of the empty string

str="python"
if len(str)<2:
    print("true")
else:
    print(str[0:2]+str[-2:])

#2). Python string program that takes
#a list of strings and returns the length of the longest string.

str=['i','archana','sachin','anirudh','shravya']
count=0
for i in str:                       #doubt- print longest str
    a= len(i)
    if a>count:
        count= a
print(count)