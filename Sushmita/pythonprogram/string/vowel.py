letter=input('enter string:')
vowel=['a','e','i','o','u']
for char in letter:
    if char in vowel :
        print(f'{char} is vowel')
    else:
        print(f'{char} is consoant')
