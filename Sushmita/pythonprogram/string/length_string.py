word=input('enter string:')
temp=0
for char in word:
    a=len(char)
    if a > temp:
        temp=a
print(temp)
