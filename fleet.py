

class Fleet:
    def __init__(self, robot_one, robot_two, robot_three, robot_four):
        self.fourth_robot = robot_four
        self.third_robot = robot_three
        self.second_robot = robot_two
        self.first_robot = robot_one
        self.list = []

    def generate_fleet_robots(self):
        self.list.append(self.first_robot)
        self.list.append(self.second_robot)
        self.list.append(self.third_robot)
        self.list.append(self.fourth_robot)
        print(self.list)
