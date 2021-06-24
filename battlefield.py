from herd import Herd
from fleet import Fleet
import sys


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.robot_one_turn = self.fleet.fleet_list[0]
        self.robot_two_turn = self.fleet.fleet_list[1]
        self.robot_three_turn = self.fleet.fleet_list[2]

        self.herd = Herd()
        self.dino_one_turn = self.herd.herd_list[0]
        self.dino_two_turn = self.herd.herd_list[1]
        self.dino_three_turn = self.herd.herd_list[2]
        self.robot_input = None
        self.dino_input = None

    def run_game(self):
        if len(self.herd.herd_list) == 3 and len(self.fleet.fleet_list) == 3:
            self.welcome()
        if len(self.fleet.fleet_list) > 0:
            self.display_robots()

        self.choose_robot()
        if len(self.herd.herd_list) > 0:
            self.display_dino()

        self.choose_dino()

        self.battle()

        self.dead()

        self.winner_of_battle()

        self.end_of_game()

    def welcome(self):
        print("Welcome to Robots vs Dinosaurs!\n")

    def display_robots(self):
        index = 0
        for each in self.fleet.fleet_list:
            print(f"{index} {each.name}   Power Level-{each.power_level}")
            index += 1

    def choose_robot(self):
        self.robot_input = int(input("\nPlease Choose a robot\n"))
        for each in self.fleet.fleet_list:
            if each == self.fleet.fleet_list[self.robot_input]:
                print(self.fleet.fleet_list[self.robot_input].name)
                return self.fleet.fleet_list[self.robot_input]

    def display_dino(self):
        index = 0
        for each in self.herd.herd_list:
            print(f"{index} {each.type}   Power Level-{each.attack_power}")
            index += 1

    def choose_dino(self):
        self.dino_input = int(input("\nPlease Choose a dinosaur\n"))
        for each in self.herd.herd_list:
            if each == self.herd.herd_list[self.dino_input]:
                print(self.herd.herd_list[self.dino_input].type)
                return self.herd.herd_list[self.dino_input]

    def battle(self):
        while len(self.herd.herd_list) and len(self.fleet.fleet_list):
            self.herd.herd_list[self.dino_input].health -= self.fleet.fleet_list[self.robot_input].weapon.attack_power
            self.fleet.fleet_list[self.robot_input].health -= self.herd.herd_list[self.dino_input].attack_power
            if self.fleet.fleet_list[self.robot_input].health > 0:
                print(f"\n{self.fleet.fleet_list[self.robot_input].name} attacked {self.herd.herd_list[self.dino_input].type}.")
            print(f"{self.herd.herd_list[self.dino_input].type} attacked {self.fleet.fleet_list[self.robot_input].name}.")
            if self.herd.herd_list[self.dino_input].health <= 0:
                print(f"{self.herd.herd_list[self.dino_input].type} has lost the battle.")
            else:
                print(f"{self.herd.herd_list[self.dino_input].type} health is now at {self.herd.herd_list[self.dino_input].health}.")
            if self.fleet.fleet_list[self.robot_input].health <= 0:
                print(f"{self.fleet.fleet_list[self.robot_input].name} has lost the battle.")
            else:
                print(f"{self.fleet.fleet_list[self.robot_input].name} health is now at {self.fleet.fleet_list[self.robot_input].health}.\n")
            if self.fleet.fleet_list[self.robot_input].health > 0 and self.herd.herd_list[self.dino_input].health > 0:
                self.battle()
            else:
                self.dead()

    def dead(self):
        while len(self.herd.herd_list) and len(self.fleet.fleet_list):
            if self.fleet.fleet_list[self.robot_input].health <= 0:
                del self.fleet.fleet_list[self.robot_input]
            if self.herd.herd_list[self.dino_input].health <= 0:
                del self.herd.herd_list[self.dino_input]
            if len(self.fleet.fleet_list) and len(self.herd.herd_list):
                self.run_game()

    def winner_of_battle(self):
        print("The winner has officially been decided!\n")
        if len(self.herd.herd_list) != 0:
            print("The dinosaurs have won the battle!")
        if len(self.fleet.fleet_list) != 0:
            print("The robots have won the battle!")

    def end_of_game(self):
        play_again = input("Would you like to play again? Type in yes or no.")
        if play_again.lower() == "yes":
            self.run_game()
        elif play_again.lower() == "no":
            sys.exit("\nThanks for playing Robots vs Dinosaurs!")
        else:
            self.end_of_game()
