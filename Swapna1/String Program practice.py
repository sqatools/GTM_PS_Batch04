'''Get a string made of first and the last 2 chars'''

str="welcome"
if len(str) < 2:
    print(True)
else:
    print(str[:1] + str[-4:]) #wcome

print("_" * 80)
str="hi"
if len(str) < 5:
    print(True)
else:
    print(str[:1] + str[-4:]) #True

print("_" * 80)


'''From list of strings, length of longest string'''
str1=["welcome", "to","learn","Python","Programming"]
temp=0
for word in str1:
    a=len(word)
    if a>temp:
      temp=a
      print(temp)
print("_" * 80)
"""String made of 4 copies of last 2 characters"""

str2="Helloworld"
print(str2[-2:]*4)

print("_" * 80)
""" Reverse a string if its length is multiple of 4"""

str3="python"
a=len(str3)
if a%4==0:
    print("Reverse string:", a)
else:
    print("not a multiple of 4")
print("_" * 80)

str4="helloooo"

if len(str4)%4==0:
    print("Reverse string:", str4[::-1])
else:
    print("not a multiple of 4")
print("_" * 80)

"""Count occurrences of a substring in a string.// output ???"""

str5 = "Python"
sub = "hon"
print(str5.count("hon"))

print("_" * 80)
'''The passed letter is a vowel or consonant'''
str6= "apple"
for char in str6:
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
        print(f"{char} is vowel")
    else:
        print(f"{char} is consonant")

        '''Longest and smallest word in the input string'''
print("_"*40)
str_a= "Welcome to world of python"
list= str_a.split(" ")
print("Longest word:", max(list,key=len))
print("Shortest word:",min(list,key=len))
print("_"*40)


''' Calculate the length of a string with loop logic '''  #// output?

str_b= "Python program"
count=0
for char in str_b:
    count=count+1
    print("Length of the string using for loop:", count)
    print("Length of the string using len() is:", len(str_b))

