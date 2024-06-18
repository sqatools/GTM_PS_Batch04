l=[2,6,3,1,5,7,4,8,9]
for i in l:
    if i%2==0:
        print(i,end=" ")
print()
for i in range(len(l)):
    if l[i]%2==0:
        print(l[i],end=" ")
print()

list_p = ['a', 'b', 'c', 'd']
list_q = [3, 6, 8, 1]

list_q.extend(list_p)
print("list p :", list_p)
print("list q :", list_q)


list_11 = [4, 6, 8, 22, 55, 12]
result = list_11.remove(55)
print("Result :", result)
print("list_11 :", list_11)


list_a=[4,6,8,3,7,11,14]
output=[]

for i in list_a:
    if i%2==0:
        output.append(i**2)

    else:
        output.append(i**3)

print(output)
