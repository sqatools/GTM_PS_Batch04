str1="Sqatools"

if len(str1)<2:
    print(True)
else:
    print(str1[:2]+str1[-2:])

str2=["i","am","learning","python"]
temp=0

for word in str2:
    a=len(word)
    if a>temp:
        temp=a
print(temp)

temp1=0
for  word1 in str2:
    a=len(word1)
    if a>temp1:
        temp1=a
print(temp1)

print(str1[-2:]*4)
print("_"*100)
if len(str1)%8==0:
    print(str1[::-1])

letter="aerv"

for word in letter:
    if word=="a" or word=="e" or word =="i" or word=="o" or word=="u":
        print(f"{word} is vowel")
    else:
        print(f"{word} is consonant")

str3="we are learning python"
output=str3.split(" ")

print("longest word:",max(output,key=len))
print("smallest word: ",min(output,key=len))


lst1=["we","are","learning","Python","programming"]
temp=0
char=""
for wor in lst1:
    a=len(wor)
   # if char in wor:
    #    char = char + wor

    if a>temp:
        temp=a
        char=wor


print(temp)
print(char)


st1="python programming"
dict1={}
for i in st1:
    if i in dict1:
        dict1[i]=+1
    else:
        dict1[i]=1

print(dict1)

st="code learning is fun"
vowels="aeiou"
out=""
te=0
for var1 in st:
    print("char",var1,"output",out)
    if var1 in vowels:
        out=out+var1
        te+=1
    else:
        continue

print("output:",out,te)

