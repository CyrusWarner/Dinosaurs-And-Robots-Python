

class Fleet:
    def __init__(self, robot_one, robot_two, robot_three, robot_four):
        self.fourth_robot = robot_four
        self.third_robot = robot_three
        self.second_robot = robot_two
        self.first_robot = robot_one
        self.fleet_list = []
        self.create_fleet()

    def create_fleet(self, robot_one, robot_two, robot_three, robot_four):
        self.fleet_list.append(robot_one)
        self.fleet_list.append(robot_two)
        self.fleet_list.append(robot_three)
        self.fleet_list.append(robot_four)
