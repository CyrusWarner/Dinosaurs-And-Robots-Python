from robot import Robot


class Fleet:
    def __init__(self):
        self.fleet_list = []
        self.create_fleet()

    def create_fleet(self):
        terminator = Robot("Terminator")
        dez = Robot("dez")
        sadie = Robot("Sadie")
        self.fleet_list.append(terminator)
        self.fleet_list.append(dez)
        self.fleet_list.append(sadie)
