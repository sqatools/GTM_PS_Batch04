import os
import shutil

# get current working directory
dir_path = os.getcwd()
print(dir_path)
# E:\Trainings\GTM_PS_Batch04_13May24\GTM_PS_Batch04\Deepesh\PythonProgramming\OS_Module

# Change working directory
'''
os.chdir("c:\\Filesdata")
dir_path = os.getcwd()
print(dir_path)
# E:\Filesdata

'''



##### create directory#####
os.mkdir("batch04")

#####  remove directory ######
# os.rmdir("batch04")  # remove folder from current directory
# os.rmdir("c:\\Filesdata\\batch04")  # remove folder from specific path

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


###### join two path and create a new path #####
print("_"*50)
path1= "E:\\Filesdata"
filename = "count_name.txt"

file_path = os.path.join(path1, filename)
print(file_path)

#######################
# check file exist
filepath1 = "E:\Filesdata\count_name.txt"
filepath2 = "E:\Filesdata\count_name123.txt"
print("file exist file1:", os.path.exists(filepath1)) # True
print("file exist file2:", os.path.exists(filepath2)) # False

#### check given path is file or folder ####
print("+"*50)
filepath3 = "E:\Filesdata\count_name.txt"
print("check given path is file :", os.path.isfile(filepath3))

filepath4 = "E:\Filesdata\BI10"

print("check given path is folder filepath4:", os.path.isdir(filepath4)) # True
print("check given path is folder filepath3 :", os.path.isdir(filepath3)) # False

###### Copy file from one location to another location ####

filepath_a = "E:\\Filesdata\\count_name.txt"
target_loc = "E:\\Filesdata\\batch04\\count_name.txt"
target_loc2 = "E:\\Filesdata\\batch04\\count_name_new.txt"

new_folder = "batch05"
folder_path =  "E:\\Filesdata\\batch05"
filepath_b  =  "E:\\Filesdata\\batch05\\count_name.txt"
shutil.copy(filepath_a, target_loc)
shutil.copy(filepath_a, target_loc2)

#os.mkdir(folder_path)
shutil.copy(filepath_a, filepath_b)


##### create entire folder path ######
"""
folder_path_long_path =  "E:\\Filesdata\\batch05\\f1\\f2\\f3\\f4\\f5"
os.makedirs(folder_path_long_path)


#### create multiple folders on same location #####
for i in range(10, 15):
    folder_path =  f"E:\\Filesdata\\batch05\\f{i}"
    os.mkdir(folder_path)
"""
#### get size of file ######
file_path_c = "E:\\Filesdata\\batch05\\count_name.txt"

print("file size :", os.path.getsize(file_path_c))  # 980 bytes

#### Get CPU count #######
print("CPU count :", os.cpu_count())  # 8

#### run window command #####
#os.system("notepad.exe")
#os.system("control")
#os.system("appwiz.cpl")

os.system("python python_test_file.py")
