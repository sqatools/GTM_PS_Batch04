
str1= "python programming is very easy to learn"
str2= str1.title()
str3=str2.split()
list1=[]
for char in str3:
    list1.append(char[0:-1]+char[-1].upper())
print(" ".join(list1))