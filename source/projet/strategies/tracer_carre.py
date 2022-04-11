from .avancer import *
from .tourner import *
import math

class TracerCarre:
    def __init__(self, robot, distance, vitesse):
        self.robot=robot
        self.distance=distance
        self.vitesse=vitesse
        self.strats=[Avancer(robot,vitesse,distance),Tourner(robot,vitesse,90),
        Avancer(robot,vitesse,distance),Tourner(robot,vitesse,270),Avancer(robot,vitesse,distance),
        Tourner(robot,vitesse,270),Avancer(robot,vitesse,distance),
        Tourner(robot,vitesse,90),Avancer(robot,vitesse,distance)]
        self.i=0
        self.stop_var=False 
        

    def start(self):
        self.strats[self.i].start()

    def step(self):
        print("Je suis dans la strategie dindice ",self.i)
        if( not self.strats[self.i].stop_var):
            self.strats[self.i].step()
        else :
            self.i+=1
            if(self.i<len(self.strats)):
                self.strats[self.i].start()
                self.strats[self.i].step()
            else :
                self.stop_var=True 
                self.stop()

    def stop(self):
        #La strategie TracerCarre s'arette deux deux cas :
        #Soit on l'arette en mettant sa variable stop_var a True et en apellant sa fonction stop() dans ce cas elle stop la strategie courrante d'indice i 
        #Soit la strategie s'acheve quand elle a executé toutes les fonctions contenues dans sa liste self.strats
        if(self.stop_var):
            if(self.i<len(self.strats)):
                self.strats[self.i].stop_var=True
                self.strats[self.i].stop()    
            return True 

        else :
            return self.stop_var