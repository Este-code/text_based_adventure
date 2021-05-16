"""
A complete text game, 
the program will let users move through rooms based on user input 
and get descriptions of each room. 
"""
# 1 = forward, 2 = backward, 3 = left, 4 = right
option_movements = "\nMOVE LIST:\n\n [1] = forward\n [2] = backward\n [3] = left\n [4] = right\n\n Choice: " # creating the move list menu

# creating the game over flag
game_over = False

# will create an empty list which I'll use as a movments record
movements = []

# creating an array which will contain room descriptions
rooms = [
    "\nYou are outside.",
    "\nYou are in an empty room. In front of you there are three doors.\n",
    "\nYou are in a dark room where you cannot find the light switch.",
    "\nYou are in a corridor, at the end of it there is another door.",
    "\nYou are inside an office, it's messy but you can still move through. On the desk you can see files and a laptop.",
    "\nYou are in a bathroom, which has a broken window on the right side of the room."
]

# creating variable to save position
position = 0

# creating a list of in-game messages
messages = [
    "\nYou've fallen into a deep hole. You are now stuck.\n\nGAME OVER",
    "\nYou've fallen out the broken window and got stuck in a trap. \n\nGAME OVER",
    "\nERROR! You insert an invalid option. Try again.",
    "\nYou hit a wall!",
    ]
# first input choice
print("\nYou are standing outside a house, in front of you there is a door.\n")

# creating door choice flag
door_choice = False

while(not game_over):
    if(not door_choice):
        # updating move and list of movements
        move = int(input(option_movements))
        movements.append(move)

    if(position==0 and move in(2,3,4)):
        print("You are moving around the house.")
        print("You went back to the front door.")

    # error message situations
    if(move not in (1,2,3,4)):
        print(messages[2])
        print(rooms[position])
    
    # you hit a wall message situations
    if((position == 3 or position == 4) and (move == 3 or move == 4)):
        print(messages[3])
        print(rooms[position])
    elif(position == 5 and move == 3):
        print(messages[3])
        print(rooms[position])

    
    # game over situations
    if(position == 2 and move in (1,3,4)):
        print(messages[0])
        game_over = True
    elif(position== 5 and move == 4):
        print(messages[1])
        game_over = True

    if(position == 0 and move == 1):
        position = 1
        print(rooms[position])
    elif(position == 3 and move == 1): # end game situation
        position = 4
        print(rooms[position])
        print("\nYou completed the game!\n")
        game_over = True
    
    # door choice
    if(position == 1):
        door = int(input("[1] = left door\n[2] = middle door\n[3] = right door\n\nChoice:"))
        if(door == 1):
            position = 2
            print(rooms[position])
            door_choice = False
        elif(door == 2):
            position = 3
            print(rooms[position])
            door_choice = False
        elif(door == 3):
            position = 5
            print(rooms[position])
            door_choice = False
    elif(position == 0):
        print(rooms[position])   
   
    # from one room you can go back to the previous room
    if((position in (2,3,5)) and move == 2):
        position = 1
        print("\nYou went back!")
        print(rooms[position])
        move = 1
        door_choice = True
    elif(position in (1,4) and move == 2):
        position = position - 1
        print("\nYou went back!")
        print(rooms[position])



