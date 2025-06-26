with open("my.txt", "r") as file:
    content = file.read()
    count = 0
    for line in content.split("\n"):
        if line:
            count += 1

print(count)