from random import randrange

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissor]
computerSelect = randrange(0, 3)
userSelect = int(input("What do you choose ? Type 0 for Rock, 1 for Paper, 2 for Scissors "))
if userSelect == computerSelect:
    print(options[userSelect])
    print("Computer chose")
    print(options[computerSelect])
    print("Equals")
elif userSelect - computerSelect == 1 or (userSelect == 0 and computerSelect == 2):
    print(options[userSelect])
    print("Computer chose")
    print(options[computerSelect])
    print("You win")
else:
    print(options[userSelect])
    print("Computer chose")
    print(options[computerSelect])
    print("You loose")
