import random
import os

# Optional: Load words from a file for a larger word pool
def load_words(file_path='words.txt'):
    if not os.path.exists(file_path):
        # Fallback to a default word list if the file doesn't exist
        return [
            'python', 'hangman', 'challenge', 'programming', 'developer',
            'algorithm', 'function', 'variable', 'iteration', 'condition'
        ]
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

class Hangman:
    def __init__(self, word_list, max_attempts=6):
        self.word_list = word_list
        self.max_attempts = max_attempts
        self.reset_game()

    def reset_game(self):
        self.target_word = random.choice(self.word_list).lower()
        self.guessed_letters = set()
        self.correct_letters = set()
        self.incorrect_letters = set()
        self.remaining_attempts = self.max_attempts
        self.word_display = ['_' for _ in self.target_word]
        self.game_over = False
        self.win = False

    def display_game_state(self):
        print("\nCurrent Word: " + ' '.join(self.word_display))
        print(f"Remaining Attempts: {self.remaining_attempts}")
        print(f"Guessed Letters: {' '.join(sorted(self.guessed_letters))}")
        if self.incorrect_letters:
            print(f"Incorrect Letters: {' '.join(sorted(self.incorrect_letters))}")

    def guess_letter(self, letter):
        letter = letter.lower()
        if not letter.isalpha() or len(letter) != 1:
            print("Please enter a single alphabetical character.")
            return

        if letter in self.guessed_letters:
            print(f"You have already guessed the letter '{letter}'. Try a different one.")
            return

        self.guessed_letters.add(letter)

        if letter in self.target_word:
            self.correct_letters.add(letter)
            for idx, char in enumerate(self.target_word):
                if char == letter:
                    self.word_display[idx] = letter
            print(f"Good job! The letter '{letter}' is in the word.")
        else:
            self.incorrect_letters.add(letter)
            self.remaining_attempts -= 1
            print(f"Sorry, the letter '{letter}' is not in the word.")

        self.check_game_over()

    def check_game_over(self):
        if '_' not in self.word_display:
            self.game_over = True
            self.win = True
        elif self.remaining_attempts <= 0:
            self.game_over = True
            self.win = False

    def play(self):
        print("Welcome to Hangman Challenge!")
        while not self.game_over:
            self.display_game_state()
            guess = input("Enter a letter to guess: ").strip()
            self.guess_letter(guess)

        self.display_game_state()
        if self.win:
            print(f"Congratulations! You guessed the word '{self.target_word}' correctly!")
        else:
            print(f"Game Over! The word was '{self.target_word}'. Better luck next time!")

        self.ask_replay()

    def ask_replay(self):
        while True:
            choice = input("Do you want to play again? (Y/N): ").strip().lower()
            if choice == 'y':
                self.reset_game()
                self.play()
                break
            elif choice == 'n':
                print("Thank you for playing Hangman Challenge! Goodbye!")
                break
            else:
                print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

def main():
    word_list = load_words()
    game = Hangman(word_list)
    game.play()

if __name__ == "__main__":
    main()
