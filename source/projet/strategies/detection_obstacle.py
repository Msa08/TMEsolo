import time
class Detection:
    """
        Strategie detection dobstacle: Permet de detecter un obstacle a une distance limite
        fixee dans le init. Si on detecte un obstacle on declenche la strategie arret. 
    """

    def __init__(self,robot,limite,frequence):
        """
            robot : Robot sur lequel on veut appliquer la strategie. 
            limite : Distance limite a laquelle on teste la detetction. 
        """
        self.robot=robot
        self.limite=limite
        self.frequence=frequence
        self.indice=0
    
    def step(self):

        self.indice+=1
        print("indice detection ", self.indice)
        if (self.indice >=self.frequence) :
            distance_Obstacle_Robot=self.robot.get_distance()
            print("Le prochain obstacle est a : ",distance_Obstacle_Robot)
            self.indice=0
            return 0 <= distance_Obstacle_Robot <=self.limite

        else :
            return False 
