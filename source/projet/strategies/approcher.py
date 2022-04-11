from .avancer import *
from .tourner import *
import math

class Approcher:
    def __init__(self, robot,distance,vitesse):
        self.robot=robot
        self.vitesse=vitesse
        self.strats=Avancer(robot,vitesse,distance)

    def start(self):
        self.strats.start()

    def step(self):
        if( not self.stop()):
            self.strats.step()
            self.robot.set_vitesse(self.robot.get_vitesse()+10)
            print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVIIIIIIIIIIIIIIIIIIIIIIIIIIIIITTTTTTTTTEEEEEEEEEESSSSSSSSSSSSSE . ", self.robot.get_vitesse())
        else :
            self.robot.set_vitesse(0)

    def stop(self):
        return self.strats.stop()