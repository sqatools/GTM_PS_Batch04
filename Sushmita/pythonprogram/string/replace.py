#Replace the second occurrence of a characterresult
string='programming'
result=' '
for char in string:
    if char in result:
        result=result+'$'
    else:
        result=result+char

print('Result of string:',result)

#python program to get to swap the last character of a given string.
str='Sql Tool'
print(str[-1]+str[1:-1]+str[0])
