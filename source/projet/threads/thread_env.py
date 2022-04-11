import threading 
import time 
DELTATIMEENV=0.01

class Thread_env(threading.Thread):
    def __init__(self,environnement):
        threading.Thread.__init__(self)
        self.environnement=environnement
        self.running=True

    def run(self):
      while self.running :
        self.environnement.update()
        time.sleep(DELTATIMEENV)
        
    def stop(self):
      self.running = False
    
    
