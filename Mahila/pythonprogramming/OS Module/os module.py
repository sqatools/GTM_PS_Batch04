import os

########### get current working directory
dir_path = os.getcwd()
print(dir_path)

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

file_data = os.listdir("D:\\GitRepo\AutomationRepo\Seleniumpython\GTM_PS_Batch04\Mahila\pythonprogramming")
print(file_data)


