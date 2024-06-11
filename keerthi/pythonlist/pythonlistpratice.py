list1 = [2, 4.5, 'python', [9, 0, 2], (1, 3, 5), {'c': 123, 'd' : 345}, {3, 7, 1, 4}, True]

print(list1, type(list1))

print(list1[3])
print(list1[-2])
print(list1[5]['d'])
print(list1[2][4])
print(list1[-3])

print('*'*50)

for val in list1:
    print(val)

print('*'*50)
# program to print all the even number from given list
lista=[2,5,4,1,6,9,0]
for val in lista:
    if val%2==0:
        print(val)

print('*'*50)

for i in range(len(lista)):
   # print(i,lista[i])
  if lista[i]%2==0:
      print(lista[i],lista)

print('*'*50)

#list slicing

print(lista[3:6])
print(lista[2:7])
print(lista[1:6])

print(lista[1:-3])
print(lista[2: -6: -1])
print(lista[::-2])
print(lista[::-1])

##########list methods#####
print()