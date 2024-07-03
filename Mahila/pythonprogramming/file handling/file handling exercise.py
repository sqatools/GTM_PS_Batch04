# #How to Read a File in Reading Mode
#
# #read with function
# def read_file(filename):
#     file = open(filename,"r")
#     data = file.read()
#     print(data)
#     file.close()
# read_file("File_handling_read")
#
# print("-"*80)
#
# #read without function
# file=open("File_handling_read","r")
# data = file.read()
# print(data)
# file.close()
#
# print("-"*80)
#program to overwrite the existing file content

#with function
# def write_ex(filename):
#     val=open(filename,"w")
#     val.write(content)
#     val.close()
#
# content = "This is china"
# write_ex("file_handling_override")
#
# #without function
#
# file=open("file_handling_override","w")
# file.write("This is India")
# file.close()
# #

#abend data to an existing file

# def apend(filename):
#     file = open(filename , "a")
#     data=file.write(content)
#     file.close()
# content = ("\nnewly added lines")
# apend("file_handling_override")
#
# #without function
#
# file= open("file_handling_override" , "a")
# file.write("\nwe are learning python")
# file.close()

#to get the file’s first three and last three lines

# file = open("readlines" , "r")
# data = file.readlines()
#
# for val in (data[:3]):
#     print(val)
# for val in (data[-3:]):
#     print(val)

#Program to get all the email ids from a text file
# List = [ ]
# file = open("readlines","r")
#
# data = file.read()
# word_list = data.split(" ")
# for word in word_list:
#     if "@gmail" in word:
#          List.append(word)
#     else:
#         continue
# print(List)
# file.close()

#Python program to get a specific line from the file
#
# file = open("readlines","r")
#
# data = file.readlines()
# print(data[0])

#Program to get odd lines from files and append them to separate files
# f1 = open("readlines","r")
# f2 = open("newfile","w")
# data = f1.readline()
#
# for val in range(0, len(data)):
#     if (val%2 !=0):
#         f2.write(data[val])
#     else:
#         pass
# f1.close()
# f2.close()

# length og max variable
max_word = ''
max_len = 0

file = open("readlines","r")
file_data = file.read()
word_list = file_data.split()
for word in word_list:
    if len(word) > max_len:
        max_len = len(word)
        max_word = word
    else:
        continue
print("Max length word :", max_word)
print("Max lenght :", max_len)











