from robot import Robot


class Fleet:
    def __init__(self):
        self.fleet_list = []
        self.create_fleet()

    def create_fleet(self):
        terminator = Robot("Terminator", 100)
        dez = Robot("dez", 70)
        sadie = Robot("Sadie", 80)
        self.fleet_list.append(terminator)
        self.fleet_list.append(dez)
        self.fleet_list.append(sadie)
