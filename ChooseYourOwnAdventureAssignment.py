import json

with open("story.json") as file:
    story = json.load(file)

scene = story["start_scene"]
while True:
    print(f"\n{scene["text"]}")
    if not scene["options"]:
        userInput = input("\nPlay again? (yes/no): ").strip().lower()
        if userInput in ["yes", "y"]:
            scene = story["start_scene"]
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
