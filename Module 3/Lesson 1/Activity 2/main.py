file = open("penguin.myfile", "r")
print("Read mode-")
print(file.read())
file.close()

file = open("penguin.myfile", "w")
print("Write mode-")
file.write("Hello I'm Penguin")
file.close()

file = open("penguin.myfile", "a")
print("Append mode")
file.write(", I like Python")
file.close()