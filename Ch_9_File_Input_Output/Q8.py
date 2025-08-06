with open("this.txt") as f:
    content = f.read()

with open("copy.txt", "w") as f:
    new = f.write(content)