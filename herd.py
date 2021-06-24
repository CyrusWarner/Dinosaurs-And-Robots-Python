from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.herd_list = []
        self.create_herd()

    def create_herd(self):
        trex = Dinosaur("T-rex", 25, 100)
        velociraptor = Dinosaur("Velociraptor", 15, 75)
        triceratops = Dinosaur("Triceratops", 20, 75)
        self.herd_list.append(trex)
        self.herd_list.append(velociraptor)
        self.herd_list.append(triceratops)
