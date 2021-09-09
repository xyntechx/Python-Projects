from pet import Pet
from utility import set_difficulty, get_stat_ints, get_stats, get_random_stat, play
from keyboard_settings import start_keyboard
import time


try:
    name = input("Name of pet: ")
    difficulty = int(input("Set the difficulty (1/2/3/4/5): "))
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

    start_keyboard(pet)
    start = time.time()

    while play(pet):
        end = time.time()
        if end - start == duration:
            stat = get_random_stat(stat_int_list)

            # TODO: Replace with match case once Python 3.10 rolls around
            if stat == 0:
                pet.set_hunger()
                print("Hunger:", pet.get_hunger())

            elif stat == 1:
                pet.set_thirst()
                print("Thirst:", pet.get_thirst())

            elif stat == 2:
                pet.set_energy()
                print("Energy:", pet.get_energy())

            elif stat == 3:
                pet.set_fitness()
                print("Fitness:", pet.get_fitness())

            elif stat == 4:
                pet.set_mental_health()
                print("Mental Health:", pet.get_mental_health())

            count += 1

            if count == 10:
                count = 0
                pet.grow_up()
                print(" - - - ")
                print(pet.get_name(), "grew up!")
                print("Age:", pet.get_age())
                print(" - - - ")

            start = time.time()

except KeyboardInterrupt:
    print("\nThank you for playing!")
