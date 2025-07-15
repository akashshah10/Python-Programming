# Write a python program using function to convert Celsius to Fahrenheit.

def temp_convert(Celsius):
    Farhenheit = 9/5*(Celsius) + 32
    return Farhenheit

Celsius = float(input("Enter the temperature in Celsius: "))
 
a = temp_convert(Celsius)
print(a) 