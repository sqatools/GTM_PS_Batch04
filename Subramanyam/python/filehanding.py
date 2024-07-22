# def read_file(filename):
#     file=open(filename,"r",5)
#     data=file.read()
#     print("file data: ",data)
#     file.close()
# read_file("text_file")
# #read_file("C:\\Users\\subra\\OneDrive\\Desktop\\Python\\Python Notes\\file handling.7")

# def write_file(filename,contact):
#     file=open(filename,"w")
#     data=file.write(contact)
#     file.close()
#
#
# contact= " The syntax to open a file using with the statement is given below."
# write_file("text_file",contact)

# def append_file(filename,cotent2):
#     file=open(filename,"a")
#     data=file.write(cotent2)
#     file.close()
#
# contact= "\n 1.The syntax to open a file using with the statement is given below."
# append_file("text_file",contact)

# file=open("text_file","r")
# data=file.read()
# print(data)
# file.close()

# file=open("text_file","a")
# file.write("\n new line: new data 123456789 ")
# file.close()
# file=open("readcontent.txt","r")
# lineslist=file.readlines()
# for i in (lineslist[::-2]):
#     print(i)
#
# # for i in lineslist[-3:]:
# #     print(i)

# email_list=[]
# file=open("text_file","r")
# file_data=file.read()
# word_list=file_data.split(" ")
# for i in word_list:
#     if "@" in i:
#         email_list.append(i)
#     else:
#         continue
#
# print(email_list)
# file.close()

# def mail_list(filename):
#     email_list=[]
#     file=open(filename,"r")
#     file_data=file.read()
#     word_list=file_data.split(" ")
#     for word in word_list:
#         if "@" in word:
#             email_list.append(word)
#         else:
#             continue
#
#         return email_list
#     # print(email_list)
# filename1="text_file"
# mail_list(filename1)

# file=open("text_file",'r')
# data=file.readlines()
# print(data[4])
# file.close()

# f1=open("text_file",'r')
# f2=open("readcontent.txt",'w')
# lines_list=f1.readlines()
# for i in range(0,len(lines_list)):
#     if i%2==0:
#         f2.write(lines_list[i])
#     else:
#         pass
#
# f1.close()
# f2.close()
# Open 1st file in read mode
# f1 = open('text_file', 'r')
# # Open 2nd file in write mode
# f2 = open('readcontent.txt', 'w')
# # Read lines of the file
# lines_list = f1.readlines()
# # Iterate over lines
# for i in range(0, len(lines_list)):
# # Check for odd line
#     if(i % 2!= 0):
#     # Write lines to 2nd file
#         f2.write(lines_list[i])
#     else:
#         pass
# # Close the file
# f1.close()
# f2.close()

#
# result_list=[]
# with open("text_file",'r') as file:
#     while True:
#         line=file.readline()
#         if not line:
#             break
#         result_list.append(line)
#     print(result_list)

# max_word=''
# max_len=0
#
# with open("readcontent.txt","r") as file:
#     file_data=file.read()
#     word_list=file_data.split()
#     for word in word_list:
#         if len(word)>max_len:
#             max_len=len(word)
#             max_word=word
#         else:
#             continue
# print(max_word)
# print(max_len)


# file=open("text_file","r")
# data=file.read()
# words=data.split()
# count=0
# for word in words:
#     if word == 'India':
#         count= count+ 1
#
# print(count)


# import random
# lines =open("text_file","r").read().splitlines()
# data=random.choice(lines)
# print(data)

# with open("text_file","r") as file:
#     with open("readcontent.txt","a") as output:
#          for line in file:
#              output.write(line.upper())

# file=open("text_file","r")
# words=file.read().split()
# count=0
# for word in words:
#     count+=1
# print(count)

# with open("readcontent.txt",'r') as file:
#     file_lines=file.readlines()
#     for i in range(len(file_lines)):
#         for j in range(i+1,len(file_lines)):
#             if len(file_lines[i])>len(file_lines[j]):
#                 temp=file_lines[i]
#                 file_lines[i]=file_lines[j]
#                 file_lines[j]=temp
#             else:
#                 continue
# with open("text_file","w") as file:
#     all_file=" ".join(file_lines)
#     file.write(all_file)


# with open("readcontent.txt") as file:
#     file_lines=file.readlines()
#     file_lines.sort()
#     for i in file_lines:
#         print(i)
# with open("text_file","w") as file:
#     all_file="".join(file_lines)
#     file.write(all_file)

# import string,os
# if not os.path.exists("letters"):
#     os.makedirs("letters")
#
# for letter in string.ascii_uppercase:
#     with open(letter+".txt",'w') as f:
#         f.writelines(letter)

# with open("readcontent.txt","r") as file:
#     words=file.read().split()
#     even=[]
#     odd=[]
#     for word in words:
#         if len(word)%2==0:
#             even.append(word)
#         else:
#             odd.append(word)
#
# print(even)
# print(odd)
from random import random


# file=open("readcontent.txt","r")
# data=file.read().split()
# num=[]
# for val in data:
#     if val.isnumeric():
#         if len(val)==10:
#             num.append(val)
# file=open('text_file','a')
# all_num="\n".join(num)
# file.write(all_num)
# import random
# file1=random.randint(1,25)
# print(file1)
# f=[]
# for i in range(1,10):
#     f.append(i)

