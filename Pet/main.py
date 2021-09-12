from pet import Pet
from utility import set_difficulty, get_stat_ints, get_stats, get_random_stat, compile_tries, play
from keyboard_settings import setup_keyboard, control_keyboard
from colours import RED, END
import time
import colorama


colorama.init()

tries = {}
try_count = 0

try:
    while True:
        name = input("Name of pet: ")
        difficulty = int(input("Set the difficulty [1/2/3/4/5]: "))
        print()

        pet = Pet(name)
        stat_count, duration = set_difficulty(difficulty)
        stat_int_list = get_stat_ints(stat_count)
        stat_list = get_stats(stat_int_list)
        count = 0

        print("Stats in play:\n" + "\n".join(stat_list) + "\n")

        print(3)
        time.sleep(1.0)
        print(2)
        time.sleep(1.0)
        print(1)
        time.sleep(1.0)
        print("Let's Start!\n")

        print(" - - - ")
        print("Name:", pet.get_name())
        print("Age: 0")
        print(" - - - ")

        listener = setup_keyboard(pet)
        control_keyboard(listener, 0) # start keyboard listener
        start = time.time()

        while play(pet):
            end = time.time()
            if end - start == duration:
                stat = get_random_stat(stat_int_list)

                # TODO: Replace with match case once Python 3.10 rolls around
                if stat == 0:
                    pet.set_hunger()
                    print(RED + "Hunger -1 (" + str(pet.get_hunger()) + ")" + END)

                elif stat == 1:
                    pet.set_thirst()
                    print(RED + "Thirst -1 (" + str(pet.get_thirst()) + ")" + END)

                elif stat == 2:
                    pet.set_energy()
                    print(RED + "Energy -1 (" + str(pet.get_energy()) + ")" + END)

                elif stat == 3:
                    pet.set_fitness()
                    print(RED + "Fitness -1 (" + str(pet.get_fitness()) + ")" + END)

                elif stat == 4:
                    pet.set_mental_health()
                    print(RED + "Mental Health -1 (" + str(pet.get_mental_health()) + ")" + END)

                count += 1

                if count == 10:
                    count = 0
                    pet.grow_up()
                    print(" - - - ")
                    print(pet.get_name(), "grew up!")
                    print("Age:", pet.get_age())
                    print(" - - - ")

                start = time.time()

        control_keyboard(listener) # stop keyboard listener

        tries["Try " + str(try_count)] = pet
        try_count += 1

        continue_game = input("Continue? [Y/N]: ").upper()[-1]

        if continue_game == "N":
            print(compile_tries(tries))
            break

except KeyboardInterrupt:
    try:
        control_keyboard(listener) # stop keyboard listener
    except NameError:
        pass

    if tries:
        print(compile_tries(tries))

    print("\nThank you for playing!")
