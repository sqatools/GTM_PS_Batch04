word = input('enter word:')
result = ''
for char in word:
    if char.isupper():
        print(char.lower(), end='')
    else:
        print(char, end='')
"""
input1 = input("Enter word: ")
result = ''
for char in input1:
    if char.isupper():
        print(char.lower(), end="")
    else:
        print(char, end="")
"""
