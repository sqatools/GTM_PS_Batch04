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



oupt=st.split()

print("longest word",max(oupt,key=len))
print("short ward",min(oupt,key=len))



df="Helllllo ffdfdas sdfsfsd sssfdddd"
chari=" "
counti=0

temp2=1
for va in range(len(df)-1):
    if df[va]==df[va+1]:
        temp2=temp2+1
        if temp > counti:
            counti=temp2
            chari=df[va]
        else:
            temp2=1


print("char max",chari,"\nmax count",counti)


thei=0

for i in df:
    thei+=1

print("without count len funtion",thei)
print("with len function",len(df))


st2="programming"
st3=""

for i in st2:
    if i in st3:
        st3=st3+"$"
    else:
        st3=st3+i
print("result",st3)

print(st2[::-1])
print(st2[-1]+st2[1:-1]+st2[0])


string1="its online learning"
list1=string1.split(" ")

for word2 in list1:
    new_word=word2[-1]+word2[1:-1]+word2[0]
    index=list1.index(word2)
    list1[index]=new_word
print(" ".join(list1))

inp="we are learning python codding"
lit=inp.split(" ")
vowels="aeiou"
dictionary=dict()

for i in lit:
    count=0
    for j in i:
        if j in vowels:
            count+=1
    dictionary[i]=count
print(dictionary)

s="sqa tools learning"
result=" "
vowels1=['a','e','i','o','u','A','E','I','O','U']

for i in s:
    if i in vowels1:
        result=result+i*3
    else:
        result=result+i*2
print(result)