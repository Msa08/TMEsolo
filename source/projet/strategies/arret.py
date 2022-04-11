class Arret: 
    def __init__(self,robot):
      self.robot=robot
      self.running=True

    def start(self):
        print("ALERTEEEE OBSTACLE,Jarette le robot !!!!!!!!!!!!!!!!!!!!")
  
        self.robot.mode=1
        self.robot.set_vitesse(0,0)

    def stop(self):
      return self.running
  