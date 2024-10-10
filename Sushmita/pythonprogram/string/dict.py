string="We are Learning Python Codding"
str=string.split(' ')
#print(str)
vowel=['a','e','i','o','u']
dictinory=dict()
for word in str:
    count=0
    for char in word:
        if char in vowel:
            count=count+1
    dictinory[word]=count

print(dictinory)
