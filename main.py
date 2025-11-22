# main.py

from data import rooms, starting_room
from functions import *
import time

def main():
    inventory = []
    current_room = starting_room

    title_screen()
    intro_result = read_intro_file()

    if intro_result == "quit":
        print(c("\nYou chose not to deal with the stress you'll face and go back to sleep.", "blue"))
        print(c("ENDING: GIVE UP", "bold"))
        return

    while True:
        clear()
        show_location(current_room, rooms)
        command = get_command()

        if command.startswith("go "):
            direction = command[3:]
            new_room = move(current_room, direction, rooms, inventory)

            if new_room is not None:
                current_room = new_room

        elif command.startswith("take "):
            take_item(current_room, command[5:], rooms, inventory)

        elif command.startswith("drop "):
            drop_item(current_room, command[5:], rooms, inventory)

        elif command.startswith("examine "):
            examine_item(command[8:], rooms, current_room)

        elif command == "i":
            print("\nInventory:", ", ".join(inventory) if inventory else "Empty.")

        elif command == "q":
            print(c("\nYou chose not to deal with the stress you'll face and go back to sleep.", "blue"))
            print(c("ENDING: GIVE UP", "bold"))
            break

        else:
            print(c("Invalid command. Please enter a valid command.", "red"))
            time.sleep(1.5)

        if check_end_game(current_room, inventory):
            break

main()