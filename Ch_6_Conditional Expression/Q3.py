# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

m1 = int(input("enter first subject marks: "))
m2 = int(input("enter second subject marks: "))
m3 = int(input("enter third subject marks: "))

sum = m1 + m2 + m3

if(m1 or m2 or m3 >= 100 or m1 or m2 or m3 < 0):
    print("Invalid marks")

elif (m1 >= 33 and m2 >= 33 and m3 >= 33 and ((sum/300)*100) >=40):
    print("Passed")

else: 
    print("Failed")