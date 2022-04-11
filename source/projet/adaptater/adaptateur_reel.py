import math
class Adaptateur_reel:
    
    def __init__(self,robot):
        self.robot=robot
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT,0)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,0)
        self.l_pos,self.r_pos=self.robot.get_motor_position()
        self.mode=1
        self.vitesse_RoueDroite=self.vitesse
        self.vitesse_RoueGauche=self.vitesse
        self.premier=0

    
    def set_vitesse(self,vitesse_RoueDroite,vitesse_RoueGauche):
        """
            Fixe la vitesse des deux moteurs en nombre de deges par seconde
            vitesse: la vitesse cible a la vitesse on veut que le robot se deplace        
        """
        self.vitesse_RoueDroite=vitesse_RoueDroite
        self.vitesse_RoueGauche=vitesse_RoueGauche
        rayon=self.get_rayon()

        if self.mode ==1  :
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT,vitesse_RoueDroite)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,vitesse_RoueGauche)

        if self.mode ==2 :
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT,vitesse_RoueDroite)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,0)


    def set_mode(self,mode):
        """
            Va fixer le mode dans lequel vont se mettre les roues
            Mode: -Mode 1 ( les deux roues tournent dans le meme sens)
                  -Mode 2 ( Les deux roues ne tournent pas dans le meme sens)

        """
        self.mode=mode

    def get_rayon(self):
        """
            Renvoie le rayon de la roue en cm. 
        """
        return self.robot.WHEEL_DIAMETER/2

    def get_vitesse(self):
        """
            Renvoie la vitesse du robot ( en m/s ), qui depend de la vitesse des roues. 
        """
        return self.vitesse

    def get_distance(self) :
        """
            Retourne la distance ( en mm ) a laquelle se trouve le prochain obstacle. 
        """
        return self.robot.get_distance()

    def detection_obstacle(self,distance):
        """
            Detecte la presence dun obstacle a une certaine distance du robot.
            distance: distance a laquelle on veut tester la presence dobstacle
        """
        if self.get_distance()<= distance:
            return True
        return False
    
    def get_ecart_roues(self):
        return self.robot.WHEEL_BASE_WIDTH
    
    def get_distance_parcouru(self,nb):
        if self.premier==1 :
            self.l_pos,self.r_pos=self.robot.get_motor_position()
            if self.l_pos==0:
                result=self.r_pos
            else:
                result=self.l_pos
        else :
            result=0
            self.premier=1
        self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT,self.r_pos)
        self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT,self.l_pos)
        
        return (result*math.pi*self.robot.WHEEL_DIAMETER)/360  