names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]

student_details=[(name,score) for name,score in zip(names,scores)]
print(student_details)

def read_file_byte_data(filename,num_byte):
    with open(filename,"r") as file:
        data=file.read(num_byte)
        print(data)
read_file_byte_data("first_file_py001.txt",110)