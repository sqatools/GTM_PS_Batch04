import os

# get current working directory
dir_path = os.getcwd()
print(dir_path)
# E:\Trainings\GTM_PS_Batch04_13May24\GTM_PS_Batch04\Deepesh\PythonProgramming\OS_Module

# Change working directory

"""
os.chdir("E:\\Filesdata")
dir_path = os.getcwd()
print(dir_path)
# E:\Filesdata
"""

##### create directory#####
# os.mkdir("batch04")

#####  remove directory ######
# os.rmdir("batch04")  # remove folder from current directory
# os.rmdir("E:\\Filesdata\\batch04")  # remove folder from specific path

##### Get list of files and folder #####

file_data = os.listdir("E:\\Filesdata")
print(file_data)
# ['BI10', 'BI11', 'Bi12', 'BI13', 'BI14', 'Bi15', 'count_name.txt',
# 'dsddfasd.py', 'Employee_details (2).xlsx', 'employee_details - Copy.txt',
# 'employee_details.txt', 'Employee_details.xlsx', 'f1', 'file1 - Copy.txt',
# 'file1.txt', 'fsdfasdfsadf.xlsx', 'get_line_file1.txt', 'get_line_file2.txt',
# 'gmt_batch03', 'Login_failure.png', 'myfiles - Copy (2).jpg', 'myfiles - Copy.jpg',
# 'myfiles.jpg', 'New Text Document - Copy (2).txt', 'New Text Document - Copy (3).txt',
# 'New Text Document - Copy (4).txt', 'New Text Document - Copy.txt', 'New Text Document.txt',
# 'newfile - Copy.xlsx', 'newfile.xlsx', 'newfolder1', 'pythonlearning.xlsx', 'randomdata.xls',
# 'read_excel_sheet.py', 'replace_content.txt', 'replace_content2.txt', 'Tavet',
# 'testdata123.txt', 'testfile-newfile.txt', 'testfile.txt', 'testreadfile.txt',
# 'test_data - Copy.xlsx', 'test_data.xlsx', 'test_data2.xls', 'userinput.txt',
# 'write_excel_data.py', 'write_excel_data_345.py', 'write_new_file.txt']
