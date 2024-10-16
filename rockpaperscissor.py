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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
game_images = [rock, paper, scissor]

print("Welcome to rock, papaer and scissors game")
user_choice = int(input("What do you chose? type 0 for Rock, 1 for Paper or 2 for scissor\n"))
if user_choice >= 3 or user_choice < 0:
 print("You have entered a invalid number")
else:
  print(game_images[user_choice])
  
  computer_choice = random.randint(0,2)
  
  print("computers choice:")
  print(game_images[computer_choice])
    
  if user_choice == 0 and computer_choice == 2:
    print("You Win")
  elif user_choice == 2 and computer_choice == 0:
      print("You loose")
  elif user_choice < computer_choice: 
      print("You loose")
  elif user_choice > computer_choice: 
    print("You win")                                                   
  elif user_choice == computer_choice: 
      print("Draw")
  else:
    print("You have entered a invalid number")
  

  


