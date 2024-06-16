'''
Get a string made of first and the last 2 chars
'''

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

str4="sqatools"

if len(str4)%4==0:
    print("Reverse string:", str4[::-1])
else:
    print("not a multiple of 4")
print("_" * 80)



