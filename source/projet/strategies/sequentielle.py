import time

class Sequentielle:
    """
        Classe sequentielle qui va permettre de realiser une
        strategie sequentielle, strategie composee dune succesion
        de strategie
    """
    def __init__(self):
        self.strats=[]
        self.i=0
        self.stop_var=False 

    def start(self):
        self.strats[self.i].start()

    def step(self):
        print("Je suis dans la sequentielle",self.strats[self.i])
        if( not self.strats[self.i].stop()):
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
        """
            Teste si la strategie que lon est entrain deffectuer 
            est la derniere de la liste de strategie
        """
        #La strategie Sequentielle s arette deux deux cas :
        #Soit on l arette en mettant sa variable stop_var a True et en apellant sa fonction stop() dans ce cas elle stop la strategie courrante d indice i 
        #Soit la strategie s acheve quand elle a execute toutes les fonctions contenues dans sa liste self.strats
        if(self.stop_var):
            if(self.i<len(self.strats)):
                self.strats[self.i].stop_var=True
                self.strats[self.i].stop()    
            return True
        else :
            return self.stop_var

