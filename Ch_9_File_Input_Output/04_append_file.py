# string = "Akash is learning steadily, Ok the file is created"

# f = open("My_file.txt", "a") #w means write mode 

# f.write("\nAppended text")

# f.close()


#User input
text = input("Enter the text you want to append: ")

f = open("file2.txt", "a")
f.write(text + "\n")
f.close()