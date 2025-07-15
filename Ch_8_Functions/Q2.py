# Write a program using functions to find greatest of three numbers.

def greatest(a, b, c):
    if(a >= b and a >= c):
        return a
    
    elif(b >= a and b >= c):
        return b
    
    else:
        return c
    
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

max = greatest(a, b, c)

print(f"The greatest number is: {max}")