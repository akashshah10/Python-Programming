a = int(input("Enter your age: "))

#If statement 1
if(a % 2 == 0):
    print("Even")
#End of if statement 2

#If statement 2
if( a >= 18):
    print("Verified")
    print("OK!")

elif(a < 0):
    print("Invalid age")

elif(a == 0):
    print("not born!")

else:
    print("Children are not allowed")

    print("End of Program")