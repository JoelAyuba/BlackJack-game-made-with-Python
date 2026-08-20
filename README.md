# BlackJack-game-made-with-Python
Use of python calsses and functions to create a blackjack game

A classic, interactive command-line Blackjack game built with Python. This project uses an object-oriented approach to simulate a realistic deck of cards, player hands, and standard casino dealer rules.

---

## Features

* **Object-Oriented Design:** Clean implementation utilizing distinct `Card`, `Deck`, and `Hand` classes for modularity.
* **Smart Ace Handling:** Automatically adjusts the value of an Ace from 11 down to 1 to prevent a hand from busting.
* **Automated Dealer Logic:** The dealer follows standard casino rules, automatically drawing cards until their hand value reaches at least 17.
* **Input Validation:** Safely handles user input, reprompting the player if they enter anything other than the accepted commands.

## Prerequisites

This game runs on pure Python and relies exclusively on the built-in `random` module. You do not need to install any external libraries.

* Python 3.x installed on your machine.

## How to Run

1. Clone this repository or download the source code file to your local machine.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the script.
4. Execute the following command (assuming the file is named `blackjack.py`):
   ```bash
   python blackjack.py
