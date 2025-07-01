# If the names of 2 friends are same; what will happen to the program in problem 6?

d = {}

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name : lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name : lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name : lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name : lang})

print(d)

#In this case update method will keep updating, which means that the last key will be printed. If we want to get both the keys then we have to use the list class