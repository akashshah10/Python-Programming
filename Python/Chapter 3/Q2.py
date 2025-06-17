letter = '''Dear <|Name|>,
            You are selected!
            <|Date|>'''

print(letter.replace("<|Name|>","Akash").replace("<|Date|>","24 June"))  #This is called chaining. Here I have done done chaining of replace()