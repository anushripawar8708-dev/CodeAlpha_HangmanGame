import random
words = ["Happy", "Joyful", "Sunny", "Witty", "Calm"]
word = random.choice(words)
guessed_word = ["_"] * len(word)
incorrect_guesses = 0
max_guesses = 6
guessed_letters = []
print("===== WELCOME TO HANGMAN =====")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")
while incorrect_guesses < max_guesses and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Incorrect guesses:", incorrect_guesses, "/", max_guesses)
    print("Guessed letters:", guessed_letters)
    guess = input("Enter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        incorrect_guesses += 1
        print("Wrong guess!")
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The correct word was:", word)