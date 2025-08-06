# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.
search = input("Enter your string: ")
with open("poem.txt") as f:
    content = f.read()
    if(search in content):
        print("Found the string")

    else:
        print("No such string")

#The above code accepts user input and checks whether the desired string is present or not and uses "with" to open,close and read the text


# f  = open("poem.txt")
# content = f.read()
# if("Twinkle" in content):
#     print("Found the string")

# else:
#     print("No such string")
# f.close()

#In the above code we have to explicitly close the file so the first method is more reliable and usable