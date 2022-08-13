import random
import string
from words import words


def choose_word(words):
    word = random.choice(words)                       # The word which is to be guessed is choosen randomly 

# 'words' list contains some words containing '-' or space, to filter them out we are using below code. 
# Remove this section in case your 'words' list doesn't have this problem.
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()                               # To avoid error, we use capital letter only.

def play_hangman(n):
    word = choose_word(words)                         # The random word to be guessed
    word_letters = set(word)                          # Set of all the letter in that word
    used_letters = set()                              # This will be used to store used letters
    alphabets = set(string.ascii_uppercase)           # Set carrying all uppercase alphabets
    lives = n                                         # Number of wrong tries allowed before the player lose the game
    print(f"The word-to-be-guessed is of {len(word_letters)} length.")

    
    while len(word_letters) > 0 and lives > 0:
        print("\n---------------------------------")  # Making the cmd look good :)
        print(f"Lives left: {lives}     |     Used letters: ", ''.join(used_letters))

        # what current word is /or/ how much the player have guessed
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", ''.join(word_list))
        
        # Taking players guess
        input_letter = input("Take a guess: ").upper()

        # If the guess is right or its a new letter
        if input_letter in alphabets - used_letters:
            used_letters.add(input_letter)
            if input_letter in word_letters:
                word_letters.remove(input_letter)       # removing the guessed letter from main word 
                print("You got that right!")
            else:
                lives -= 1
                print("Wrong guess!")

        elif input_letter in used_letters:
            print("You have already used that letter, try again.")

        else:
            print("Invalid character, try again.")
    
    if lives == 0:
        print(f"You lost! The word was: {word}")
    else:
        print(f"You got the right word and won! As you guessed, the word is: {word}")

#----------------------MAIN---------------------------

print("\nWelcome to the game of Hangman brave Player!")
print("There are 3 modes to play from. \nEasy(8 lives) --- Normal(5 lives) --- Hell(3 lives)!")
mode = int(input("Type '1' to play EASY mode!\n" + 
"Type '2' to play NORMAL mode!\nType '3' to play HELL mode!\n"))

while mode < 1 or mode > 3:
    mode = int(input("Invalid input, please choose from given options!\n"))

if mode == 1:
        n = 8
        print("EASY mode is selected. All the best!\n")
elif mode == 2:
        n = 5
        print("NORMAL mode is selected. All the best!\n")
elif mode == 3:
        n = 3
        print("HELL mode is selected. All the best!\n")

play_hangman(n)



