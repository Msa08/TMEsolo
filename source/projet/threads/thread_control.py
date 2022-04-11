import threading
import time
DELTATIMECONTROLE=0.01

class Thread_control (threading.Thread):
    """
      Notre Thread de control qui va permettre denvoyer des instruction (strategies)
      a nos robot reels et/ou simule.
    """
    def __init__(self,robot,strategie):      
        threading.Thread.__init__(self)  # ne pas oublier cette ligne
        # (appel au constructeur de la classe mère)   
        self.running=True
        self.robot=robot
        self.strategie=strategie


    def run(self):
        while (not self.strategie.stop() and self.running==True):
            print("Je suis laa ",self.strategie.stop())
            self.strategie.step()
          
            if (self.strategie.stop()):
              self.stop()
              
            time.sleep(DELTATIMECONTROLE)
          
            
        
    def stop(self):
      print("J'ai stop le  thread de control ici")
      self.running = False