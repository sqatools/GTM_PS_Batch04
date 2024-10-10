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
#new_content = "\nAppending data to existing file"
#append_file("append_data.txt", new_content)

#2. append content to fresh file: It will create fresh file and add content to the file

#new_content = "\nAppending data to fresh file file"
#append_file("append_data_fresh.txt", new_content)



# read file with context manager
# context manager : context manager has its own enter and exist method, once we come
#                   out of the context manager, then file will be closed automatically
#                   no need to close the file explicitly.

def read_with_context(filename):
    with open(filename, "r") as file:
        file_data = file.read()
        print("file data :", file_data)
        print("is file closed in side:", file.closed)

    print("is file closed outside :", file.closed)


#read_with_context("test_data.txt")


# different read methods
"""
1. read specific number of bytes from file
2. read line
3. read list of lines
"""

#1. read specific number of bytes
def read_file_byte_data(filename, num_byte):
    with open(filename, "r") as file:
        data = file.read(num_byte)
        print(data)

#read_file_byte_data("test_data.txt", 10)

#2. read line : readline method read one line at a time and move cursor from begining
# of file to end of the each line.
def read_specific_number_lines(filename, line_nums):
    with open(filename, "r") as file:
        # print(file.readline(), end="")
        for _ in range(line_nums):
            print(file.readline(), end="")



#read_specific_number_lines("test_data.txt", 5)
"""
1. Other Git for Windows downloads
2. Standalone Installer
3. 32-bit Git for Windows Setup.
4. 64-bit Git for Windows Setup.
5. Portable ("thumbdrive edition")
"""

# read list of lines with readlines method.

def read_list_of_lines(filename):
    with open(filename, "r") as file:
        lines_list = file.readlines()
        print(lines_list)
    return  lines_list

# read_list_of_lines("test_data.txt")

def read_odd_number_line(filename):
    lines_list = read_list_of_lines(filename)
    for i in range(len(lines_list)):
        if (i+1)%2 != 0:
            print(lines_list[i])
        else:
            continue

#read_odd_number_line("test_data.txt")


def read_even_number_line(filename):
    lines_list = read_list_of_lines(filename)
    for i in range(len(lines_list)):
        if (i+1)%2 == 0:
            print(lines_list[i])
        else:
            continue

#read_even_number_line("test_data.txt")


# write a python to replace the values from word1 to word2:

def replace_file_data(filename, word1, word2):
    # open file in read mode, to read all content
    with open(filename, "r") as file:
        file_data = file.read()

    # replace the word1 with word2
    updated_data = file_data.replace(word1, word2)

   # re-write same file with write mode.
    with open(filename, "w") as file:
        file.write(updated_data)


#replace_file_data("test_data.txt", "Windows", "Python")

# write a python program to combine 2 files together and add in third file

def combine_two_files(file1, file2, file3):
    with open(file1, "r") as file1_obj:
        file1_lines = file1_obj.readlines()

    with open(file2, "r") as file2_obj:
        file2_lines = file2_obj.readlines()

    with open(file3, "a")as file3_obj:
         for i in range(len(file1_lines)):
             file3_obj.write(file1_lines[i])
             file3_obj.write(file2_lines[i])


combine_two_files("file1_data.txt", "file2_data.txt", "file3_data.txt")


