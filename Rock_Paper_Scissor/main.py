#Scissor Ladder game
#Scissor wins against Paper, Paper wins against Rock, Rock wins against Scissor
#Scissor: 1, Paper: 0, Rock: -1
import random

computer = random.choice([1, 0, -1])

choice = input("Enter your choice: ").lower()

my_dict = {"s":1, "p": 0, "r": -1}
reverse_dict = {1:"Scissor", 0:"Paper", -1: "Rock"}

if(choice not in my_dict):
    print("Invalid Input")

else:
    my_choice = my_dict[choice]

    print(f"You chose: {reverse_dict[my_choice]}\nComputer chose: {reverse_dict[computer]}")

    if(computer == my_choice):
        print("Game tie")

    else:
        if(computer == 1 and my_choice == 0):
            print("You lose")
        elif(computer == 1 and my_choice == -1):
            print("You win")

        elif(computer == 0 and my_choice == 1):
            print("You win")
        elif(computer == 0 and my_choice  == -1):
            print("You lose")

        elif(computer == -1 and my_choice == 1):
            print("You lose")
        elif(computer == -1 and my_choice  == 0):
            print("You win")