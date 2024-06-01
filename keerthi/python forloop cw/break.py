n=100
for n in range(1,100):
    prime=True
    for i in range(2,n):
        if n%i==0:
          prime = False
          break
    else:
        continue
    if prime:
        print(n,end=' ')
    else:
        pass
