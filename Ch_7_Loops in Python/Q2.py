# Write a program to print multiplication table of a given number using for loop.

n = int(input("Enter the number: "))

for i in range(1,11):
    print(f"{n} * {i} = {n * i}")
