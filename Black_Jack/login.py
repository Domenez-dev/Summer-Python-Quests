import random
import csv
import os
from time import sleep

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Unix-like systems (Linux, macOS)
    else:
        os.system('clear')

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
    clear_screen
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

def update_balance(username, new_balance):
    updated = False
    rows = []
    with open('players.csv', 'r', newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['username'] == username:
                row['balance'] = new_balance
                updated = True
            rows.append(row)

    if updated:
        with open('players.csv', 'w', newline="") as csvfile:
            fieldnames = ['username', 'pin', 'balance']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
