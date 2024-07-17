import os
import shutil
from datetime import datetime


date1=datetime.now()
print(date1)

today1=datetime.today()
print(today1)

dat_var=date1.strftime("%d-%m-%y %H:%M:%S")
print(dat_var)
# dir_path= os.getcwd()
# print(dir_path)
#
# # os.chdir("C:\Git_Repo\Automation_repo")
# # dir_path=os.getcwd()
# # print(dir_path)
# #
# # os.mkdir("batch02")
#
# #os.rmdir("batch01")
#
# os.rmdir("C:\\Git_Repo\\Automation_rep\\batch02")
#
# file_data=os.listdir("C:\Git_Repo\Automation_repo")
# print(file_data)
#
#
# path1="C:\Git_Repo\Automation_repo"
# filename="content_test.txt"
#
# file_path=os.path.join(path1,filename)
# print(file_path)
#
# filepath1="C:\\Git_Repo\\Automation_repo\\batch01"
# print(os.path.exists(filepath1))
#
# filepath2="C:\\Git_Repo\\Automation_repo\\batch03"
# print(os.path.exists(filepath2))
#
#
# filepath_a="C:\\Git_Repo\\Automation_repo\\subramanyam_file.txt"
# print(os.path.getsize(filepath_a))
# target_loc="C:\\Git_Repo\\Automation_repo\\batch01\\subramanyam_file.txt"
# target_loc2="C:\\Git_Repo\\Automation_repo\\batch01\\subramanyam_file_new.txt"
#
# #shutil.copy(filepath_a, target_loc)
# #shutil.copy(filepath_a, target_loc2)
#
# filepath_b="C:\\Git_Repo\\Automation_repo\\batch02\\subramanyam_file.txt"
#
# shutil.copy(filepath_a,filepath_b)

#
# folder_long_path="C:\\Git_Repo\\Automation_repo\\batch02\\s\\u\\b\\b\\u"
# #os.makedirs(folder_long_path)
#
# for i in range(10,15):
#     folder_long_path1=f"C:\\Git_Repo\\Automation_repo\\batch02\\s{i}"
#     os.mkdir(folder_long_path1)
# print("CPU count :", os.cpu_count())
#
# #os.system("notepad.exe")
# os.system("python Table.py")