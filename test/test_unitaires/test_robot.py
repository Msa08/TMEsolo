import unittest 
from source import *
import math 

class RobotTest(unittest.TestCase) :
  def setUp(self):
    self.robot=Robot(0,0,Vecteur(1,0),2)
    self.robot2=Robot(0,0,Vecteur(1,math.pi),2)

  def test_coordonnées(self):
    self.assertGreaterEqual(self.robot.x,0)
    self.assertGreaterEqual(self.robot.y,0)

  
  def test_avancer(self):
    self.robot.avancer()
    self.robot2.avancer()
    self.assertAlmostEqual(self.robot.x,1)
    self.assertAlmostEqual(self.robot.y,0)
    self.assertAlmostEqual(self.robot2.x,-1)
    self.assertAlmostEqual(self.robot2.y,0)

  def test_reculer(self):
    self.robot.reculer()
    self.robot2.reculer()
    self.assertAlmostEqual(self.robot.x,-1)
    self.assertAlmostEqual(self.robot.y,0)
    self.assertAlmostEqual(self.robot2.x,1)
    self.assertAlmostEqual(self.robot2.y,0)
