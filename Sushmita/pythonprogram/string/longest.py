string='i am learning python'
str1=string.split(' ')
print(str1)
print('longest word:',max(str1,key=len))
print('shortest word:',min(str1,key=len))
