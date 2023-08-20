import random

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
from hangman_words import word_list
chosen_word = random.choice(word_list)
list_guess = []
lives = 6
for letters in chosen_word:
    list_guess += "_"

print(list_guess)

end_of_game = False

while not end_of_game:
    guess = input("guess the letter->").lower()
    if guess in list_guess:
        print(f"You have already guessed {guess}")
    for position in range(len(chosen_word)):
        if(chosen_word[position]==guess):
            list_guess[position] = guess
    if guess not in chosen_word:
        lives = lives-1
        print(f"You guessed {guess}, that's not in the word. You lose a life")
    print(f"You have {lives} lives left")
    if "_" not in list_guess:
        end_of_game = True
        print("Yay!! You won")
    print(stages[lives])
    print(list_guess)
    if(lives == 0):
        print("You lost all your life\n *******Game Over*******")
        end_of_game = True
        print(f"The word was{chosen_words}")


