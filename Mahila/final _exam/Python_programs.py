# #1.
#
#
# result = []
#
# for i in range(4):
#     values = []
#     for j in range(1, 6):
#         values.append(5 * i + j)
#     result.append(values)
#
# print(result)
#
# 2.
#
#
#
# inp_list =["Hello", 45, "sqa",  23, 5, "Tools", 20]
#
# count = 0
#
# for i in inp_list:
#     if isinstance(i, int):
#         count += 1
#
# print("Integer count in given list : ",count)

# #3.
#
# input_list = [3, 5, 7, 8]
# element_to_insert = 'a'
# result = []
#
# for i in input_list:
#         result.append(element_to_insert)
#         result.append(i)
# print(result)

#4.
# dic_1 =  {'x':23,'y':10,'z':7}
# count = 0
# for i in dic_1.values():
#     count += i
#
# print(count)

#3.
#Python file program to read the data of two of the files created and add it to a new file.

def adding_two_files(file_name_1, file_name_2, file_name_3):
    with open(file_name_1, "r") as file1:
        file1_lines = file1.readlines()

    with open(file_name_2, "r") as file2:
        file2_lines = file2.readlines()

    with open(file_name_3, "a")as file3:
         for i in range(len(file1_lines)):
             file3.write(file1_lines[i])
             file3.write(file2_lines[i])


adding_two_files("file1_data.txt", "file2_data.txt", "file3_data.txt")

