from herd import Herd
from fleet import Fleet


class Battlefield:
    def __init__(self):
        self.display_welcome = "Welcome to Robots vs Dinosaurs!\n"
        print(self.display_welcome)
        self.fleet = Fleet()
        self.robot_one_turn = self.fleet.fleet_list[0]
        self.robot_two_turn = self.fleet.fleet_list[1]
        self.robot_three_turn = self.fleet.fleet_list[2]

        self.herd = Herd()
        self.dino_one_turn = self.herd.herd_list[0]
        self.dino_two_turn = self.herd.herd_list[1]
        self.dino_three_turn = self.herd.herd_list[2]
        self.battle_one()

    def battle_one(self):
        user_input = input("Type in yes if you would like to begin the battle!\n\n")
        if user_input.lower() == "yes":
            self.robot_one_turn.health -= self.dino_one_turn.attack_power
            self.dino_one_turn.health -= self.robot_one_turn.weapon.attack_power
            self.robot_one_turn.power_level -= 10
            self.dino_one_turn.energy -= 10
            print(f"{self.dino_one_turn.type} attacked {self.robot_one_turn.name}!")
            print(f"{self.robot_one_turn.name} is now at {self.robot_one_turn.health} health points!")
            if self.robot_one_turn.health != 0:
                print(f"{self.robot_one_turn.name}s energy is now at {self.robot_one_turn.power_level}\n\n")
            print(f"{self.robot_one_turn.name} attacked {self.dino_one_turn.type}!")
            print(f"{self.dino_one_turn.type} is now at {self.dino_one_turn.health} health points!")
            if self.dino_one_turn.health != 0:
                print(f"{self.dino_one_turn.type}s energy is now at {self.dino_one_turn.energy}.\n\n")
            if self.dino_one_turn.health != 0:
                return self.battle_one()
            elif self.dino_one_turn.health == 0:
                print(f"{self.dino_one_turn.type} has lost the battle!\n")
                self.battle_two()

    def battle_two(self):
        user_input = input("Type in yes to begin the next round for the second battle!\n\n")
        if user_input.lower() == "yes":
            self.robot_two_turn.health -= self.dino_two_turn.attack_power
            self.dino_two_turn.health -= self.robot_two_turn.weapon.attack_power
            self.robot_two_turn.power_level -= 10
            self.dino_two_turn.energy -= 10
            print(f"{self.dino_two_turn.type} attacked {self.robot_two_turn.name}!")
            print(f"{self.robot_two_turn.name} is now at {self.robot_two_turn.health} health points!")
            if self.robot_two_turn.health != 0:
                print(f"{self.robot_two_turn.name}s energy is now at {self.robot_two_turn.power_level}\n\n")
            print(f"{self.robot_two_turn.name} attacked {self.dino_two_turn.type}!")
            print(f"{self.dino_two_turn.type} is now at {self.dino_two_turn.health} health points!")
            if self.dino_two_turn.health != 0:
                print(f"{self.dino_two_turn.type}s energy is now at {self.dino_two_turn.energy}.\n\n")
            if self.dino_two_turn.health != 0:
                return self.battle_two()
            elif self.dino_two_turn.health == 0:
                print(f"{self.dino_two_turn.type} has lost the second battle!\n")
                self.battle_three()

    def battle_three(self):
        user_input = input("Type in yes to begin the next round for the final battle!\n\n")
        if user_input.lower() == "yes":
            self.robot_three_turn.health -= self.dino_three_turn.attack_power
            self.dino_three_turn.health -= self.robot_three_turn.weapon.attack_power
            self.robot_three_turn.power_level -= 10
            self.dino_three_turn.energy -= 10
            print(f"{self.dino_three_turn.type} attacked {self.robot_three_turn.name}!")
            print(f"{self.robot_three_turn.name} is now at {self.robot_three_turn.health} health points!")
            if self.robot_three_turn.health != 0:
                print(f"{self.robot_three_turn.name}s energy is now at {self.robot_three_turn.power_level}\n\n")
            print(f"{self.robot_three_turn.name} attacked {self.dino_three_turn.type}!")
            print(f"{self.dino_three_turn.type} is now at {self.dino_three_turn.health} health points!")
            if self.dino_three_turn.health != 0:
                print(f"{self.dino_three_turn.type}s energy is now at {self.dino_three_turn.energy}.\n\n")
            if self.dino_three_turn.health != 0:
                return self.battle_three()
            elif self.dino_three_turn.health == 0:
                print(f"{self.dino_three_turn.type} has lost the final battle!\n\n\n")
                self.winner_of_battle()

    def winner_of_battle(self):
        print("The winner has officially been decided!\n")
        if self.robot_three_turn.health == 0 & self.robot_two_turn.health == 0 & self.robot_one_turn.health == 0:
            print("The dinosaurs have won the battle!")
        elif self.dino_one_turn.health == 0 & self.dino_two_turn.health == 0 & self.dino_three_turn.health == 0:
            print("The robots have won the battle!")
