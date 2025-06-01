
import random

# Step 1: List of words
word_list = ["apple", "banana", "grape", "mango", "peach"]

# Step 2: Randomly choose a word from the list
chosen_word = random.choice(word_list)

# Step 3: Create a display with underscores
display = ["_" for _ in chosen_word]

# Step 4: Set number of allowed wrong guesses
lives = 6

# Step 5: Store guessed letters
guessed_letters = []

# Step 6: Start the game loop
while lives > 0 and "_" in display:
    print("\nCurrent Word: ", " ".join(display))
    guess = input("Guess a letter: ").lower()

    # Check if letter is already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # If guessed letter is correct
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
        print("Correct guess!")
    else:
        lives -= 1
        print(f"Wrong guess! Lives remaining: {lives}")

# Step 7: Game result
if "_" not in display:
    print("\nCongratulations! You guessed the word:", chosen_word)
else:
    print("\nGame Over! The word was:", chosen_word)