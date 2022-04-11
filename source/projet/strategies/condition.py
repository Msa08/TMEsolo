class Condition :
    def __init__(self,strategie1,strategie2,detection):
        self.detection=detection
        self.i=0
        self.strat1=strategie1
        self.strat2=strategie2
        self.premier1=0
        self.premier2=0 
        
    def start(self):
        print("Debut de la strategie Condition")
        return 
        
    def step(self):
        if(not self.detection.step()):
            if(self.premier1==0):                       #pour faire le start quune seule fois
                self.strat1.start()
                self.premier1+=1
            if not self.strat1.stop_var :                 #on execute S1 sequentielle 
                self.strat1.step()
  
        else:
            print("*********JE DETECTE UN DOBSTACLE****************")    
            if(self.premier2==0):                       #pour faire le start quune seule fois
                self.strat2.start()
    
            if not self.strat2.stop() :                 #on execute S1 sequentielle 
                self.strat2.step()
            
            self.strat1.stop_var=True
            self.strat1.stop()

           

    def stop(self):
        print("Je suis dans le stop de la condition")
        return (self.strat1.stop_var)