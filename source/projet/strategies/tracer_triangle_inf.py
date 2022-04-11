from .tourner import Tourner
from .detection_obstacle import Detection
from .tracer_triangle import TracerTriangle
import math

class TriangleInf:
    def __init__(self,robot,distance,vitesse):
        self.robot=robot
        self.distance=distance
        self.vitesse=vitesse
        self.stop_var=False
        self.strats=TracerTriangle(robot,distance,vitesse)
        self.detection=Detection(robot,100,6)
        self.tourner=Tourner(robot,50,180)
        self.a=25
        
    def start(self):
        self.strats.start()
        self.a=0
        
    def step(self):
        if self.detection.step():
            self.strats.stop_var=True
            self.strats.i=8
            self.strats.stop()
            if self.a==0:
                self.tourner.start()
            self.a=1
            if self.a==1 and not self.tourner.stop():
                self.tourner.step()
            
        elif not self.detection and self.a==2 and not self.tourner.stop():
            self.tourner.step()
        
        elif not self.detection and self.tourner.stop():
                self.strats.i=0
                self.strats.stop_var=False
        elif self.a==0:
            self.strats.step()
        elif self.strats.i==8:
            self.strats.start()
        else:
            self.strats.start()
            
    def stop(self):
        return False
            
                
            
            
            
        
        