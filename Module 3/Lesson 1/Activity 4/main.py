file_name = input("Enter the file name: ")
try:
    file = open(file_name, "r")
    print("File content-")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File dosen't exist")