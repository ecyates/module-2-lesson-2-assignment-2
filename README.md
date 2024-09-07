# Module 2 - Lesson 2 - Python Conditional Statements
Author: Elizabeth Yates

In this repo, I'm doing the following assignment: 

1. Nested Decisions: The Adventure Game 🏰 (nested_decisions.py)

Objective: To practice the use of nested if statements.

Task 1: Code Correction 

You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. Identify and fix them.

Buggy Code:

place = input("Choose a place: forest or cave? ")

if place = "forest":
    action = input("climb a tree or cross a river?")
    if action = "climb a tree":
        print("You found a bird's nest!")
    else action = "cross a river":
        print("You found a boat!")
elif place = "cave":
    print("You find a hidden treasure!")

Task 2: Setting the Scene

Based on your corrected code from Task 1, expand the game. If the user chooses "cave", ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.

Task 3: Default Path

If the user makes an invalid choice at any point, incorporate a pass statement to handle it. HINT: How can an else statement be of use here?

2. Quick Decisions: The Event Planner 🎉 (quick_decisions.py)

Objective: To practice the use of shorthand if statements.

Task 1: Code Correction 

You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

Buggy Code:

attendees = input("Enter number of attendees: ")
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

Task 2: Venue Selection

Based on the corrected code from Task 1, further enhance your code to recommend additional things like "audio system" or "projector" based on the number of attendees.

Task 3: Catering Choices

Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".