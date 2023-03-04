#!/usr/bin/env python3

import requests
import time
from random import randint

"""Show the game instructions when called"""
def showInstructions():
    """Show the game instructions when called"""
    print('''
    RPG Game    
    ========    
    Commands:      
        go [direction]      
        get [item]    
        ''')

def showStatus():
    print('---------------------------')
    print('You are in the ' + currentRoom + '.')
    print('Inventory:', inventory)
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'] + '.')
      roomItems() 
    print("---------------------------")
inventory = []

# sphinx API logic
APIURL = "https://catfact.ninja/fact"

def allKnowingSphinx():
    fact = requests.get(f"{APIURL}")
    fact = fact.json()
    print(fact['fact'])
    time.sleep(1)


riddle_questions = {
    "Who created Python?: ": 
        {
        "choices": "A. Jeff Bezos, B. Elon Musk, C. Bill Gates, D. Guido van Rossum",
        "answer" : "D"
        },
    "What year was the Python born?: ":
        {
        "choices": "A. 1988, B. 1991, C. 2002, D. 2010",
        "answer" : "B"
        },
    "What statement/function does Python uses to display messages onto the screen?:": {
        "choices": "A. console.log(), B. System.out.println(), C. print(), D. println()",
        "answer" : "C"
    }
    }

def riddles():

    correct_guesses = 0

    for index, (key, value) in enumerate(riddle_questions.items()):

        print(f"***********************************************************\n{key}")
        print(value.get("choices"))

        guess = input("Select an answer: (A, B, C, or D): ")
        guess = guess.upper()

        if guess == value.get("answer"):
            correct_guesses += 1
            print(f"You got it! So far you correctly guessed: {correct_guesses} correctly.")            
        else:
            correct_guesses -= 1
            print(f"WRONG! Deducting your score. So far you correctly guessed: {correct_guesses} correctly.")

    if correct_guesses >= 3:
        print(f"Good job, you guessed all 3 answers correctly. You have earned the {rooms[currentRoom]['item']}. You can choose to go North or South.")
        if 'star' not in inventory:
            inventory.append("star")
            del rooms[currentRoom]['item']

    else:
        print("*********** GAME OVER! *********** \nYou didn't answer all three questions correctly! Restart the program to start over!")
        quit()
    

def game():

    choices = ["rock", "paper", "scissors"]
    computer = choices[randint(0,2)]
    win_count=0

    while True:
        if win_count > 0:
            break
        player = input("Let's play a game with a computer! Please input Rock, Paper or Scissors. \n>>> ")
        player = player.lower()

        if player == computer:
            print("Tie!")
        elif player == "rock":
            if computer == "paper":
                print(f"You lose! {computer} covers {player}")
            else:
                print(f"You win! {player} smashes {computer}! You can move again now!")
                win_count+=1
        elif player == "paper":
            if computer == "scissors":
                print(f"You lose! {computer} cut {player}")
            else:
                print(f"You win! {player} covers {computer}! You can move again now!")
                win_count+=1
        elif player == "scissors":
            if computer == "rock":
                print(f"You lose! {computer} smashes {player}")
            else:
                print(f"You win! {player} cut {computer}")
                win_count+=1
        else:
            print("Something went wrong. Try check your spelling!")

        computer = choices[randint(0,2)]

def roomItems():
    if currentRoom == 'Hall':
        print(f"A {rooms[currentRoom]['item']} could be useful to move on.")
    if currentRoom == 'Dining Room':
        print(f"Grabbing this magic {rooms[currentRoom]['item']} may come in handy in the future. Use it wisely.")
    if currentRoom == 'Sphinx Room':
        print("Hello explorer! It is I— the All-knowing Sphinx!")
        print(f"If you grab the {rooms[currentRoom]['item']}, there's sure to be something that will CAT-ch your eye!")
    if currentRoom == 'Riddle Room' and 'star' not in inventory:
        time.sleep(1)
        print(f"Haha, you thought you could move around easily like that?\nYou must successfully solve 3 random questions to obatin the {rooms[currentRoom]['item']}\nand move north or south! Good luck!")
        riddles()

    
    

    


rooms = {

    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': 'key'
    },    
    'Sphinx Room': {
        'north': 'Kitchen',
        'item': 'encyclopedia'
    },
    'Kitchen': {
        'north': 'Hall',
        'south' : 'Sphinx Room',
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Riddle Room',
        'item': 'potion'
    },
    'Riddle Room': {
        'north': 'Dining Room',
        'item': 'star',
        'south': 'Garden'
    },
    'Garden': {
        'north': 'Riddle Room'
    }
}


currentRoom = 'Hall'

showInstructions()

while True:
    showStatus()
    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split(" ", 1)

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            if "key" not in inventory and (move[1] == "east" or move[1] == "south"):
                print("You need a key to unlock this room.")
            else:
                currentRoom = rooms[currentRoom][move[1]]             
        else:
            print("You can't go that way!")

    if move[0] == 'get' :
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory.append(move[1])
            print(f'You picked up a {move[1]}.')
            del rooms[currentRoom]['item']
            if currentRoom == 'Sphinx Room':
                time.sleep(1)
                allKnowingSphinx()
        else:
             print('You already have a ' + move[1] + '!')
       
    if currentRoom == 'Kitchen':
        game()   

    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
    elif currentRoom == 'Garden' and 'potion' not in inventory:
        print('You missed an essential item. Go back through the house to find it.')
        