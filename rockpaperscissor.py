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
def winner(x, y):
  if x == rock and y == "paper":
      print("You win")
  elif x == paper and y == "scissors":
      print("You win")
  elif x == scissors and y == "rock":
      print("You win")
  elif x == "rock" and y == paper:
      print("You lose")
  elif x == "paper" and y == scissors:
      print("You lose")
  elif x == "scissors" and y == rock:
      print("You lose")
  else:
      print("It's a draw")
  return

outcomes = [rock, paper, scissors]
t=True
while t:
  computer = random.choice(outcomes)
  
  user_choice = input("Choose rock, paper, or scissors: ").lower()
  print("Computer chose:\n" + computer)
  
  if user_choice == "rock":
      print("You chose:\n" + rock)
  elif user_choice == "paper":
      print("You chose:\n" + paper)
  elif user_choice == 'scissors':
      print("You chose:\n" + scissors)
  else:
      print("Choose the correct option")
  winner(computer, user_choice)
  v=input("Do you want to play again? (y/n)").lower()
  if v=='n' or v=='no':
    t=False
print("Thank you for playing")