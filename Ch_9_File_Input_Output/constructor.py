class Python:
    language = "Py"    # --> Class attribute
    month = "Aug"      # --> Class attribute  

    def __init__(self):# --> __init__ is a dunder method which is automatically called
        print("I'm creating a new object")

    def getInfo(self):  
        print(f"The language is {self.language} and the month is {self.month}")

    @staticmethod      # --> It is a decorator
    def greet():
        print("Hello! How are you?")


akash = Python()
akash.name = "Akash"   # --> Instance/Object attribute 
akash.language = "C++" # --> Instance/Object attribute
print(akash.name, akash.language, akash.month)

akash.greet()
akash.getInfo()
