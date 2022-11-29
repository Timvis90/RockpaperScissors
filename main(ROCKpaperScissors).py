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

#Write your code below this line 👇

import random 

print("ROCK PAPER SCISSORS\n\n")

player_selection = int(input("Type 0 for rock, 1 for paper, or 2 scizzors to make your selection and hit enter \n\n"))

if player_selection == 0:
  print(rock + "\n\nyou selected rock")
elif player_selection == 1:
  print(paper + "\n\nyou selected paper")
else:
  print(scissors + "\n\nyou selected scissors")

computer_choice = random.randint(0,2)

if computer_choice == 0:
  print(rock + "\n\ncomputer selected rock")
elif computer_choice == 1:
  print(paper + "\n\ncomputer selected paper")
else:
  print(scissors + "\n\ncomputer selected scissors")

if computer_choice == player_selection:
  print("\nit is a tie!!!")
elif player_selection == 0 and computer_choice == 1:
  print("\nyou lose!")
elif player_selection == 0 and computer_choice == 2:
  print("\nyou win!")
elif player_selection == 1 and computer_choice == 0:
  print("\nyou win!")
elif player_selection == 1 and computer_choice == 2:
  print("\nyou lose!")
elif player_selection == 2 and computer_choice == 0:
  print("\nyou lose!")
elif player_selection == 2 and computer_choice == 1:
  print("\nyou win!")

