"""
File Open mode
read(r) : when we open a file with read mode then we can read content of files

write(w)
append(a)
"""
# read content of the file
def read_file(filename):
    file = open(filename, "r")
    data = file.read()
    print("file data :", data)
    print(file.closed) # False
    file.close() # closing file
    print(file.closed) # True

#read_file("test_data.txt")
#read_file("E:\\Filesdata\\count_name.txt")

# write content to the file

def write_file(filename, content):
    file = open(filename, "w")
    file.write(content)
    file.close()

#1. write to existing file : This will overwrite the existing content of file
#content = "We are working on file handling"
#write_file("write_data.txt", content)

#2. : write content to new file: It will create new file if file is not available then add
# content to the file.
#content2 = "adding content to fresh file"
#write_file("write_fresh_data.txt", content2)


### Append content to the file ###

def append_file(filename, content):
    file = open(filename, "a")
    file.write(content)
    file.close()

#1. already available file : It will update the existing content of file
#   without removing old content
new_content = "\nAppending data to existing file"
append_file("append_data.txt", new_content)

#2. append content to fresh file: It will create fresh file and add content to the file

new_content = "\nAppending data to fresh file file"
append_file("append_data_fresh.txt", new_content)




