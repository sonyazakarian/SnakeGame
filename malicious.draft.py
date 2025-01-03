

import random 

class Hangman:

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
    
    def choose_possible_words(self, length):
        if length in self.dictionary:
            self.possible_words = self.dictionary[length]
            self.display = ['_' for _ in range(length)]
        else:
            print("No words of this length")

    def take_guess(self):
        self.guesses_left = number_of_guesses
        self.guessed_letters = set() 

        while self.guesses_left > 0 and "_" in self.display:

            print("\nWord: ", " ".join(self.display))
            print("Guesses left: ", self.guesses_left)
            print("Guessed letters: ", ", ".join(self.guessed_letters))

            guess = input("Enter a letter: ").lower()

            if guess in self.guessed_letters:
                print(f"You've already guessed the letter {guess}. Guess again.")
            
            else:
                self.guessed_letters.add(guess)
                self.guesses_left -= 1

    def partition_surviving_words(self, guessed_letter):
        partitions = {}

        for word in self.possible_words:
            
            pattern = ''.join([letter if letter == guessed_letter else '_' for letter in word])

            if pattern not in partitions:
                partitions[pattern] = []
            partitions[pattern].append(word)

            largest_partition = max(partitions.values(), key=len)
            self.possible_words = largest_partition

            if len(largest_partition) == 1:
                self.answer = largest_partition[0]

            return partitions

            # this means:
            # if there is only 1 word in the partition, then you pick that one as the final word
            # so then self.answer = that word. hence the line self.answer = largest_partition[0]


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
                        


    


















def search_dictionary(self, guess):
    partitions = {}

    for word in self.current_word_list:  # Iterate over the current list of possible words
        pattern = self.get_pattern(word, guess)  # Get the pattern for the word with the guessed letter
        if pattern not in partitions:
            partitions[pattern] = []
        partitions[pattern].append(word)  # Add word to the partition with that pattern

    # Find the partition with the largest number of words
    max_partition = max(partitions.values(), key=len)

    # Update the current word list to be the largest partition
    self.current_word_list = max_partition

    # Update the display if the guess was in the largest partition's pattern
    self.update_display_word_from_partition(max_partition[0], guess)



def get_pattern(self, word, guess):
    pattern = ""
    for letter in word:
        if letter == guess:
            pattern += guess  # Add the guessed letter if it's in the word
        else:
            pattern += "_"  # Keep the underscore for letters not yet guessed
    return pattern

