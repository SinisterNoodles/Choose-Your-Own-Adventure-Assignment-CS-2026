# Chiano Arcari
# Anurag Nagra
# Computer Sciences ICS3U
# March 31, 2026

from story import story
from story import title
import textwrap, time

print(f"\n{title}") # Print the title of the story at the start
scene = story["startScene"] # Set the starting scene to the first scene
while True: # Loop to keep the story running
    for lineOfText in scene["text"]:
        print(f"\n{textwrap.fill(lineOfText, 80)}") # Wrap the text to 80 characters per line for better readability
        time.sleep(1) # Delay for added effect
    if not scene["options"]:
        userInput = input("\nPlay again? (yes/no): ").strip().lower()
        if userInput in ["yes", "y"]: # Reset to the starting scene if user wants to replay
            scene = story["startScene"]
            print(f"\n{title}")
            continue
        else: # Exit the main loop and end the game
            break
    print("\nOptions: ")
    for option in scene["options"]:
        print(f"- {option.capitalize()}") # Capitalize the first letter of each option for readability
    while True:
        userInput = input("\nEnter your choice: ").strip().lower()
        if userInput in scene["options"]:
            scene = story[scene["options"][userInput]] # Move to the next scene based on user's choice
            break
        else: # Prompt again if the user enters an invalid option (not an available option)
            print("Invalid option. Please try again.")
