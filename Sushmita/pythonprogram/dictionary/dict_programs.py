#Python program to iterate over a dictionary.
D1={'a':1,'b':2}
for val in D1:
    print(val,':',D1[val])

print('_'*50)
#Python program to create a dictionary in the given form.
n=4
D2={}

for i in range(1,4+1):
    D2.update({i:i**3})
print(D2)
