word=input('enter word:')
digit=0
character=0
for ele in word:
    if ele.isalpha():
        character += 1
    elif ele.isnumeric():
        digit +=1

print('digits:',digit)
print('charactrer:',character)
