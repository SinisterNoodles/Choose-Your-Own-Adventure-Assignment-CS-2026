from story import story
from story import title
import textwrap, time

print(f"\n{title}")
scene = story["startScene"]
while True:
    for lineOfText in scene["text"]:
        print(f"\n{textwrap.fill(lineOfText, 80)}")
        time.sleep(1)
    if not scene["options"]:
        userInput = input("\nPlay again? (yes/no): ").strip().lower()
        if userInput in ["yes", "y"]:
            scene = story["startScene"]
            print(f"\n{title}")
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
