import random 

class Hangman:

    def __init__(self):
        self.dictionary = {}

    def load_dictionary(self, dictionary_file):
        word_dict = {}
        with open(dictionary_file, 'r') as file:
            for word in file:
                word = word.strip().lower()
                word_length = len(word)
                if word_length not in word_dict:
                    word_dict[word_length] = []
                word_dict[word_length].append(word)
        self.dictionary = word_dict

    def choose_possible_words(self, length):
        if length in self.dictionary:
            self.possible_words = self.dictionary[length]
            self.display = ['_' for _ in range(length)]
            return True
        else:
            print("No words of this length in the dictionary.")
            return False

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
        return largest_partition[0]

    def play_hangman(self, word_length, number_of_guesses):
        if not self.choose_possible_words(word_length):
            return

        self.guesses_left = number_of_guesses
        self.guessed_letters = set()
        self.answer = None

        while self.guesses_left > 0 and "_" in self.display:
            print("\nWord: ", " ".join(self.display))
            print("Guesses left: ", self.guesses_left)
            print("Guessed letters: ", ", ".join(self.guessed_letters))

            guess = input("Enter a letter: ").lower()

            if guess in self.guessed_letters:
                print(f"You've already guessed the letter {guess}. Guess again.")
                continue
            
            self.guessed_letters.add(guess)

            # Partition words and update display
            self.partition_surviving_words(guess)
            self.update_display(guess)

            if "_" not in self.display:
                print("Congratulations! You guessed the word:", "".join(self.display))
                return
            self.guesses_left -= 1

        if "_" in self.display:
            print("Sorry, you've run out of guesses. The word was:", self.answer)

    def update_display(self, guessed_letter):
        for i, letter in enumerate(self.answer):
            if letter == guessed_letter:
                self.display[i] = guessed_letter

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
    game.load_dictionary('dictionary.txt')  # Make sure to load the dictionary first

    while True:
        word_length = int(input("How many letters long do you want the word to be? "))
        number_of_guesses = int(input("How many guesses do you want to have? "))

        game.play_hangman(word_length, number_of_guesses)

        if not game.play_again():
            break 

    print("Thanks for playing!")
