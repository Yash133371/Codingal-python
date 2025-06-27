file = open("codingal.txt")
for line in file:
    print(line)
    print("Next line.")
file.close()

file = open("codingal.txt")
print("Reading the first line")
print(file.readline())