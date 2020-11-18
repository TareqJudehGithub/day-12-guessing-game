from random import randint, choice
from art import logo

print(logo)

guess_me = choice(range(1, 101))
game_over = False
attempts = 0


correct_input = False
while correct_input == False:

  difficulty = input("Choose game difficulty: Easy(10 attempts) / Hard(5 attempts)\n").lower()
  if difficulty == "easy":
    attempts = 10
    correct_input = True
    
  elif difficulty == "hard":
    attempts = 5
    correct_input = True
    
  else:
    print("Bad input.")


while game_over == False:

  user_guess = input("Guess the Lucky Number: ")
  if user_guess == guess_me:
    print(f"Correct! you guessed {guess_me}! Which is the right number!")
  elif user_guess > guess_me:
    print("Your guess is higher than the Lucky Number")
print(attempts)
