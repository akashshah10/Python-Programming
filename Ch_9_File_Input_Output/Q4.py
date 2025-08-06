# A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.

word  = input("Enter the word you want to replace: ")

with open("Donkey.txt","r") as f:
    content = f.read()

content_new = content.replace(word , "######")
with open("Donkey.txt","w") as f:
    content = f.write(content_new)
