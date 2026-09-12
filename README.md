# 🎮 Hangman Game in Python

## 📌 Project Description

This project is a simple **text-based Hangman game** developed using Python. The player has to guess a randomly selected word one letter at a time.

The game is designed for beginners and uses basic Python concepts such as **lists, strings, random, while loops, and if-else statements**.

## 🎯 Features

* Contains 5 predefined words.
* Selects a word randomly.
* Player guesses one letter at a time.
* Maximum of 6 incorrect guesses are allowed.
* Shows the letters guessed by the player.
* Displays the progress of the word.
* Simple console-based input and output.
* No graphics, audio, files, or APIs are used.

## 🛠️ Technologies Used

* **Python**
* `random`
* Lists
* Strings
* `while` loop
* `if-else`
* Console input/output

## 📂 Project Structure

```text
CodeAlpha_Hangman
│
├── hangman.py
└── README.md
```

## ▶️ How to Run

### 1. Install Python

Make sure Python is installed on your computer.

Check it using:

```bash
python --version
```

### 2. Open the Project

Open the project folder in **VS Code**.

### 3. Run the Program

Open the VS Code terminal and enter:

```bash
python hangman.py
```

## 🎮 How to Play

1. Run the program.
2. The computer randomly selects one word from the list.
3. The word is displayed as blank spaces.
4. Enter one letter at a time.
5. If the letter is correct, it will be revealed.
6. If the letter is incorrect, one attempt is lost.
7. You have a maximum of **6 incorrect guesses**.
8. Guess the complete word to win!

## 📝 Example

```text
===== WELCOME TO HANGMAN =====
Guess the word one letter at a time!
You have 6 incorrect guesses.

Word: _ _ _ _ _ _
Incorrect guesses: 0 / 6
Guessed letters: []

Enter a letter: p

Correct guess!

Word: p _ _ _ _ _
Incorrect guesses: 0 / 6
Guessed letters: ['p']
```

## 📚 Learning Objectives

Through this project, I learned how to:

* Use Python lists.
* Generate random choices using `random.choice()`.
* Use `while` loops.
* Use conditional statements.
* Work with strings and characters.
* Take input from users.
* Build a simple interactive console application.

## 👩‍💻 Author

**Anushri Pawar**

## 📌 Project

**CodeAlpha Internship – Hangman Game**

## ⭐ Future Improvements

Possible future improvements include:

* Adding difficulty levels.
* Adding a scoring system.
* Adding more words.
* Adding hints.
* Adding a graphical interface.
