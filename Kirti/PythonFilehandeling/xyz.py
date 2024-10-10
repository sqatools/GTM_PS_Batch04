#How To read file
def read_file(xyz):
    file = open(xyz, "r")
    data = file.read()
    print("xyz:", data)
read_file("xyz.txt")

#How to write the file
#Existing file

def write_file(xyz, content):
    file = open(xyz,"w")
    file.write(content)
    file.close()
content = "ABC and this is written in file"
write_file("xyz.txt",content)

#How to write the file
#New file

description = "ABC and this is written in file This will be written in new file"
write_file("newfile.txt",description)


# Append the coneten to the File existing
def append_file(aaa,cont2):
    file = open(aaa, "a")
    file.write(cont2)
    file.close()

cont2 = "\nHi this this the appended data to the exisitng file"
append_file("xyz.txt",cont2)

# Append the coneten to the File New?
def append_file(ooo,cont2):
    file = open(ooo, "a")
    file.write(cont2)
    file.close()

cont2 = "\nHi this the appended data to the New file"
append_file("ooo.txt",cont2)