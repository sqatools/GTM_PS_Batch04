list=[4,6,8,3,7,11,14]
output = [ ]

for i in list:
    if i%2==0:
        output.append(i**2)
    else:
        output.append(i**3)
print("output list :", output)
