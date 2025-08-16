class Python:
    language = "Py"    # --> Class attribute
    month = "Aug"      # --> Class attribute  

akash = Python()
akash.name = "Akash"   # --> Instance/Object attribute 
print(akash.name, akash.language, akash.month)

miku = Python()
miku.name  = "Riju"    # --> Instance/Object attribute 
print(miku.month, miku.language, miku.name)

#Here name is instance/object attribute and language,month are class attributes as they directly belonmgs to the class