from story import story
from asciiArt import asciiArt
import textwrap, time

scene = story["startScene"]
while True:
    art = scene.get("art")
    if art is not None:
        print(f"\n{asciiArt[art]}")
    for lineOfText in scene["text"]:
        print(f"\n{textwrap.fill(lineOfText, 80)}")
        time.sleep(1)
    if not scene["options"]:
        userInput = input("\nPlay again? (yes/no): ").strip().lower()
        if userInput in ["yes", "y"]:
            scene = story["startScene"]
            continue
        else:
            break
    print("\nOptions: ")
    for option in scene["options"]:
        print(f"- {option.capitalize()}")
    while True:
        userInput = input("\nEnter your choice: ").strip().lower()
        if userInput in scene["options"]:
            scene = story[scene["options"][userInput]]
            break
        else:
            print("Invalid option. Please try again.")
