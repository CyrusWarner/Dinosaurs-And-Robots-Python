from robot import Robot
from weapon import Weapon
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd

weapon_one = Weapon("sword")
weapon_two = Weapon("gun")

# assigning robots names and weapons
robot_one = Robot("Terminator", weapon_one)
robot_two = Robot("dez", weapon_one)
robot_three = Robot("Sadie", weapon_two)
robot_four = Robot("Cyrus", weapon_two)

# Putting variables into robot.py
robots = Fleet(robot_one, robot_two, robot_three, robot_four)

# assigning dinosaurs names, attack power, and energy
dino_one = Dinosaur("T-rex", 10, 100)
dino_two = Dinosaur("Velociraptor", 8, 75)
dino_three = Dinosaur("Triceratops", 6, 75)
dino_four = Dinosaur("Brontosaurus", 3, 50)

# assigning dinos to Herd
dinos = Herd(dino_one, dino_two, dino_three, dino_four)
