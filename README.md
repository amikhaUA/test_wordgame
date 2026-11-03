# 🎮 Word Guessing Game

A simple multilingual word-guessing game built with Python. Players try to guess a secret word one letter at a time before running out of attempts.

## 🌍 Supported Languages

- 🇸🇪 Swedish (Svenska)
- 🇬🇧 English
- 🇺🇦 Ukrainian (Українська)

The game uses the **wordfreq** library to select random words from each language.

## ✨ Features

- Choose between three languages
- Randomly selected words
- Words between 7 and 12 letters
- 8 attempts to guess the word
- Display correctly guessed letters and remaining attempts
- Prevent duplicate guesses
- Validate player input
- Display a winning or losing message

## 🛠️ Requirements

- Python 3.8 or newer
- `wordfreq` library (listed in `requirements.txt`)

## 📦 Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-username/word-guessing-game.git
```

> Replace `your-username` with your actual GitHub username.

**2. Open the project folder**

```bash
cd word-guessing-game
```

**3. Install the required library**

```bash
python -m pip install -r requirements.txt
```

On macOS, you may need to use `python3` instead of `python`.

## 🚀 How to Play

Run the Python file:

```bash
wordgame test 1_1.py
```

**Step 1:** Choose your language.

1. Svenska
2. English
3. Українська

**Step 2:** The program randomly selects a secret word (not just nouns)

**Step 3:** Guess one letter at a time.

**Step 4:** Each incorrect guess reduces your remaining attempts by one.

**Step 5:** Guess the complete word before your attempts run out!

## 🎯 Example Gameplay

```text
Choose language:
1. Svenska
2. English
3. Українська (Ukrainian)
Your choice 1-3: 1

Word: _ _ _ _ _ _ _
Attempts left: 7
Guess a letter: e

Word: e _ e _ _ _ _
Attempts left: 6
Guess a letter: l

Word: e l e _ _ _ _
Attempts left: 5
Guess a letter: f

Word: e l e f _ _ _
Attempts left: 4
Guess a letter: a

Word: e l e f a _ _
Attempts left: 3
Guess a letter: n

Word: e l e f a n _
Attempts left: 2
Guess a letter: t

Congrats! You guessed the word 'elefant'!
```

*This is an illustrative example; the actual word is chosen randomly.*

## 🧠 How It Works

The program uses several Python concepts:

- **Lists:** Store available words and guessed letters.
- **Dictionaries:** Match language choices to language codes.
- **Loops:** Keep the game running until the player wins or loses.
- **Conditional statements:** Check whether guesses are correct.
- **List comprehensions:** Display correctly guessed letters.
- **Functions:** Organize and execute the game.
- **External libraries:** Retrieve words using `wordfreq`.

## 🔮 Future Improvements

1. Add difficulty levels (Easy, Medium, Hard)
2. Add a scoring system
3. Show translations after each round
4. Allow players to play multiple rounds
5. Save high scores
6. Add categories such as animals, food, and technology
7. Create a graphical user interface (GUI)

## 📚 Word Source

Words are retrieved using the open-source Python library [wordfreq](https://pypi.org/project/wordfreq/).
