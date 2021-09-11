from colours import PURPLE, END


class Pet:
    def __init__(self, name: str) -> None:
        self.name = name
        self.age = 0  # will increase over time
        self.hunger = 10  # the lower, the hungrier
        self.thirst = 10  # the lower, the thirstier
        self.energy = 10  # the lower, the more tired
        self.fitness = 10  # the lower, the less fit
        self.mental_health = 10  # the lower, the less healthy

    def __repr__(self) -> str:
        stats_list = [
            "Name: " + self.name,
            "Age: " + str(self.age),
            "Hunger: " + str(self.hunger),
            "Thirst: " + str(self.thirst),
            "Energy: " + str(self.energy),
            "Fitness: " + str(self.fitness),
            "Mental Health: " + str(self.mental_health)
        ]
        return PURPLE + "\n".join(stats_list) + END

    def get_name(self) -> str:
        """Return the name of your pet."""
        return self.name

    def change_name(self, new_name: str) -> None:
        """Change the name of your pet.

        Argument(s):
        new_name: str -- the new name of your pet
        """
        self.name = new_name

    def get_age(self) -> int:
        """Return the age of your pet."""
        return self.age

    def grow_up(self) -> None:
        """Increment your pet's age by 1."""
        self.age += 1

    def get_hunger(self) -> int:
        """Return the hunger of your pet."""
        return self.hunger

    def set_hunger(self, inc_or_dec: int = 1) -> None:
        """Set the hunger of your pet.

        Argument(s):
        inc_or_dec: int -- to increment (value 0) or decrement (value 1) (default 1)
        """
        if inc_or_dec:
            self.hunger -= 1
        else:
            if self.hunger < 10:
                self.hunger += 1

    def get_thirst(self) -> int:
        """Return the thirst of your pet."""
        return self.thirst

    def set_thirst(self, inc_or_dec: int = 1) -> None:
        """Set the thirst of your pet.

        Argument(s):
        inc_or_dec: int -- to increment (value 0) or decrement (value 1) (default 1)
        """
        if inc_or_dec:
            self.thirst -= 1
        else:
            if self.thirst < 10:
                self.thirst += 1

    def get_energy(self) -> int:
        """Return the energy of your pet."""
        return self.energy

    def set_energy(self, inc_or_dec: int = 1) -> None:
        """Set the energy of your pet.

        Argument(s):
        inc_or_dec: int -- to increment (value 0) or decrement (value 1) (default 1)
        """
        if inc_or_dec:
            self.energy -= 1
        else:
            if self.energy < 10:
                self.energy += 1

    def get_fitness(self) -> int:
        """Return the fitness of your pet."""
        return self.fitness

    def set_fitness(self, inc_or_dec: int = 1) -> None:
        """Set the fitness of your pet.

        Argument(s):
        inc_or_dec: int -- to increment (value 0) or decrement (value 1) (default 1)
        """
        if inc_or_dec:
            self.fitness -= 1
        else:
            if self.fitness < 10:
                self.fitness += 1

    def get_mental_health(self) -> int:
        """Return the mental health of your pet."""
        return self.mental_health

    def set_mental_health(self, inc_or_dec: int = 1) -> None:
        """Set the mental health of your pet.

        Argument(s):
        inc_or_dec: int -- to increment (value 0) or decrement (value 1) (default 1)
        """
        if inc_or_dec:
            self.mental_health -= 1
        else:
            if self.mental_health < 10:
                self.mental_health += 1


# Create Pet subclasses if need be :D
