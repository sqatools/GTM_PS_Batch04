list_1 = [4, 6, 8, 3, 7, 11, 14]
output = []

for val in list_1:
    if val % 2 == 0:
        output.append(val ** 2)
    else:
        output.append(val ** 3)
print(output)
