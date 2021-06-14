from weapon import Weapon


class Robot:
    def __init__(self, name, power):
        self.name = name
        self.power_level = power
        self.health = 100
        self.weapon = Weapon()
