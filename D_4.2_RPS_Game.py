import random

print("Welcome to ROCK PAPER SCISSORS game")

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock , paper , scissors]

player_choice = int(input("What do you choose?Type 0 for ROCK , 1 for PAPER, 2 for SCISSORS:\n"))
print(game_images[player_choice])

computer_choice = random.randint(0,2)
print("computer chose:")
print(game_images[computer_choice])

print(f"Computer chose {computer_choice}")

if player_choice == 0 and computer_choice == 2 :
    print("You win!")

elif computer_choice == 0 and player_choice == 2:
    print("You lose")

elif computer_choice > player_choice :
    print("You lose")

elif computer_choice == player_choice :
    print("It's a draw")

else: print("You choose invalid number")