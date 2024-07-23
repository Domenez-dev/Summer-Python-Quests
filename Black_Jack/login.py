import random
import csv

families = ['♠', '♥', '♣', '♦']
numbers = {
    'ace': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'jack': 10,
    'queen': 10,
    'king': 10    
}

def shuffle():
    global cards
    cards = []
    for i in families:
        for j in numbers:
            cards.append(tuple((j, i)))

actions = ['deal', 'hit', 'stand', 'split']

def generate_card():
    return {
        {random.choice(families)}: {random.choice(list(numbers.keys()))}
        }

player_hand = {}
dealer_hand = {}

shuffle()

def sign_up(username):
    print('please enter your pin: ')
    invalid_pin = True
    while invalid_pin:
        pin = input('pin: ')
        if len(pin) != 4:
            print('pin should be 4 digits length')
        else:
            try:
                int(pin)
                invalid_pin = False
            except:
                print('pin should be an integer of 4 digits')
    player = [username, pin, '2500']
    with open('players.csv', 'a', newline="") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(player)
    print(f'player {username} added succesfully')
    return print()

def login():
    for _ in range(3):
        username = input('Login username: ')
        user_found = False
        with open('players.csv', 'r', newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['username'] == username:
                    user_found = True
                    for _ in range(3):
                        pin = input('Your pin: ')
                        if pin == row['pin']:
                            print('Welcome back, ' + row['username'])
                            print('Your balance is: ' + row['balance'])
                            return row
                        else:
                            print('Wrong pin')
                            print("Try again")
                    print('3 incorrect attempts')
                    return False
            if not user_found:
                print('Username does not exist. Would you like to sign up or try again?')
                choice = input(f'Sign up [1] with {username} or try again [2]: ')
                if choice == '1':
                    sign_up(username)
                    break
                else:
                    continue

logged_user = login()
