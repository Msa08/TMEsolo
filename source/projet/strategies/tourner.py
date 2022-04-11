import time
import math


class Tourner:

    def __init__(self,robot,vitesse,angle):
        """
            Strategie qui va mettre le robot en mode 2 et va permettre au robot 
            d effectuer une rotation (que la vitesse soit positive ou negative 
            la seule roue qui tourne dans ce mode est la roue droite )
        """
        #Les angles sont en degre 
        self.robot=robot
        self.angle_actuel=0
        self.angle_a_faire=angle
        self.vitesse=vitesse
        self.delta_time=0
        self.time=0
        self.stop_var=False

    def start(self):
        """
            Inialise la vitesse dune roue a une certaine vitesse 
        """
        self.time=time.time()
        self.robot.set_mode(2)
        print("Cest la que j'ai fais le premier set vitesse de tourner")
        self.robot.set_vitesse(self.vitesse,0)
        
  


    def step(self):
        """
            Verifie que la tache a ete accomploe en fonction du retour
            de la fonction stop
        """
        
        print("***********Je suis dans tourner **************************")
        self.delta_time=time.time()-self.time
        rayon=self.robot.get_ecart_roues()
        self.angle_actuel+=abs(((self.robot.get_distance_parcouru_RoueDroite(self.delta_time))*360)/(rayon*2*math.pi))
        print("Angle actuel en degre(step de la strategie Tourner)", self.angle_actuel,"Delta time dans tourner ",self.delta_time)
      
        if(self.angle_actuel>=self.angle_a_faire):
            self.stop_var=True
            self.stop()
          
        self.time=time.time()
        
  

    def stop(self):
        """
            Retourne si la valeur booleenne True ou False en fonction 
            du test qui verifie so langle parcouru actuellement est
            superieur ou egal a langle cible
        """
        if(self.stop_var):
            #La strategie s arette deux deux cas :
            #Soit on l arette en mettant sa variable stop_var a True et en apellant sa fonction stop()
            #Soit la strategie s acheve quand elle a efectue sa tache 
            print("****************Fin de la strategie Tourner*************************")
            print("Cest la que j'ai fais le second set vitesse de tourner")
            self.robot.set_vitesse(0,0)
            self.robot.set_mode(1)
        
            return True 
            
        return self.stop_var