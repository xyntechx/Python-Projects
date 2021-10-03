from random import randint, choice


def set_difficulty(level: int) -> tuple:
    """Return the number of stats in play and the stat drop duration.

    Argument(s):
    level: int -- level of difficulty (value 1, 2, 3, 4, or 5)

    Levels:
    Level 1: 3 stats, stats drop every 3 seconds
    Level 2: 4 stats, stats drop every 3 seconds
    Level 3: 4 stats, stats drop every 2 seconds
    Level 4: 5 stats, stats drop every 2 seconds
    Level 5: 5 stats, stats drop every 1 second
    """
    # TODO: Replace with match case once Python 3.10 rolls around
    if level == 1:
        stat_count = 3
        duration = 3

    elif level == 2:
        stat_count = 4
        duration = 3

    elif level == 3:
        stat_count = 4
        duration = 2

    elif level == 4:
        stat_count = 5
        duration = 2

    elif level == 5:
        stat_count = 5
        duration = 1

    return stat_count, duration


def get_stat_ints(stat_count: int) -> list:
    """Return a list of stat indices in play.

    Argument(s):
    stat_count: int -- number of stats in play
    """
    stat_int_list = []

    for _ in range(stat_count):
        stat_int = randint(0, 4) # choose a random stat

        while stat_int in stat_int_list: # prevent duplicate stats
            stat_int = randint(0, 4)

        stat_int_list.append(stat_int)

    return stat_int_list


def get_stats(stat_int_list: list) -> list:
    """Return a list of stats in play.

    Argument(s):
    stat_int_list: list -- list of stat indices
    """
    stat_list = []

    for stat in stat_int_list:
        # TODO: Replace with match case once Python 3.10 rolls around
        if stat == 0:
            stat_list.append("Hunger")
        elif stat == 1:
            stat_list.append("Thirst")
        elif stat == 2:
            stat_list.append("Energy")
        elif stat == 3:
            stat_list.append("Fitness")
        elif stat == 4:
            stat_list.append("Mental Health")

    return stat_list


def get_random_stat(stat_int_list: list) -> int:
    """Return a random stat index.

    Argument(s):
    stat_int_list: list -- list of stat indices
    """
    return choice(stat_int_list)


def compile_tries(tries: dict) -> str:
    """Return a compilation of all the tries in a session.
    
    Argument(s):
    tries: dict -- a dictionary of all the tries in a session
    """
    result = "\n"

    for index in tries:
        result += index + "\n"
        result += str(tries[index]) + "\n"

    return result.rstrip()


def play(pet) -> bool:
    """Return False if any of the stats is 0."""
    if (not pet.hunger) or (not pet.thirst) or (not pet.energy) or (not pet.fitness) or (not pet.mental_health):
        print("Oh no! Take better care of", pet.name, "next time!")
        print("Thank you for playing!")
        print(" - - - ")
        print(pet)
        print(" - - - ")
        return False
    return True
