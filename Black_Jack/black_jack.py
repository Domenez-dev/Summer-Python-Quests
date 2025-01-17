import random
from login import login, sign_up, update_balance, clear_screen

# Login in to play with your balance
logged_user = login()

# Define the suits and ranks
suits = ['♥', '♦', '♣', '♠']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': 11
    }

# Define the card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.suit} {self.rank}'

# Define the deck class
class Deck:
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

# Define the hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# Define functions for the game
def take_bet(balance):
    while True:
        try:
            bet = int(input(f'How many chips would you like to bet? (max {balance}) '))
            if bet <= 0:
                print('Bet must be greater than 0.')
            elif bet > balance:
                print(f'Sorry, your bet cannot exceed your balance. {balance}')
            else:
                return bet
        except ValueError:
            print('Please enter a valid number.')

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's': ")
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print("Sorry, please try again.")
            continue
        clear_screen()
        break

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print("<card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

# Game logic
playing = False
while True:
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    if not playing:
        chips = int(logged_user['balance'])
    bet = take_bet(chips)

    show_some(player_hand, dealer_hand)

    playing = True
    while playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)
        if player_hand.value > 21:
            print("Player busts!")
            chips -= bet
            break

    if player_hand.value <= 21:
        while dealer_hand.value < 21 and dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)
        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            print("Dealer busts!")
            chips += bet

        elif dealer_hand.value > player_hand.value:
            print("Dealer wins!")
            chips -= bet

        elif dealer_hand.value < player_hand.value:
            print("Player wins!")
            chips += bet

        else:
            print("Dealer and Player tie! It's a push.")

    print(f"\nPlayer's total chips: {chips}")
    update_balance(logged_user['username'], chips)
    new_game = input("\nWould you like to play another hand? Enter 'y' or 'n': ")
    clear_screen()

    if new_game[0].lower() == 'n':
        print("Thanks for playing!")
        break
    elif new_game[0].lower() == 'y':
        playing = True
        continue
