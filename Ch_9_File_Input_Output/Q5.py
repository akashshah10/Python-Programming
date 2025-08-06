# Repeat program 4 for a list of such words to be censored.

words  = ["error", "wrong"]

with open("file3.txt","r") as f:
    content = f.read()

for word in words:
    content = content.replace(word ,"#"*len(word))
with open("file3.txt","w") as f:
    content = f.write(content)
