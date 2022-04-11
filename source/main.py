from projet import Adaptateur_reel
from projet import Robot, Environnement, Obstacle, Affichage2D
from projet import Avancer, Tourner, TracerCarre, TracerTriangle, Condition, Approcher, Arret, Detection, Sequentielle
from projet import Thread_env, Thread_control
import math



#Creation du robot et de l environnement

env=Environnement("EARTH",500)
robot=Robot(100,100,0,20,10,10,env)               # robot simule
env.ajouter_Robot(robot)                                                #Ajout du robot dans l environnement
env.ajout_obstacle_aleatoire(2)
env.ajout_gemme(3)

vitesse=50
distance=50

#Avancer 
condition1=Condition(Avancer(robot,vitesse,distance),Arret(robot),Detection(robot,100,6))

#Tourner 
condition3=Condition(Tourner(robot,vitesse,90),Arret(robot),Detection(robot,100,6))

#Tracer carre dans le robot simule
tracer_cc=TracerCarre(robot,distance,vitesse)
condition=Condition(tracer_cc,Arret(robot),Detection(robot,100,6))



# Tracer un triangle dans le robot simule
condition2=Condition(TracerTriangle(robot,distance,vitesse),Arret(robot),Detection(robot,100,3))

#THREADS 
th_env=Thread_env(env)
th_env.start()
th_control=Thread_control(robot,condition)                   #condition en parametre pour tracer_carre
#th_control=Thread_control(robot,condition1)                 #condition en parametre pour avancer
#th_control=Thread_control(robot,condition2)                 #condition en parametre pour tracer_triangle
#th_control=Thread_control(robot,condition3)                 #condition en parametre pour tourner
  
th_control.start()
Affichage2D(env)
th_control.stop()
th_env.stop()
