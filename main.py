#!/usr/bin/python3def showInstructions():
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
    print('You are in the ' + currentRoom)
    print('Inventory:', inventory)
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")
inventory = []



riddle_questions = {
    "Who created Python?: ": "D",
    "What year was the Python born?: ": "B",
    "What statement/function does Python uses to display messages onto the screen?: ": "C",
}

options = [["A. Jeff Bezos", "B. Elon Musk", "C. Bill Gates", "D. Guido van Rossum"],
           ["A. 1988", "B. 1991", "C. 2002", "D. 2010"],
           ["A. console.log()", "B. System.out.println()", "C. print()", "D. println()"]]


def riddles():

    correct_guesses = 0
    question_num = 1
    for key, value in riddle_questions.items():
        print("***********************************************************")
        print(key)

        for i in options[question_num-1]:
            print(i)
        guess = input("Select answers & type (A, B, C, or D): ")
        guess = guess.upper()

        if guess == value:
            correct_guesses += 1
            print(f"you got it! So far you correctly guessed: {correct_guesses}")            
        else:
            correct_guesses -= 1
            print(f"WRONG! Deducting your score. So far you correctly guessed: {correct_guesses}")
    
        question_num += 1
    if correct_guesses >= 3:
        print("Good job, you guessed all 3 answers correctly. You can get the item and go north or south now.")
    else:
        print(f"You got {correct_guesses} numbers of questions wrong! Let's try again")
        riddles()




rooms = {

    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': 'key'
    },

    'Kitchen': {
        'north': 'Hall',
        'item': 'monster',
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
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print('You can\'t go that way!')

    if move[0] == 'get' :
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory.append(move[1])
            print(move[1] + ' got!')
            del rooms[currentRoom]['item']
        else:
             print('Can\'t get ' + move[1] + '!')

    if currentRoom == 'Riddle Room':
        print("Haha, you thought you can move around easily like that? You must successfully solve 3 random questions to move north or south! Good luck!")
        riddles()

    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you ... GAME OVER!')
        break

    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break