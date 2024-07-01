#How to Read a File in Reading Mode
# file=open('write_data.txt','r')
# data=file.read()
# print(data)
# file.close()

#program to overwrite the existing file content
# file=open('write_data.txt','w')
# file.write('line 5: This is china')
# file.close()
# file=open('write_data.txt','r')
# data=file.read()
# print(data)

#program to append data to an existing file
# file=open('write_data.txt','a')
# file.write('\nline 4: This is India')
# file.close()

#Program to get the file’s first three and last three lines
# file=open('test-data.txt','r')
# linelist=file.readline()
# # for i in (linelist[:5]):
# #    print(i)
#
# for i in (linelist[-8:]):
#     print(i)

#Program to get all the email ids from a text file
# email_list=[]
# file=open('test-data.txt','r')
# file=file.read()
# file_list=file.split()
# for word in file_list:
#     if '@' in word:
#         email_list.append(word)
# print(email_list)

#Python program to get a specific line from the file
# file=open('test-data.txt','r')
# data=file.readlines()
# print('2nd line :',data[1])

#Program to get odd lines from files and append them to separate files
# f1=open('write_data.txt','r')
# f2=open('new_data.txt','w')
# line_data=f1.readlines()
# for i in range(0,len(line_data)):
#     if (i%2==0):
#         f2.write(line_data[i])
#
# f2=open('new_data.txt','r')
# data=f2.read()
# print(data)

#Python file program to find the longest word in a file
# max_len=0
# max_word=''
# file=open('test_data.txt','r')
# data=file.read()
# word_list=data.split()
# for word in word_list:
#     if len(word)>max_len:
#         max_len=len(word)
#         max_word=word
# print(max_word)

#Program to count of a specific word in a file
# file=open('test_data.txt','r')
# data=file.read()
# word_list=data.split()
# count=0
# for word in word_list:
#     if word=='python':
#         count=count+1
# print(count)

#Program to copy the file’s contents to another file after converting it to lowercase
# f1=open('write_data.txt','r')
# f2=open('lower_case.txt','w')
# for line in f1:
#     f2.write(line.lower())
# f2=open('lower_case.txt','r')
# data=f2.read()
# print(data)

#Sort lines of file with line length size:
# f1=open('test_data.txt','r')
# lines=f1.readlines()
# temp=0
# for i in range(len(lines)):
#     for j in range(i+1,len(lines)):
#         if len(lines[i])> len(lines[j]):
#             temp=lines[i]
#             lines[i]=lines[j]
#             lines[j]=temp
# f1=open('sort.txt','w')
# relines=''.join(lines)
# f1.write(relines)
# f1=open('sort.txt','r')
# data=f1.read()
# print(data )

#program to get all odd and even length words in two lists
file=open('test-data.txt','r')
data=file.read().split()
even=[]
odd=[]
for word in data:
    if len(word)%2==0:
        even.append(word)
    else:
        odd.append(word)
print(even)
print(odd)



