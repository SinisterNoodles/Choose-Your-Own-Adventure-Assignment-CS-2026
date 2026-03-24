import json

with open("story.json") as file:
    story = json.load(file)

scene = story["start_scene"]
while True:
    print(f"\n{scene["text"]}")
    if not scene["options"]:
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
