f = open("file2.txt")
print(f.read())
f.close()

#The burden of f.close() in much. Hence we use another method for f.close()

# Instead we can use the with statement

with open("file2.txt") as f:
    print(f.read())

#Here we don't have to explicitly close the file. The with method is dafer, cleaner and more reliable