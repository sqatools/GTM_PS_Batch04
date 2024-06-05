string=input('enter string:')
if len(string)<2:
    print(True)
else:
    print(string[:2]+string[-2:])

print('_'*50)


print(string[-2:]*4)
