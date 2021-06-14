from herd import Herd
from fleet import Fleet


class Battlefield:
    def __init__(self):
        self.display_welcome = "Welcome to Robots vs Dinosaurs!"
        self.fleet = Fleet()
        self.robot_one_turn = self.fleet.fleet_list[0]
        self.robot_two_turn = self.fleet.fleet_list[1]
        self.robot_three_turn = self.fleet.fleet_list[2]
        self.robot_four_turn = self.fleet.fleet_list[3]

        self.herd = Herd()
        self.dino_one_turn = self.herd.herd_list[0]
        self.dino_two_turn = self.herd.herd_list[1]
        self.dino_three_turn = self.herd.herd_list[2]
        self.dino_four_turn = self.herd.herd_list[3]

        user_input = str(input("Would you like to begin the battle, if so type in start!"))
        if user_input.lower() == "start":
            self.robot_one_injury = self.robot_one_turn.health - self.dino_one_turn.attack_power
            self.dino_one_injury = self.dino_one_turn.health - self.robot_one_turn.weapon.attack_power
            print(f"{self.robot_one_turn.name} is now at {self.robot_one_injury} health points")
            print(f"{self.dino_one_turn.type} is now at {self.dino_one_injury} health points")
            print(f"Second battle!")
            self.robot_two_injury = self.robot_two_turn.health - self.dino_two_turn.attack_power
            self.dino_two_injury = self.dino_two_turn.health - self.robot_one_turn.weapon.attack_power
            print(f"{self.robot_two_turn.name} is now at {self.robot_two_injury} health points")
            print(f"{self.dino_two_turn.type} is now at {self.dino_two_injury} health points")




