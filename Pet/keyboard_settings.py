from pynput import keyboard
from colours import GREEN, END


def on_press(key, pet) -> None:
    """On Press function for the keyboard listener."""
    try:
        # TODO: Replace with match case once Python 3.10 rolls around
        if key.char == "h":
            pet.set_hunger(0)
            print(GREEN + "Hunger +1 (" + str(pet.get_hunger()) + ")" + END)
        if key.char == "t":
            pet.set_thirst(0)
            print(GREEN + "Thirst +1 (" + str(pet.get_thirst()) + ")" + END)
        if key.char == "e":
            pet.set_energy(0)
            print(GREEN + "Energy +1 (" + str(pet.get_energy()) + ")" + END)
        if key.char == "f":
            pet.set_fitness(0)
            print(GREEN + "Fitness +1 (" + str(pet.get_fitness()) + ")" + END)
        if key.char == "m":
            pet.set_mental_health(0)
            print(GREEN + "Mental Health +1 (" + str(pet.get_mental_health()) + ")" + END)
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
