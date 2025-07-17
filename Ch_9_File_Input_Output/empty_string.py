print(bool(""))        # Output: False
print(bool("Akash"))   # Output: True

# Since empty strings have no content, Python treats them as False.

a = "Akash"
if(a == "" or "Akash"): #A non empty string is always treated as True in boolean context. Hence, the output is Ok
    
    print("Ok")

else:
    print("No")
