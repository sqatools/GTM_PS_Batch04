#Most simultaneously repeated character in string
str='Hellllo ptyhhhhonnn'
max_char_count=0
max_char_repeat=''
temp =1
for i in range(len(str)-1) :
    if str[i]==str[i+1]:
        temp=temp+1
        if temp>max_char_count:
            max_char_count=temp
            max_char_repeat=str[i]
        else:
            temp=1
print('Max repeated char:',max_char_repeat,
    '\n max repeated count:',max_char_count )

'''
output
Max repeated char: n 
 max repeated count: 9
'''
