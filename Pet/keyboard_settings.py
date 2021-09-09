from pynput import keyboard


def on_press(key, pet) -> None:
    try:
        # TODO: Replace with match case once Python 3.10 rolls around
        if key.char == "h":
            pet.set_hunger(0)
            print("\nThank you for feeding me!")
        if key.char == "t":
            pet.set_thirst(0)
            print("\nThank you for giving me a drink!")
        if key.char == "e":
            pet.set_energy(0)
            print("\nThank you for letting me sleep!")
        if key.char == "f":
            pet.set_fitness(0)
            print("\nThank you for making me exercise!")
        if key.char == "m":
            pet.set_mental_health(0)
            print("\nThank you for playing with me!")
    except AttributeError:
        if key != keyboard.Key.esc:
            print("Oops! You have pressed a special key")


def start_keyboard(pet) -> None:
    """Start keyboard listener.

    Argument(s):
    pet: Pet -- your pet
    """
    listener = keyboard.Listener(on_press=lambda event: on_press(event, pet))
    listener.start()
