# Task 1: Code Correction 
# You are provided with a Python script that is supposed to 
# guide a user through an adventure game, but it has some errors. Identify and fix them.

# Task 2: Setting the Scene
# Based on your corrected code from Task 1, expand the game. 
# If the user chooses "cave", ask them if they want to "light a torch" 
# or "proceed in the dark", and provide outcomes for each decision.

# Prompt user to choose a place.
place = input("Choose a place: forest or cave? ")

# Fix = to ==
if place == "forest":
    action = input("Climb a tree or cross a river? ")
    # Fix = to ==
    if action == "climb a tree":
        print("You found a bird's nest!")
    # Fix else to elif
    elif action == "cross a river":
        print("You found a boat!")
    # If the user makes an invalid statement, pass
    else: pass
# Fix = to ==
elif place == "cave":
    # Another choice: torch or dark?
    action = input("Would you like to light a torch or proceed in the dark? ")
    # If user lights a choice, they find a hidden treasure
    if action == "light a torch":
        print("You found a hidden treasure!")
    # If user proceeds in the dark, they are eaten by a dragon
    elif action == "proceed in the dark":
        print("You were eaten by a dragon, whoops!")
    # If the user makes an invalid statement, pass
    else: pass
# If the user makes an invalid statement, pass
else: pass

