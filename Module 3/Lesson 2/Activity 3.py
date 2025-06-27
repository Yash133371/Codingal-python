file = open("codingal.txt", "r")
for line in file:
    if not line.startswith("Coding"):
        print(line)
        
file.close()