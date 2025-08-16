class Python:
    language = "Py"    # --> Class attribute
    month = "Aug"      # --> Class attribute  

akash = Python()
akash.name = "Akash"   # --> Instance/Object attribute 
akash.language = "C++" # --> Instance/Object attribute
print(akash.name, akash.language, akash.month)


# Instance attributes, take preference over class attributes during assignment & retrieval. #