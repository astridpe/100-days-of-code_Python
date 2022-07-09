import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

choices = [rock, paper, scissors]
computer_index = random.randint(0, len(choices) - 1)
computer_choice = choices[computer_index]

if choice == 0:
    print(rock)
    print("Computer chose:")
    print(computer_choice)
    if computer_choice == choices[0]:
        print("Its a draw.")
    elif computer_choice == choices[2]:
        print("You win!")
    else:
        print("You lose.")

elif choice == 1:
    print(paper)
    print("Computer chose:")
    print(computer_choice)
    if computer_choice == choices[1]:
        print("Its a draw.")
    elif computer_choice == choices[0]:
        print("You win!")
    else:
        print("You lose.")

elif choice == 2:
    print(scissors)
    print("Computer chose:")
    print(computer_choice)
    if computer_choice == choices[2]:
        print("Its a draw.")
    elif computer_choice == choices[1]:
        print("You win!")
    else:
        print("You lose.")

else:
    print(f"{choice} is not a valid number. You lose!")
