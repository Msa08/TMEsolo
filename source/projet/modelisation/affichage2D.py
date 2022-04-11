from tkinter import *


class Affichage2D :
  """
    Cette classe va nous permettre d'afficher l'environnement et
    ses composants sur une interface graphique (Tkinter)
  """

  def __init__(self,environnement):
    self.environnement=environnement
    self.fenetre= Tk()
    self.fenetre.config(background="#F8F9F9")
    self.fenetre.geometry("720x480")
    self.fenetre.titre="Environnement"

    Bouton_Quitter = Button(self.fenetre, text ='Quitter', command = self.fenetre.destroy)
    Bouton_Quitter.pack()
    self.canvas= Canvas(self.fenetre,width = self.environnement.longueur, height=self.environnement.longueur, bg="white")
    self.canvas.pack()
    self.fenetre.after(0,self.update)
    self.fenetre.mainloop()



  def afficher_robot(self):
    """
      Creer la representation du/des robot(s), ses delimitations
      en fonction de sa position et sa couleur
    """
    for robot in self.environnement.liste_Robots :
      x0=robot.x-(robot.longueur)/2
      y0=robot.y-(robot.longueur)/2
      x1=robot.x+(robot.longueur)/2
      y1=robot.y+(robot.longueur)/2
      self.canvas.create_rectangle(x0,y0,x1,y1,fill="black")
      self.canvas.create_rectangle(x0,y0,x0+5,y0+5,fill="red")
      self.canvas.create_rectangle(x1-robot.longueur,y1,x1-5,y1-5,fill="blue")
      
  
  def afficher_obstacle(self):
    """
      Creer la representation du/des obstacles(s), ses delimitations
      en fonction de sa forme rectangulaire, position et sa couleur
    """
    for obstacle in self.environnement.liste_Obstacles:
     self.canvas.create_rectangle(obstacle.x2,obstacle.y2,obstacle.x4,obstacle.y4,fill='red')
  
  
  def update(self):
    """
      Met a jour les elements de laffichage 2D
    """
    self.canvas.delete("all")
    self.afficher_robot()
    self.afficher_obstacle()
    self.fenetre.after(1,self.update)