# Write a python program to rename a file to “renamed_by_ python.txt
import os

with open("name.txt") as f:
    content = f.read()

with open("renamed_by_ python.txt", "w")as f:
    f.write(content)

os.remove("name.txt")