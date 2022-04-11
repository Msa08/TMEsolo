from projet import Adaptateur_reel
from projet import Avancer, Tourner, TracerCarre, TracerTriangle, Condition, Approcher, Arret, Detection, Sequentielle
from projet import Thread_env, Thread_control
import math
from robot2I013 import Robot2I013

r=Robot2I013() # robot reel
robot=Adaptateur_reel(r) # adaptator_robot reel

#Tracer carre
vitesse=100
distance=200

sequentielle=Sequentielle()
#sequentielle.strats.append(Avancer(robot,vitesse,distance))
sequentielle.strats.append(Tourner(robot,vitesse,math.pi/2))
#sequentielle.strats.append(Avancer(robot,vitesse,distance))
#sequentielle.strats.append(Tourner(robot,vitesse,math.pi/2))
#sequentielle.strats.append(Avancer(robot,vitesse,distance))
#sequentielle.strats.append(Tourner(robot,vitesse,math.pi/2))
#sequentielle.strats.append(Avancer(robot,vitesse,distance))
sequentielle.start()




tracer_cc=TracerCarre(robot,distance,vitesse)
condition=Condition(tracer_cc,Arret(robot),Detection(robot,20,6))


#Les threads
tourner=Tourner(robot,vitesse,math.pi/2)
tourner.start()
th_control=Thread_control(robot,tourner)
th_control.start()
