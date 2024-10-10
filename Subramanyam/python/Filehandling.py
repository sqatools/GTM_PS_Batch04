# import difflib
#
# with open("text_file") as file_1:
#     file_1_text=file_1.readlines()
# with open("readcontent.txt") as file_2:
#     file_2_text=file_2.readlines()
# for lines in difflib.unified_diff(
#         file_1_text,file_2_text,fromfile="filename",
#         tofile="file.txt",lineterm=""):
#     print(lines)
#
# file=open("text_file","r")
# data=file.readlines()
# count=0
#
# for i in data:
#     count+=1
# print(count)
#
# import os
# info=os.stat("text_file")
# print("size of file: ",info.st_size)

# tup=('1','2','3',"hello")
# f=open("readcontent.txt","w")
# f.write("".join(tup))
# f.close()
# f1=open("readcontent.txt","r")
# print(f1.closed)
# f1.close()
# print(f1.closed)
# file=open("text_file","r")
# file_data=file.read().split()
# list1=[]
# for words in file_data:
#     # for char in words:
#     list1.append(words)
# print(list1)
# data=data2=""
# with open("readcontent.txt","r") as f:
#     data=f.read()
# with open("readcontent1.txt","r") as f:
#     data2=f.read()
#
# data+="\n"
#
# data+=data2
#
# with open("writefile.txt","w") as f:
#     f.write(data)

# fil=open("readcontent1.txt")
# words=fil.read().split()
# count=0
# special=['!','@','#','$','%','^','&','*','(',':',";"]
# for i in words:
#     for j in i:
#         if j  in special:
#             count+=1

# print(count)

# file=open("readcontent.txt")
# # file.readline()
# # print(file.tell())
# # file.seek(10)
# # print(file.tell())
# data=list(file.readlines())
# for i in reversed(data):
#     print(i)
# i=0
# while i<3:
#     print(i)
#     i++
#     print(i+1)

# f1=open("readcontent.txt","r")
# f2=open("writefile.txt","a")
# lines=f1.readlines()
# for line in lines:
#     if "t" in line:
#         f2.write(line)
#
# f1.close()
# f2.close()

# file=open("readcontent.txt")
# words=file.read().split()
# for word in words:
#     if len(word)<5:
#         print(word,end=" ")
#
# file=open("readcontent.txt","r")
# data=file.read()
# data.replace(" ",'_')
# file1=open("file2.txt","w")
# file1.write(data)

def read_file_byte_data(filename,num_byte):
    with open(filename,"r") as file:
        data=file.read(num_byte)
        print(data)
# read_file_byte_data("text_file",10)

def read_file_byte_data(filename):
    with open(filename,"r") as file:
        data=file.readlines()
        #print(data)
    return data
#read_file_byte_data("text_file")

def odd_lines_list(filename):
    list_lines=read_file_byte_data(filename)
    for i in range(len(list_lines)):
        if (i+1)%2!=0:
            print(list_lines[i],end="")
        else:
            continue
#odd_lines_list("text_file")



def read_file_lines(filename,lines_num):
    with open(filename,"r") as file:

        for line in range(lines_num):
            print(file.readline(),end="")

#read_file_lines("text_file",5)


def read_file_lines(filename):
    with open(filename,"r") as file:

        for line in filename:
            print(file.readline(),end="")

#read_file_lines("text_file")

def replace_words(filename,word1,word2):
    with open(filename,"r") as file:
        data = file.read()
    updated_data=data.replace(word1,word2)

    with open(filename,"w") as file:
        file.write(updated_data)

#replace_words("test_data.txt","github","Git")

def combination_two_file(file1,file2,file3):
    with open(file1,'r') as file1:
        file1_lines=file1.readlines()

    with open(file2,'r') as file2:
        file2_line=file2.readlines()

    with open(file3,'a') as file3:
        for i in range(len(file1_lines)):
            file3.write(file1_lines[i])
            file3.write(file2_line[i])

combination_two_file("readcontent.txt",'readcontent1.txt','testfile.txt')