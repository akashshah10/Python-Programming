# Write a recursive function to calculate the sum of first n natural numbers.

def recursive_sum(n):
    if(n == 1):
        return 1
    return n + recursive_sum(n-1)

n = (int(input("Enter the value of n: ")))
print(f"The sum of first {n} natural nos. is: {recursive_sum(n)}")
