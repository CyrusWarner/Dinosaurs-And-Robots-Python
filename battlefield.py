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
        user_input = input("Type in yes if you would like to begin the battle!\n")
        if user_input.lower() == "yes":
            self.robot_one_turn.health -= self.dino_one_turn.attack_power
            self.dino_one_turn.health -= self.robot_one_turn.weapon.attack_power
            print(f"{self.dino_one_turn.type} attacked {self.robot_one_turn.name}!")
            print(f"{self.robot_one_turn.name} is now at {self.robot_one_turn.health} health points!\n\n")
            print(f"{self.robot_one_turn.name} attacked {self.dino_one_turn.type}!")
            print(f"{self.dino_one_turn.type} is now at {self.dino_one_turn.health} health points!\n\n")
            if self.dino_one_turn.health != 0:
                return self.battle_one()
            elif self.dino_one_turn.health == 0:
                print(f"{self.dino_one_turn.type} has lost the battle!\n")
                self.battle_two()

    def battle_two(self):
        user_input = input("Type in yes to begin the next round for the second battle!\n")
        if user_input.lower() == "yes":
            self.robot_two_turn.health -= self.dino_two_turn.attack_power
            self.dino_two_turn.health -= self.robot_two_turn.weapon.attack_power
            print(f"{self.dino_two_turn.type} attacked {self.robot_two_turn.name}!")
            print(f"{self.robot_two_turn.name} is now at {self.robot_two_turn.health} health points!\n\n")
            print(f"{self.robot_two_turn.name} attacked {self.dino_two_turn.type}!")
            print(f"{self.dino_two_turn.type} is now at {self.dino_two_turn.health} health points!\n\n")
            if self.dino_two_turn.health != 0:
                return self.battle_two()
            elif self.dino_two_turn.health == 0:
                print(f"{self.dino_two_turn.type} has lost the second battle!\n")
