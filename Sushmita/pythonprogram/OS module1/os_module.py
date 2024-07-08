import os
import shutil
# get current working directory
dir_path = os.getcwd()
print(dir_path)
#C:\GitRepo\Sushmitashastri23\Newpython\GTM_PS_Batch04\Sushmita\pythonprogram\OS module1

# Change working directory


#os.chdir("D:\\Filesdata")
##dir_path = os.getcwd()
#print(dir_path)
# # E:\Filesdata

##### create directory#####
#os.mkdir("batch04")

#####  remove directory ######
# os.rmdir("batch04")  # remove folder from current directory
# os.rmdir("E:\\Filesdata\\batch04")  # remove folder from specific path

##### Get list of files and folder #####

#file_data = os.listdir("C:\GitRepo")
#print(file_data)
#['Pythonselenium', 'Sushmitashastri23']

###### join two path and create a new path #####
# print("_"*50)
# path1="C:\python"
# filename = "count_name.txt"
# file_path = os.path.join(path1, filename)
# print(file_path)

#######################
# check file exist
filepath1 = "C:\python\count_name.txt"
filepath2 = "C:\python\count_name.txt123.txt"
print("file exist file1:", os.path.exists(filepath1)) # True
print("file exist file2:", os.path.exists(filepath2)) # False

#### check given path is file or folder ####
print("+"*50)
filepath3 = "C:\python\count_name.txt"
print("check given path is file :", os.path.isfile(filepath3))

filepath4 = "C:\python\python program"
print("check given path is folder filepath4:", os.path.isdir(filepath4))
print("check given path is folder filepath3 :", os.path.isdir(filepath3))

###### Copy file from one location to another location ####

filepath_a = "C:\\python\\count_name.txt"
target_loc = "C:\\python\\python program\\count_name.txt"
target_loc2 = "C:\\python\\python program\\count_name_new.txt"

new_folder = "batch05"
folder_path =  "C:\\python\\batch05"
filepath_b  =  "C:\\python\\batch05\\count_name.txt"
shutil.copy(filepath_a, target_loc)
shutil.copy(filepath_a, target_loc2)

#os.mkdir(folder_path)
shutil.copy(filepath_a, filepath_b)

##### create entire folder path ######
"""
folder_path_long_path =  "C:\\python\\batch05\\f1\\f2\\f3\\f4\\f5"
os.makedirs(folder_path_long_path)

#### create multiple folders on same location #####
for i in range(10, 15):
    folder_path =  f"C:\\python\\batch05\\f{i}"
    os.mkdir(folder_path)
"""

#### get size of file ######
file_path_c = "C:\\python\\batch05\\count_name.txt"

print("file size :", os.path.getsize(file_path_c))

#### Get CPU count #######
print("CPU count :", os.cpu_count())  # 8

#### run window command #####
#os.system("notepad.exe")
#os.system("control")
#os.system("appwiz.cpl")

os.system("python python_test_file.py")
