# functions.py

import os
import sys
import time

# Optional color system (works on most terminals)
USE_COLOR = True

def c(text, color):
    if not USE_COLOR:
        return text
    codes = {
        "cyan": "\033[96m",
        "yellow": "\033[93m",
        "green": "\033[92m",
        "red": "\033[91m",
        "bold": "\033[1m",
        "end": "\033[0m",
    }
    return f"{codes.get(color,'')}{text}{codes['end']}"


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def title_screen():
    clear()
    print(c("==================================", "cyan"))
    print(c("        ECHOES OF CAELESTIA        ", "bold"))
    print(c("==================================", "cyan"))
    print()


def show_location(room_name, rooms):
    room = rooms[room_name]
    print(c(f"== {room_name.upper()} ==", "yellow"))
    type_text(f"\n{room['description']}", delay=0.01)

    if room["items"]:
        print(c("Items here:", "green"), ", ".join(room["items"]))

    print(c("Exits:", "cyan"), ", ".join(room["exits"].keys()))


def get_command():
    print("\nWhat do you do?")
    print("-----------------------------------")
    print(c("Commands:", "cyan"))
    print("\n  go <direction>  – move")
    print("  take <item>     – pick something up")
    print("  drop <item>     – drop an item")
    print("  examine <item>  – inspect something")
    print("  i               – check inventory")
    print("  q               – quit")
    print("-----------------------------------")
    
    return input("> ").lower().strip()


def move(current_room, direction, rooms, inventory):
    room_data = rooms[current_room]

    if direction not in room_data["exits"]:
        print(c("You can't go that way.", "red"))
        time.sleep(1.5)  # Let player SEE the message
        return None  # Signals to main() that move failed

    next_room = room_data["exits"][direction]

    if next_room == "escape_pod" and "keycard" not in inventory:
        print(c("The door is locked. A panel reads: 'Keycard Required'.", "red"))
        time.sleep(1.5)
        return None

    return next_room


def take_item(room_name, item, rooms, inventory):
    room = rooms[room_name]
    if item in room["items"]:
        inventory.append(item)
        room["items"].remove(item)
        print(c(f"You took the {item}.", "green"))
    else:
        print(c(f"There is no {item} here.", "red"))


def drop_item(room_name, item, rooms, inventory):
    if item not in inventory:
        print(c("You don’t have that item.", "red"))
        return
    inventory.remove(item)
    rooms[room_name]["items"].append(item)
    print(c(f"You dropped the {item}.", "yellow"))


def examine_item(item, rooms, current_room):
    descriptions = {
        "blaster": "A compact energy blaster. Standard security issue.",
        "keycard": "A corporate access keycard. Authorises high-level clearance.",
    }
    if item in rooms[current_room]["items"]:
        desc = descriptions.get(item, "Nothing special about it.")
        print(c(f"{item.capitalize()}: {desc}", "green"))
    else:
        print(c("You don't see that here.", "red"))


def check_end_game(current_room, inventory):
    if current_room == "escape_pod" and "keycard" in inventory:
        print(c("\nYou insert the keycard…", "yellow"))
        time.sleep(1)
        print(c("The pod launches. You escape the corporate planet and hibernates your way back to Earth.", "green"))
        print(c("ENDING: FREEDOM", "bold"))
        return True

    if current_room == "hallway" and "blaster" in inventory:
        print(c("\nA patrol droid spots you!", "red"))
        time.sleep(1)
        print(c("You fire the blaster and sprint for cover.", "yellow"))
        print(c("ENDING: GUNFIGHT IN THE HALLWAY", "bold"))
        return True

    return False


def read_intro_file():
    file_path = 'intro.md'

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            type_text(content, delay=0.015)

        while True:
            choice = input("\nPress ENTER to begin your journey, or press q to give up > ").lower().strip()
            if choice == "":
                return "start"
            elif choice == "q":
                return "quit"
            else:
                print(c("Press ENTER to begin or Q to give up.", "yellow"))

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        # Continue the game even if the intro file is missing.
        return "start"


def type_text(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()  # newline