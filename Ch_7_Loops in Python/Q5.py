# Write a program to find whether a given number is prime or not.

num = int(input("Enter the number you want to check: "))

if(num <= 1):
    print(f"{num} is not a prime number")

else:
    for i in range(2, int(num/2)+1):
        if(num % i == 0):
            print(f"{num} is a not prime number")
            break

    else:
        print(f"{num} is a prime number")