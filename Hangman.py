import random
import hangman_res
import os

def hangman():
    life = 6
    user_inputs = []

    # Randomly choose a word from the word_list and assign it to a variable called chosen_word.
    # Create an empty list called display. For each letter in the chosen_word, add "_" to display.
    chosen_word = random.choice(hangman_res.word_list)
    display = []
    word_length = len(chosen_word)
    for position in range(word_length):
        display += "_"
    for letter in display:
        print(letter, end="  ")
    print()
    print()

    while life > 0:
        # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
        guess = input("Guess a letter : ").lower()
        while len(guess) != 1:
            print("Please enter a single letter only :")
            guess = input().lower()
        while guess.isalpha() == False:
            print("Please enter a letter only :")
            guess = input().lower()
        while guess in user_inputs and guess in chosen_word:
            guess = input("Oops! You have already guessed this letter. Enter a different lettter.\n").lower()
        while guess in user_inputs:
            guess = input("You tried this already! Enter a different letter.\n").lower()
        user_inputs += guess
        
        # Clearing the Screen
        os.system('cls')

        # Check if the letter user guessed (guess) is one of the letters in the chosen word. Loop through each position in the chosen_word. If the letter at that position matches the guess, reveal the letter at that position in display.
        # matches = word_length
        for position in range(word_length): 
            letter = chosen_word[position]
            if letter == guess:
                if letter != display[position]:
                    display[position] = letter
                    print()
            # else:
            #     matches -= 1
        # if matches == 0:
        for letter in display:
            print(letter, end="  ")
        print()
        print()
        if guess not in chosen_word:
            life -= 1
        print(hangman_res.stages[life])
        if guess not in chosen_word:
            print(f"Oops! The letter {guess} is not present in the word.\n")
        if "_" not in display:
            print("\nCongratulations! You guessed all letters in the word.")
            break
    if life == 0:
        print(f"\nPssst, the solution is {chosen_word}.\n\nGame Over! Better luck next time.")
        
# print(hangman_res.logo)
# Another way of using other modules :
from hangman_res import logo
print(logo)
print()
hangman()
    
print("\n\n1. Play again\n2. Exit\n")
valid = True
while valid:
    try:
        choice = int(input("Enter your choice (Type 1 or 2) :\n"))
        if choice == 1:
            os.system('cls')
            hangman()
        else: 
            print("Hope you had fun playing hangman!")
        valid = False
    except: 
        print("Please enter a valid choice!\n")