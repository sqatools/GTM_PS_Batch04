import os

# get current working directory
dir_path = os.getcwd()
print(dir_path)
#C:\GitRepo\Sushmitashastri23\Newpython\GTM_PS_Batch04\Sushmita\pythonprogram\OS module1

# Change working directory


# os.chdir("D:\\Filesdata")
# dir_path = os.getcwd()
# print(dir_path)
# # E:\Filesdata

##### create directory#####
#os.mkdir("batch04")

#####  remove directory ######
# os.rmdir("batch04")  # remove folder from current directory
# os.rmdir("E:\\Filesdata\\batch04")  # remove folder from specific path

##### Get list of files and folder #####

file_data = os.listdir("C:\GitRepo")
print(file_data)
#['Pythonselenium', 'Sushmitashastri23']
