from pynput import keyboard
from colours import GREEN, END


def on_press(key, pet) -> None:
    """On Press function for the keyboard listener."""
    try:
        # TODO: Replace with match case once Python 3.10 rolls around
        if key.char == "h":
            if pet.hunger < 10:
                pet.hunger += 1
            print(GREEN + "Hunger +1 (" + str(pet.hunger) + ")" + END)
        if key.char == "t":
            if pet.thirst < 10:
                pet.thirst += 1
            print(GREEN + "Thirst +1 (" + str(pet.thirst) + ")" + END)
        if key.char == "e":
            if pet.energy < 10:
                pet.energy += 1
            print(GREEN + "Energy +1 (" + str(pet.energy) + ")" + END)
        if key.char == "f":
            if pet.fitness < 10:
                pet.fitness += 1
            print(GREEN + "Fitness +1 (" + str(pet.fitness) + ")" + END)
        if key.char == "m":
            if pet.mental_health < 10:
                pet.mental_health += 1
            print(GREEN + "Mental Health +1 (" + str(pet.mental_health) + ")" + END)
    except AttributeError:
        if key != keyboard.Key.esc:
            print("Oops! You have pressed a special key")


def setup_keyboard(pet):
    """Set up keyboard listener.

    Argument(s):
    pet: Pet -- your pet
    """
    listener = keyboard.Listener(on_press=lambda event: on_press(event, pet))
    return listener


def control_keyboard(listener, start_or_stop: int = 1) -> None:
    """Control keyboard listener.

    Argument(s):
    listener: Listener -- keyboard listener
    start_or_stop: int -- to start (value 0) or stop (value 1) (default 1)
    """
    listener.stop() if start_or_stop else listener.start()
