def adding_two_files(file_name_1, file_name_2, file_name_3):
    with open(file_name_1,"r") as file1:
        file1_lines=file1.readlines()


    with open(file_name_2,"r") as file2:
        file2_lines = file2.readlines()

    with open(file_name_3,"a") as file3:
        for i in range(len(file1_lines)):
            file3.write(file1_lines[i])
            file3.write(file2_lines[i])


adding_two_files("file1_data.txt", "file2_data.txt", "file3_data.txt")