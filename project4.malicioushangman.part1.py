
"""
Sonya Zakarian
Project 4: Malicious Hangman, Part 1
October 20, 2024

"""

import random

class Hangman:

    def __init__(self):
        self.dictionary = self.load_dictionary('Dictionary.txt')
        self.answer = ""
        self.display = []
        self.guesses_left = 0
        self.guessed_letters = set()

    def load_dictionary(self, dictionary_file):
        word_dict = {}                            # Creates dictionary word_dict
        with open(dictionary_file, 'r') as file:  # Reads dictionary file 
            for word in file:
                word = word.strip().lower()
                word_length = len(word)
                if word_length not in word_dict:
                    word_dict[word_length] = []
                # Creates word_dict dictionary of all the words in Dictionary text file, indexed by number of letters
                word_dict[word_length].append(word)  
        return word_dict

    def choose_answer(self, length):
        if length in self.dictionary:
            # Randomly chooses a word from the Dictionary text file 
            self.answer = random.choice(self.dictionary[length])
            self.display = ['_' for _ in range(len(self.answer))]
        else:
            print("No words of this length")

    def play_hangman(self, word_length, number_of_guesses):
        self.guesses_left = number_of_guesses  
        # Creates set for guessed letters
        self.guessed_letters = set()  
        # Calls choose_answer method to secretly pick a word for the length inputted by the user 
        self.choose_answer(word_length) 

        while self.guesses_left > 0 and "_" in self.display:

            print("\nWord: ", " ".join(self.display))
            print("Guesses left: ", self.guesses_left)
            print("Guessed letters: ", ", ".join(self.guessed_letters))

            guess = input("Enter a letter: ").lower()

            if guess in self.guessed_letters:
                print(f"You've already guessed the letter {guess}. Guess again.")
            else:
                self.guessed_letters.add(guess)
                # Updates display if guessed letter is part of the word 
                if guess in self.answer:
                    print(f"Correct! {guess} is a letter in the word.")
                    self.update_display_word(guess)
                else:
                    print(f"Incorrect. {guess} is not in the word.")
                    self.guesses_left -= 1

        # Informs the player they've won if no more "_" left in word 

        if "_" not in self.display:
            print(f"Congratulations! You guessed the word: {self.answer}.")
        else:
            print(f"Sorry, you're out of guesses! The word was {self.answer}.")

    # Updates display word to show the accurately guessed letters 
    def update_display_word(self, guess):
        for i, letter in enumerate(self.answer):
            if letter == guess:
                self.display[i] = guess

    # Restarts game if player wants to play again 
    def play_again(self):
        while True:
            play_again = input("\nDo you want to play again? (y/n): ").lower()
            if play_again == 'y':
                return True
            elif play_again == 'n':
                return False
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    game = Hangman()

    while True:
        word_length = int(input("How many letters long do you want the word to be? "))
        number_of_guesses = int(input("How many guesses do you want to have? "))

        game.play_hangman(word_length, number_of_guesses)

        if not game.play_again():
            break 

    print("Thanks for playing!")
