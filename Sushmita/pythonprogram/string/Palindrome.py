#Get all the palindrome words from the string

string = "Python efe language aakaa hellolleh"

list1=string.split()
new_list=[]

for word in list1:
    if word==word[::-1] :
        new_list.append(word)

print(new_list)
