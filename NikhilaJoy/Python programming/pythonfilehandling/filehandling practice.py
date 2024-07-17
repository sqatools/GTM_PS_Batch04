#1). Python Program How to read a file in reading mode.
"""
def read_file(filename):
    file=open(filename,"r")
    result=file.read()
    print(result)
read_file("file1forpractice")
"""
"""
file=open("file1forpractice","r")
result=file.read()
print(result)
"""
#2). Python file program to overwrite the existing file content.
"""
def overwrite_file(filename,content):
    file=open(filename,"w")
    result=file.write(content)
    print(result)
content="you are overwritten"
overwrite_file("file1forpractice",content)
"""
"""
def read_file(filename):
    file=open(filename,"r")
    result=file.read()
    print(result)
    file.close()
    print(file.closed)
read_file("file1forpractice")
"""

#3).  Python file program to append data to an existing file.
"""
def append_file(filename,content):
    file = open(filename, "a")
    result = file.write(content)
    print(result)
content=("Added a new line using append")
append_file("file1forpractice",content)
"""
#4).  Python file program to get the file’s first three and last three lines.
"""
def read_file_byte_data(filename, num_byte):
    with open(filename, "r") as file:
        data = file.read(num_byte)
        print(data)
read_file_byte_data("file1forpractice",5)
"""
"""
def read_line(filename,linecount):
    file=open(filename,"r")
    data=file.readlines()
    for i in (data[:3]):
        print(i)
read_line("file1forpractice",4)
"""
#5). Python file program to get all the email ids from a text file.
"""
email_id=[]
file=open("file2practice","r")
file_data=file.read()
word=file_data.split(" ")
print(word)
for i in word:
    if "@" in i:
        email_id.append(i)
    else:
        continue
print(email_id)
"""
#6). Python file program to get a specific line from the file.
"""
file=open("file2practice","r")
file_data=file.readlines()
print(file_data[1])
"""
#7). Python file program to get odd lines from files and append them to separate files.
file=open("file2practice","r")
f2=open("write1.txt","a")
file_data=file.readlines()
print(file_data)
d=len(file_data)
#print(d)
for i in range(0,d):
    if i%2!=0:
        f2.write(file_data[i])
    else:
        pass
#print(file_data[1])