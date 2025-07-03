import os


print("Creating file")
with open("my_file.txt", "w") as f:
    f.write("Hello python!")

print("Reading file")
with open("my_file.txt", "r") as f:
    print(f.read())

print("Deleting file")
os.remove("my_file.txt")

if not os.path.exists("my_file.txt"):
    print("Succesfully deleted file")
else:
    print("Deleting was unsuccesfull")