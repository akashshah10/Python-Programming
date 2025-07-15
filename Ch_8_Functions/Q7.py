# Write a python function which converts inches to cms.

def inch_to_cm(inch):
    return inch * 2.54

n = float(input("Enter value in inches: "))
print(f"The corresponding value of {n} inch in cm is {inch_to_cm(n)}")