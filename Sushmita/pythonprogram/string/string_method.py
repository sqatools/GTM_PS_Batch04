print(dir(str),end='')

'''
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', 
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__',
 '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 
 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 
 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 
 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 
 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate',
  'upper', 'zfill']
'''

# convert the string into upper to lower and lower to upper
print('\n_',end=' ')
########
# upper() and lower() methods:

str_a = "Hello We Learning Python"
str_b="SUSHMITA"
print('\n upper:',str_a.upper())
print('Lower:',str_b.lower())

print('_'*50)

## swapcase method : This will convert upper to lower and lower to upper
print("swap case output :", str_a.swapcase()) # LLO wE lEARNING pYTHON

# isupper() and islower() method : This method will return the True and False if the string is upper or lower
str_b='sushmita'
print('Upeer:',str_b.islower())
str_a="SUSH"
print('Upeer:',str_a.isupper())
str_c='1234 '
print('Upeer:',str_c.isupper())

# title() method : This method will convert the string into title case, it means first character of each word will be capital
str1='i am learning python programming'
print('Tiltle:',str1.title())

# istitle() method: This method check the given string is title case or not.
str_f = "Python Programming"
print(str_f.istitle())
srt_2='sush md'
print(srt_2.istitle())

print("_"*50)
##########
# count() method : This method will return the count of any char/substring in given string.
str_g = "learning Is fun, python Is very easy"
print('count:',str_g.count('e'))
print('count of space:',str_g.count(' '))

#######
# index method : this method will return the index position of any char/substring
str_h = "Indian Cricket Team"
print('Index:',str_h.index('T')) #15
print('Index:',str_h.index('Team')) #15

###########
# find method() : This method return the index position of char/substring if
# it is available else it will return -1

str_k = "Learning is Fun"
print('find:',str_k.find('F')) #12
# if the string or char is not available then it will return output as -1
print('find:',str_k.find('T')) #-1

str2 = "Good Morning"
print(str2[:8:-1])

print("_"*50)
###################################
# replace method : this method replace the one word to another

str_a = "Hello We Are Learning Python"

op=str_a.replace('Python','Java')
print('Replace:',op)

output3 = str_a.replace("Python", "Java").replace("Are", "Were")
print("Output3 :", output3)

print("-"*50)
####################
# split() method : This method can break the string in list of substring.

str_1 = "Today India is playing good cricket"
str_2 = "India,will,win,the,match"
str_3 = "Learning%is%Fun"

op1=str_1.split(' ')
print('split method:',op1)
#['Today', 'India', 'is', 'playing', 'good', 'cricket']

op2=str_2.split(',')
print('split method:',op2)
#['India', 'will', 'win', 'the', 'match']

op3=str_3.split('%')
print('split method:',op3)

str_4 = "Pytnghon ProngramingAre"
op4=str_4.split('o')
print(op4)
#['Pytngh', 'n Pr', 'ngramingAre']

###################
print("_"*50)
# strip() method : This method remove the training spaces from given string
str_m = "  Python Programming  "
print(str_m)
print(str_m.strip()) #Python Programming

output2 = str_m.lstrip()
print(output2)

output3 = str_m.rstrip()
print(output3)

########################################
#join() method : This method can join any string with delimeters

str_j = "Learning"

output_j = "-".join(str_j)
print('op_j :',output_j) #L-e-a-r-n-i-n-g

string1='shastri'
op6=",".join(string1)
print('result :',op6) # s,h,a,s,t,r,i

####################################
print("_"*50)
# isalpha method will return if string only contains alphabates
str_a = "Hello"
print(str_a.isalpha())


# isnumeric : This method return true if string only contains numberic value
str_b = "34567"
print("check is numeric :", str_b.isnumeric()) # True

str_b1 = "34567 Word"
print("check is numeric :", str_b1.isnumeric()) # False

# isalnum: This method check if string only contains number and characters.
str_c = "234Virat"
print("check for string and numeric values :", str_c.isalnum())  # True

# isspace: this method check given char is space or not
str_e = "Hello good morning, I hoper you are doing good"

# isspace: this method check given char is space or not
str_e = "Hello good morning, I hoper you are doing good"

for char in str_e:
    print(char, ":", char.isspace())
