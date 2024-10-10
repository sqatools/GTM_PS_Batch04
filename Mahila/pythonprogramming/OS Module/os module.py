import os

########### get current working directory
# dir_path = os.getcwd()
# print(dir_path)

#D:\GitRepo\AutomationRepo\Seleniumpython\GTM_PS_Batch04\Mahila\pythonprogramming\OS Module

#####################Change current directory

# os.chdir("D:\\filedata")
#
# dir_path = os.getcwd()
# print(dir_path)
######D:\\filedata

##### create directory#####
#os.mkdir("batch05")

################remove directory ######
#os.rmdir("batch04")  # remove folder from current directory

##########get list of files and folders
#
# file_data = os.listdir("D:\\GitRepo\AutomationRepo\Seleniumpython\GTM_PS_Batch04\Mahila\pythonprogramming")
# print(file_data)

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
