# Rock Paper Scissors ASCII Art

# Rock
import random
Rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper

Paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
Scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
game=[Rock,Paper,Scissors]

User_Choice=int(input("what do you choose for 0 for rock, 1 for paper,2 for Scissors \n"))
print(game[User_Choice])

Computer_choice=random.randint(0,2)
print(game[Computer_choice])

if User_Choice==0 and Computer_choice==2:
    print("You Win")
elif Computer_choice > User_Choice:
    print("you loose")
elif Computer_choice ==User_Choice:    
    print("you draw")