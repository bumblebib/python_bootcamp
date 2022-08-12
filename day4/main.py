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

#Write your code below this line 👇

choice = [rock, paper, scissors]
name = ["Rock","Paper","Scissors"]

ask_player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if ask_player < 0 or ask_player >= 3:
  print("Invalid number you lost")
else:
  player1 = choice[ask_player]
  random_number = random.randint(0,len(choice)-1)
  player2 = choice[random_number]

  if player1 == rock and player2 == scissors:
    print(f"You chose {name[ask_player]}! {player1} \n And the computer chose {name[random_number]}! {player2} \n You won!")
  elif player2 == rock and player1 == scissors:
    print(f"You chose {name[ask_player]}! {player1} \n And the computer chose {name[random_number]}! {player2} \n You lost!")
  elif player1 == scissors and player2 == paper:
    print(f"You chose {name[ask_player]}! {player1} \n And the computer chose {name[random_number]}! {player2}\n You won!")
  elif player2 == scissors and player1 == paper:
    print(f"You chose {name[ask_player]}! {player1} \n And the computer chose {name[random_number]}! {player2} \n You lost!")
  elif player1 == paper and player2 == rock:
    print(f"You chose {name[ask_player]}! {player1} \n And the computer chose {name[random_number]}! {player2} \n You won!")
  elif player2 == paper and player1 == rock:
    print(f"You chose {name[ask_player]}! {player1} \n And the computer chose {name[random_number]}! {player2}\n You lost!")
  else:
    print(f"You chose {name[ask_player]}! {player1} \n And the computer chose {name[random_number]}! {player2} \n It's a draw")