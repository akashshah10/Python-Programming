# Write a program to print multiplication table of a given number using for loop.
#Use while loop

n = int(input("Enter the number: "))
i = 1
while(i<11):
    print(f"{n} * {i} = {n*i}")
    i += 1