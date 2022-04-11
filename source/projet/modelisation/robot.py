import math
import numpy as np

#PORTE_DETECTION est la portée de la detection d'obstacle 
PORTE_DETECTION=10


class Robot:
    #Initialisation des attributs du Robot 
    def __init__(self, x, y,angle,longueur,rayon,ecart_roues,env):
        self.x = x
        self.y = y
        self.env=env

        #L angle est en radian 
        self.angle=angle
        self.longueur=longueur

        #Mode 1 : les roues tournent dans le meme sens et du coup si la vitesse est
        #positif il avance sinon il recule .
        #Mode 2 : les roues tournent dans un sens different si la vitesse est positif 
        #alors la roue droite tourne en avant et la roue gauche en arriere; il faut 
        #calculer le nouvel angle dinclinaison sinon inverse  

        #On initialise le mode a 1 lors de la creation du robot 
        self.mode=1

        #le rayon des roue est en mm
        self.rayon_Roue=rayon

        #ecart des roues en mm 
        self.ecart_roues=ecart_roues 

        #Vitesse des roues en degre par seconde 
        self.vitesse_RoueDroite=0
        self.vitesse_RoueGauche=0

      

    #Mise a jour de la position du robot 
    def update_Position(self,delta_time):
        """
            Mise a jour de la position du robot par le calcul de la distance 
            parcouru pendant un certain temps delta_time et modification de 
            l orientation de ce dernier. 
        """  
        if(self.mode==1) :
            if(self.vitesse_RoueDroite==self.vitesse_RoueGauche):
                distance=self.get_distance_parcouru_RoueDroite(delta_time)
                self.y = self.y + ( math.sin(self.angle) * distance )
                self.x = self.x + ( math.cos(self.angle) * distance )
            
    
        if(self.mode==2):
            #Les angles sont calcules en radian 
            distance=self.get_distance_parcouru_RoueDroite(delta_time)
            self.setAngle(self.angle+(distance/self.get_ecart_roues()))
            print("Langle du robot en radian (apres apres set dans update pos) est de :   ",self.angle, "Delta time update ",delta_time)

        

    #Les Setteurs
    def getEnv(self):
        """
            Retourne lenvironnement dans lequel evolue le robot
        """
        return self.env

      
    def setAngle(self, angle):
        """
            Oriente le robot avec langle entre en parametre
        """
        self.angle=angle

    def set_vitesse(self,vitesse_RoueDroite,vitesse_RoueGauche):
        """
            Fixe la vitesse du robot a la vitesse saisie en parametre
        """
        #La vitesse de rotation est en degre/s 
        self.vitesse_RoueDroite=vitesse_RoueDroite
        self.vitesse_RoueGauche=vitesse_RoueGauche

    def set_mode(self,mode):
        """
            Va mettre le mode du robot en mode 1 ou 2 en fonction du mode en parametre
        """
        self.mode=mode

    def set_rayon(self,rayon):
        """
            Modifie le rayon de la roue du robot
        """
        self.rayon_Roue=rayon

    #Renvoie la distance entre le robot et lobstacle le plus proche 
    def get_distance(self):
        """ 
            Renvoie la distance a laquelle se trouve le prochain obstacle en fonction du cas
            de deplacement du robot
        """
        #La distance retournee est en mm 
        env=self.env
        for i in np.arange(0, int(PORTE_DETECTION),5):
          for a in env.liste_Obstacles :
  
            #Premier cas : Deplacement de bas en haut 
            if (a.x1 <= self.x + math.cos(self.angle) * i <= a.x2 and int(self.y + math.sin(self.angle) * i) == a.y1):
                return i
                
            #Second cas : Deplacement de haut en bas        
            elif (a.x4 <= self.x + math.cos(self.angle) * i <= a.x3 and int(self.y + math.sin(self.angle) * i) == a.y3):
                return i

            #Troisieme cas : Deplacement de gauche a droite 
            elif (a.y1 <= self.y + math.sin(self.angle) * i <= a.y4 and int(self.x + math.cos(self.angle) * i)== a.x1):
                return i

            #Quatrieme cas : Deplacement de gauche a droite 
            elif (a.y2 <= self.y + math.sin(self.angle) * i <= a.y3 and int(self.x + math.cos(self.angle) * i)== a.x3):
                return i
        
        return -1

    def get_distance_parcouru_RoueDroite(self,delta_time):
        #La distance retournee est en mm
        return (self.get_vitesseRoueDroite()*delta_time*2*math.pi*self.get_rayon())/360
    
    def get_distance_parcouru_RoueGauche(self,delta_time):
        #La distance retournee est en mm
        return (self.get_vitesseRoueGauche()*delta_time*2*math.pi*self.get_rayon())/360


    def get_vitesseRoueDroite(self):
        """
            Retourne la vitesse actuelle de la roue droite
        """
        #la vitesse retournee est en mm/s
        return self.vitesse_RoueDroite
    
    def get_vitesseRoueGauche(self):
        """
            Retourne la vitesse actuelle de la roue gauche
        """
        #la vitesse retournee est en mm/s
        return self.vitesse_RoueGauche

    def get_rayon(self):
        """
            Retourne le rayon de la roue du robot
        """
        #Le rayon retournee est en mm
        return self.rayon_Roue

    def get_ecart_roues(self):
        #La valeur retournee est en mm
        return self.ecart_roues
    
    def set_offset(self):
        return