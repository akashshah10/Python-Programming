# Write a program to find the greatest of four numbers entered by the user.

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
n4 = int(input("Enter fourth number: "))

if n1 >= n2 and n1 >= n3 and n1 >= n4:
    print("First number:", n1, "is greatest")

elif n2 >= n1 and n2 >= n3 and n2 >= n4:
    print("Second number:", n2, "is greatest")

elif n3 >= n1 and n3 >= n2 and n3 >= n4:
    print("Third number:", n3, "is greatest")

else:
    print("Fourth number:", n4, "is greatest")
