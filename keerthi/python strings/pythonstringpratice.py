#write a program to print 1st and last two chars of the str.
str="program"
if len(str)<2:
    print(True)
else:
    print(str[:2] + str[-2:]) #pram

#Python string program that takes a list of strings and returns the length of the longest string.

string=["iam","living","in","Mumbai"] #doubt
temp=0
for list in string:
    a = len(list)
    if a > temp:
      temp = a
    print(temp)

#3). Python string program to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).

str2="python"
print(str2[-2:]*4) #amamamam

# Python string program to reverse a string if it’s length is a multiple of 4.

str4="programming" #output not printing
if len(str4)%4 == 0:
    print(str4[-1: -11: -1])

# Python string program to count occurrences of a substring in a string.