# str1="python"
# for i in range(len(str1)-1,-1,-1):
#     print(str1[i],end=" ")
#
# print()
# list1=[1,2,3,4,5]
# for i in range(len(list1)-1,-1,-1):
#     print(list1[i],end=" ")
# print()
# list2=sorted(list1,reverse=True)
# print(list2)
#
# count=len(str1)-1
# while count>=0:
#     print(str1[count],end=" ")
#     count-=1
# print()
#
# output=str1[::-1]
# print(output)
#
# str3=list(reversed(str1))
# print("".join(str3))
# print(str3)
#
# st="we are learning python"
# list1=st.split()
# list1.reverse()
# output=' '.join(list1)
# print(output)
#
# num=123
# rev=str(num)
# print("Reverse: ",rev[::-1])
#
# a='nitin'
# b=''
# for i in a:
#     b=i+b
#     print(b)
# if a==b:
#     print("yes")
# else:
#     print("No")
#
# num=10
# total=0
# for i in range(1,num+1):
#     total+=i
# print(total)
#
# num=55
# total_sum=0
# cn=1
# while cn<=num:
#     total_sum+=cn
#     cn+=1
# print(total_sum)
#
# def natural(n):
#     if n<=0:
#         return
#     natural(n-1)
#     print(n)
# natural(10)
#
#
# n1=10
# if n1<=0:
#     pass
# print(n1-1,end="")
# print()
# st1="We aRe LeArNinG pYtHOn"
# print(st1.upper())
# print(st1.lower())
# print(st1.swapcase())
# print(st1.isupper())
# print(st1.islower())
# print(st1.title())
# d="Python Programming"
# print(d.istitle())
# str_g = "learning Is fun, python Is very easy"
#
# print(str_g.count("e"))
#
# # str_g1=
# # print(str_g1)
# s1=" ".join(set(str_g.split()))
# print(s1)
#
# temp=" "
# for i in str_g:
#     if i not in temp:
#         print(i,":",str_g.count(i))
#         temp+=i
#     else:
#         continue
#
# print(temp)
# str_h = "Indian Cricket Team"
# print(str_h.find("n "))
# #print(str_h.replace("Cricket","cricket"))
#
# #print(str_h.replace("Cricket","cricket"))
# str_h1=str_h.replace("Cricket","cricket").replace("Indian","indian")
# print(str_h1)
#
for i in range(65,127):
    print(i,":",chr(i),end=" ")


str1 = "Code Learning is Fun"
vowels="aeiou"
output=""
count=0

for var1 in str1:
    print("char : ",var1,"outpur: ",output)
    if var1 in vowels and var1 not in output:
        output+=var1
        count+=1
    else:
        continue

print(output,count)

str2 = "We Are Learning Python Programming and Its Very Easy"
longest_word=""
max_len=0
word_list=str2.split(" ")
print(word_list)
for word in word_list:
    word_len=len(word)
    if word_len>max_len:
        max_len=word_len
        longest_word=word
    else:
        continue

    print(longest_word,max_len)
print(longest_word,max_len)