f = open("file.txt")

# lines = f.readlines()
# print(lines, type(lines))
#Above commented out code is the code to read all lines of a file

# f.readline() is a method used to read one line at a time from a file.

# line1 = f.readline()
# print(line1,type(line1))

# line2 = f.readline()
# print(line2,type(line2))

# line3 = f.readline()
# print(line3,type(line3))

# line4 = f.readline()
# print(line4,type(line4))

# line5 = f.readline()
# print(line5 =="")
# print(line5,type(line5)) -- It returns an empty string


#The above process is very long. We can do it using loops
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()


f.close()