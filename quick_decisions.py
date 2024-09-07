# Task 1: Code Correction 
# You are provided with a Python script that is supposed to help in event planning, 
# but it has errors. Identify and fix them.

# Task 2: Venue Selection
# Based on the corrected code from Task 1, further enhance your code to recommend additional 
# things like "audio system" or "projector" based on the number of attendees.

# Task 3: Catering Choices
# Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, 
# otherwise recommend "Gourmet Meals Caterers".

# Change input to be an integer
attendees = int(input("Enter number of attendees: "))
# For parties of over 100 people, the event will be held in a large hall, otherwise in a conference room
venue = "large hall" if attendees > 100 else "conference room"
# For parties of over 50 people, the sound system will have to have 300-500 watts, otherwise a portable PA
sound_system = "portable PA system with 50-100 watts" if attendees <= 50 else "powerful sound system with 300-500 watts"
# Prompt whether the user wants vegetarian.
vegetarian = input("Would you like vegetarian food? ")
# If the user does want vegetarian, hire the Veggie Delight Caterers, otherwise the Gourmet Meals Caterers
catering = "Veggie Delight Caterers" if vegetarian == "yes" else "Gourmet Meals Caterers"
print("The event will be held in a", venue, "with a", sound_system, "and", catering)
