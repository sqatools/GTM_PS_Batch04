#Vowels in each word of string show as dictionary

string='we are learing python'

str_list=string.split()
dict1={}

vowel='a','e','i','o','u'
for word in str_list:
    count=0
    for char in word:
        if char in vowel:
            count=count+1
    dict1[word]=count
print(dict1)
