# Python Quiz Game (Multiple Choice)

## 📖 Short Description

**Python Quiz Game** is a command-line multiple-choice quiz application that tests the user's knowledge of Python programming. The program presents a set of quiz questions in random order, accepts the player's answers, checks each response, keeps track of the score, and displays the final result at the end.

---

## ✨ What It Does

The program allows users to:

* Answer multiple-choice Python programming questions.
* Randomize the order of questions each time the game is played.
* Receive immediate feedback on whether each answer is correct or incorrect.
* Keep track of the player's score throughout the quiz.
* Display the final score after all questions have been answered.
* Accept answers in either uppercase or lowercase letters.
* Validate answers by comparing the user's response with the correct answer.

---

## ▶️ How to Run It

### Prerequisites

* Python 3.x installed on your computer

### Steps

1. Open a terminal or command prompt.
2. Navigate to the folder containing the project.

```bash
cd path/to/your/project
```

3. Run the program.

```bash
python python_quiz.py
```

> Replace `python_quiz.py` with your actual Python filename if it is different.

4. Read each multiple-choice question.
5. Enter **A**, **B**, **C**, or **D** as your answer.
6. View your final score after answering all ten questions.

---

## 💻 Example

```text
Welcome to the Python Quiz!

Q1: Which keyword is used to define a function in Python?

A. func
B. def
C. function
D. define

Your answer (A/B/C/D): B

✅ Correct!

Q2: Which module is used to generate random numbers?

A. math
B. random
C. os
D. sys

Your answer (A/B/C/D): B

✅ Correct!

...

Quiz finished! Your final score is 9/10.
```

---

## 🐍 Python Concepts Used

This project demonstrates the following fundamental Python programming concepts:

* **Importing Modules** – Uses the built-in `random` module to shuffle the quiz questions.
* **Lists** – Stores all quiz questions in a list.
* **Dictionaries** – Represents each quiz question as a dictionary containing the question, answer choices, and correct answer.
* **Strings** – Stores questions, answer choices, and user responses.
* **Variables** – Keeps track of the quiz questions, user answers, and score.
* **Input and Output** – Uses `input()` to receive user answers and `print()` to display questions, feedback, and results.
* **For Loops** – Iterates through the list of quiz questions and answer choices.
* **`enumerate()` Function** – Automatically numbers each quiz question during the loop.
* **Conditional Statements (`if` and `else`)** – Determines whether the user's answer is correct and updates the score.
* **String Methods** – Uses `.upper()` to make user input case-insensitive.
* **Arithmetic Operators** – Uses the `+=` operator to increment the player's score.
* **Formatted Strings (f-Strings)** – Dynamically displays question numbers, answers, and scores.
* **Randomization** – Uses `random.shuffle()` to present the quiz questions in a different order every time the program runs.

---

## 🎯 Learning Objectives

After completing this project, you will be able to:

* Import and use Python modules.
* Create and manipulate lists and dictionaries.
* Build an interactive command-line application.
* Accept and process user input.
* Use loops to iterate through collections of data.
* Apply conditional statements to make decisions.
* Display dynamic information using formatted strings (f-strings).
* Randomize program behavior using the `random` module.
* Track values using variables and arithmetic operations.
* Develop a complete multiple-choice quiz application using fundamental Python programming concepts.

---

## 📄 License
This project is intended for educational purposes and may be modified and shared freely.
