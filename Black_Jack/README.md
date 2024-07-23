# Blackjack Game

This is a simple implementation of the Blackjack game in Python. The game allows a single player to play against a dealer. The player needs to log in or sign up to play with their balance.

## Features

- Login and sign-up functionality
- Bet placement
- Blackjack gameplay with hitting, standing, and ace adjustment logic
- Balance update after each game
- Dealer logic to follow Blackjack rules

## Installation

all required libraries are pre-installed in python
`random`
`csv`
`os`
`time`

## Usage

1. **Run the Blackjack game:**

   ```bash
   python blackjack_game.py
   ```

2. **Follow the prompts:**

   - Enter your username and PIN to log in or sign up if you are a new user.
   - Place your bet.
   - Play the game by choosing to hit or stand.
   - The game will update your balance based on the outcome.

## Game Rules

- The goal of Blackjack is to beat the dealer's hand without going over 21.
- Face cards are worth 10 points. Aces are worth 1 or 11 points, whichever makes a better hand.
- Each player starts with two cards, one of the dealer's cards is hidden until the end.
- To 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.
- If you go over 21, you bust, and the dealer wins regardless of the dealer's hand.
- If you are dealt 21 from the start (Ace & 10), you got a Blackjack.
- Dealer will hit until their cards total 17 or higher.

## Files

- `blackjack_game.py`: The main file to run the Blackjack game.
- `login.py`: Contains functions for user login, sign-up, and balance update.
- `players.csv`: Stores user data including username, pin, and balance.

## Example

```
Login username: zaki
Your pin: 1234
Welcome back, zaki
Your balance is: 2500

How many chips would you like to bet? (max 2500) 500

Dealer's Hand:
<card hidden>
 ♠ 10

Player's Hand:
 ♥ Ace
 ♦ 5

Would you like to Hit or Stand? Enter 'h' or 's': h

Player's Hand:
 ♥ Ace
 ♦ 5
 ♣ 2

Would you like to Hit or Stand? Enter 'h' or 's': s
Player stands. Dealer is playing.

Dealer's Hand:
 ♠ 10
 ♥ 8
Dealer's Hand = 18

Player's Hand:
 ♥ Ace
 ♦ 5
 ♣ 2
Player's Hand = 18

Dealer and Player tie! It's a push.

Player's total chips: 2500
Would you like to play another hand? Enter 'y' or 'n': n
Thanks for playing!
```

## Perspective

In the future, we plan to enhance the Blackjack game with the following features:

- **Split Action:** Allow players to split their hands when they are dealt two cards of the same rank.
- **Secure Login:** Implement more secure login using hashed passwords and a database.
- **Multiplayer Functionality:** Use sockets to enable multiple players to play at the same table in a LAN environment.
