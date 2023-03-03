import random
print("Enter choice 1:rock, 2:paper, 3:scissor")
choice = input("choice(1/2/3)")
choice = int(choice)

computer_choice = random.randint(1, 3)
print(f"computer: {computer_choice}")
if choice == computer_choice:
    print("Draw")
elif choice == 1:
    if computer_choice == 2:
        print("Computer wins")
    else:
        print(" You win")
elif choice == 2:
    if computer_choice == 1:
        print("You wins")
    else:
        print("Commputer wins")
elif choice ==3:
    if computer_choice == 1:
        print("computer wins")
    else:
        print("You wins")