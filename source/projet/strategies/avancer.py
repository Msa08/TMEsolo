import time
import math

class Avancer:
    def __init__(self,robot,vitesse,distance):
        """fais avancer le robot mis en parametre dune certaine distance a une certaine vitesse"""
        self.distance=distance
        self.parcouru=0
        self.robot=robot
        self.vitesse=vitesse
        self.time=0
        self.delta_time=0
        self.stop_var=False

    
    def start(self):
        """Va mettre la distance parcouru par le robot a zero"""
        self.time=time.time()
        self.robot.set_mode(1)
        self.robot.set_vitesse(self.vitesse,self.vitesse)
        print("La vitesse est :",self.vitesse)
    
    def step(self):
        """va verifier que lon a accompli la tache en fonction du retour de la fonction stop"""
        print("****************JE SUIS DANS AVANCER*************************")
        
        self.delta_time=time.time()-self.time
        #Je verifie ici pour avoir une meilleure precision de calculs

        if(self.parcouru>=self.distance):
            self.stop_var=True
            self.stop()
        
        self.parcouru+=abs(self.robot.get_distance_parcouru_RoueDroite(self.delta_time))
        print("Jai parcourru la distance :",self.parcouru)
        self.time=time.time()
      
    
    def stop(self):
        """Va tester si la distance parcouru est superieure ou egale a lobjectif"""
        #La strategie s'arette deux deux cas :
        #Soit on l'arette en mettant sa variable stop_var a True et en apellant sa fonction stop()
        #Soit la strategie s'acheve quand elle a efectué sa tache 
        if(self.stop_var):
            print("****************Fin de la strategie Avancer************************* Distance parcouru : ",self.parcouru)
            self.robot.set_vitesse(0,0)
            return True 

        else :
            return self.stop_var
        





