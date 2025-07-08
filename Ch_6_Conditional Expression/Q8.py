# Write a program to find out whether a given post is talking about “Akash” or not.

post = input("Enter the post: ")

if "Akash".lower() in post.lower():
    print("This post is about Akash")

else:
    print("This post is not about Akash")