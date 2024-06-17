L1 = [2, 3, 4, 5, (4, 8, 9, 0), "Hi", 'Hello', {'x': 111, 'y': 222, 'z': 333}, {0, 9, 8, 7}, False]

print(L1, type(L1))

print(L1[6])

print(L1[-3])

print(L1[4][1])

print(L1[7]['y'])

for val in L1:
    print(val)

L2 = [1, 2, 3, 4, 5]
for val in L2:
    if val % 2 == 0:
        print(val)

print("_"*50)
for i in range(len(L2)):
    if L2[i] % 2 == 0:
        print(L2[i], end=' ')


