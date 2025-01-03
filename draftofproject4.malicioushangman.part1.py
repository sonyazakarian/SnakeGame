import random

# Project 4 Malicious Hangman Part 1

class Hangman:

    def load_dictionary(self, dictionary_file):
        word_dict = {}
        with open(dictionary_file, 'r') as file:
            for word in file:
                word = word.strip().lower()
                word_length = len(word)
                if word_length not in word_dict:
                    word_dict[word_length] = []
                word_dict[word_length].append(word)
        return word_dict


    def choose_answer(self, length):
        if length in self.dictionary:
            self.answer = random.choice(self.dictionary[length])
            self.display = ['_' for _ in range(len(self.answer))]
        else:
            print("No words of this length")


    def play_hangman(self, word_length, number_of_guesses):
        self.guesses_left 
        self.guessed_letters = set()

        while self.guesses_left > 0 and "_" in self.display:

            print("\nWord: ", " ".join(self.display_word))
            print("Guesses left: ", self.guesses_left)
            print("Guessed letters: ", ", ".join(self.guessed_letters))

            guess = input("Enter a letter: ")

            if guess in self.guessed_letters:
                print(f"You've already guessed the letter {guess}. Guess again.")

            else:
                self.guessed_letters.add(guess)
                if guess in self.answer:
                    print(f"Correct. {guess} is a letter in the final word.")
                    self.update_display_word(guess)
                else:
                    print(f"Incorrect. {guess} is not a letter in the final word.")
                    self.guesses_left -= 1


        if "_" not in self.display_word:
            print(f"Congratulations! You successfully guessed the word, which is {self.answer}.")
        else:
            print(f"Sorry, you're out of guesses! The word was {self.answer}.")


    def update_display_word(self, guess):
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.display_word[i] = guess



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
        answer not None

        game.play_hangman(word_length, number_of_guesses)

        if not game.play_again():
            break 
        
    print("Thanks for playing!")


