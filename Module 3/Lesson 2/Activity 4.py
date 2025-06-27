file = open("codingal.txt", "r")
cont = file.readlines()
for i, line in enumerate(cont, start=1):
    if i % 2 == 1:
        print(line)
    else:
        print("Line is even.")

file.close()