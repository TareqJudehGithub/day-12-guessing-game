from random import randint
from art import main_logo, game_over_logo, you_win
from replit import clear




def play_again(): 
  restart_game = True
  while restart_game:
    if input("Play again? (y/n): ").lower() == "y":
      clear()
      guess_number()
    else:
      restart_game = False
      print("Good Bye!")
      return

 

def guess_number():

  print(main_logo)

  attempts = 0
  guess_me = randint(1, 100)

  correct_input = False
  game_over = False

  while correct_input == False:
    difficulty = input("Choose game difficulty: Easy(10 attempts) / Hard(5 attempts):\n").lower()
    if difficulty == "easy":
      attempts = 10
      correct_input = True
      
    elif difficulty == "hard":
      attempts = 5
      correct_input = True
      
    else:
      print("Bad input.")
      print("")

  print("")


  while game_over == False:

    if attempts == 0:
      clear()
      print(game_over_logo)
      print(f"The Lucky Number is {guess_me}")
      print('''
      ''') 
      game_over = True
      return

     
      
    print(f"Attemps left: {attempts}")
    user_guess = int(input("Guess the Lucky Number: "))
    print("") 
    
    if user_guess == guess_me:
      clear()
      print(you_win)
      print(f"The Lucky Number is {guess_me}")
      print('''
      ''')  
      game_over = True
      return

    elif user_guess > guess_me:
      print('''Your guess is HIGHER than the Lucky Number.
      ''')
      attempts -= 1
    else:
      print('''Your guess is LOWER than the Lucky Number.
      ''')
      attempts -= 1
    
   
guess_number()


play_again()