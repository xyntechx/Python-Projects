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

# Create Pet subclasses if need be :D
