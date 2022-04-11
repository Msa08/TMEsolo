from .tourner import Tourner
from .detection_obstacle import Detection
from .tracer_triangle import TracerTriangle
from .tracer_carre import TracerCarre
import math

class MotifInf:
    def __init__(self,robot,distance,vitesse):
        self.robot=robot
        self.distance=distance
        self.vitesse=vitesse
        self.stop_var=False
        self.strats=[TracerTriangle(robot,distance,vitesse),TracerCarre(robot,distance,vitesse)]
        self.detection=Detection(robot,100,6)
        self.tourner=Tourner(robot,50,180)
        self.i=0
        self.a=25
    
    def start(self):
        self.strats[self.i].start()
    
    def step(self):
        if( not self.detection.step()):
            self.strats[self.i].step()
        else :
            self.i+=1
            if self.a==25:
                self.tourner.start()
                self.a=1
            elif self.a==1 and not self.tourner.stop():
                self.tourner.step()
            
            elif(self.i<len(self.strats)):
                self.strats[self.i].start()
                self.strats[self.i].step()
            else:
                self.stop_var=True 
                self.stop()
        
        
    