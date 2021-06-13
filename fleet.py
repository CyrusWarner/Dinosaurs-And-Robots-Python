

class Fleet:
    def __init__(self, robot_one, robot_two, robot_three, robot_four):
        self.fourth_robot = robot_four
        self.third_robot = robot_three
        self.second_robot = robot_two
        self.first_robot = robot_one
        self.fleet_list.append(self.first_robot)
        self.fleet_list.append(self.second_robot)
        self.fleet_list.append(self.third_robot)
        self.fleet_list.append(self.fourth_robot)
        self.fleet_list = []

