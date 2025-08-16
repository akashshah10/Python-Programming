class Python:
    language = "Py"    # --> Class attribute
    month = "Aug"      # --> Class attribute  

    def getInfo(self):
        print(f"The language is {self.language} and the month is {self.month}")

    @staticmethod     # --> It is a decorator
    def greet():
        print("Hello! How are you?")

akash = Python()
akash.name = "Akash"   # --> Instance/Object attribute 
akash.language = "C++" # --> Instance/Object attribute
print(akash.name, akash.language, akash.month)

# akash.getInfo()       ##This and the line below this both means the
Python.getInfo(akash)
akash.greet()


# self is not a keyword.
# It’s just a naming convention that almost all Python developers follow.
# You can use any valid variable name in place of self — Python will still work, because what matters is that the first parameter in an instance method always receives the object that called it.