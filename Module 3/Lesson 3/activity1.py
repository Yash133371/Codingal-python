with open("codingal.txt", "w") as f:
    f.write("Hello my name is penguin, I like python")

with open("codingal.txt", "r") as f:
    content = f.read()
    for word in content.split():
        print(word)