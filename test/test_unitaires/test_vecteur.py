import unittest 
from source import *
import math 

class VecteurTest(unittest.TestCase) :
  def setUp(self):
    self.vecteur1=Vecteur(1,0)
    self.vecteur2=Vecteur(1,math.pi/3)

  def test_coordonnees_Cartesiennes(self):
    liste1=self.vecteur1.coordonnees_Cartesiennes()
    liste2=self.vecteur2.coordonnees_Cartesiennes()
    self.assertListEqual(liste1, [1,0])
    self.assertListEqual(liste2, [1/2,math.sqrt(3)/2])

  def test_changement_vitesse(self):
    self.vecteur1.changement_vitesse(3)
    self.assertAlmostEqual(self.vecteur1.vitesse,3)

  def test_addition_Vectorielle(self):
    temp=self.vecteur1.addition_Vectorielle(self.vecteur2)
    liste=temp.coordonnees_Cartesiennes()
    print(liste[0],liste[1])
    self.assertAlmostEqual(liste[0],3.5)
    self.assertAlmostEqual(liste[1],0.8660254037844372)

  def test_produit_scalaire(self):
    produit=self.vecteur1.produit_scalaire(self.vecteur2)
    print(produit)
    self.assertAlmostEqual(produit,1/2)

