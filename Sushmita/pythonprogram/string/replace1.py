#Replace the words in the given string
string = "JAVA is the Best Programming Language in the Market"

# new_string=string.replace('JAVA','Pyhon')
#
# print(new_string)
list1=string.split()
for word in list1:
    if word=='JAVA':
        Index=list1.index(word)
        list1[Index]='python'

print(" ".join(list1))
