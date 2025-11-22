# **Echoes of Caelestia**

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Echoes of Caelestia is a text-based exploration game written in Python.
You play as Gua Xi, a once-legendary adventurer who awakens inside a deserted corporate detention facility 850 lightyears from Earth. The alarms are silent. The guards are gone. Something is very wrong.

Your goal is simple:

**Escape… uncover what happened… or die trying.**

## **Features**

* A typing-effect narrative system
* A lightweight movement and exploration engine
* Items, inventory, and room-based interaction
* Multiple endings depending on your actions
* An immersive sci-fi backstory

## **How to Play**

After launching the game, the introduction will type itself out.

At the end of the intro:

* Press SPACE → Begin the game
* Press Q → End immediately with the “Give Up” ending

Once inside the game, you can explore the facility using simple text commands.

### **Available Commands**

| Command	| Description |
| - | - |
| go [direction] | Move to another room |
| take [item] |	Pick up an item |
| drop [item]	| Drop an item |
| examine [item] | Inspect an item |
| i	| View your inventory |
| q	| Give up (ends the game) |

Directions depend on the room (e.g., north, east, west, south).

## **Rooms and Navigation**

The environment is made up of several accessible rooms, including:

* **Detention Cell** – Where your story begins
* **Hallway** – Patrolled by droids
* **Armoury** – Contains a usable blaster
* **Control Room** – Source of security alerts
* **Escape Pod** – Your only way off the planet

Some areas require special items to access.

## **File Descriptions**

### `main.py`

- Starts the game.
- Loads the rooms and items.
- Waits for the player to type commands.
- Calls other functions (like move, take, etc).

### `data.py`

- Stores all the **rooms** in a Python dictionary.
- Each room has:
  - A description (what it looks like)
  - Exits (where you can go)
  - Items (what you can pick up)

Example:

`"armoury": {
    "description": "Stacks of weapons. There’s a blaster on the shelf.",
    "exits": {"east": "hallway"},
    "items": ["blaster"]
}`

### `functions.py`

#### Contains helper functions:

* **show_location():** Tells you where you are and what you see.
* **get_command():** Asks you what you want to do.
* **move():** Lets you go in a direction (if it's allowed).
* **take_item():** Lets you pick something up.
* **check_end_game():** Checks if you reached an ending (like escape or getting caught).

## **Endings**

1. **FREEDOM:** Escape successfully using the escape pod with the keycard.
2. **GUNFIGHT IN THE HALLWAY:** Encounter a patrol droid while armed.
3. **GIVE UP:** Simply give up. Triggered by pressing q at any time.

## **Thanks for playing!**
Go out there and have fun with your journey!