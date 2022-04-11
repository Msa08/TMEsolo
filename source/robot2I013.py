import math
class Robot2I013(object) :
    WHEEL_BASE_WIDTH= 117  # distance (mm) de la roue gauche a la roue droite.
    WHEEL_DIAMETER= 66.5 #  diametre de la roue (mm)
    WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * math.pi # perimetre du cercle de rotation (mm)
    WHEEL_CIRCUMFERENCE = WHEEL_DIAMETER * math.pi # perimetre de la roue (mm)

    def __init__(self) :
        self.MOTOR_RIGHT=1
        self.MOTOR_LEFT=0
        self.fps=0
        self.LED_LEFT_EYE = 0
        self.LED_RIGHT_EYE = 0
        self.LED_LEFT_BLINKER = 0
        self.LED_RIGHT_BLINKER = 0
        self.LED_WIFI = 0

    def set_motor_dps(self, port, dps):     
        print("set_motor_dps")
      
    def get_motor_position(self):
        return (1,2)
      
    def offset_motor_encoder(self, port, offset):
        print("offset_motor")
      
    def get_distance(self):
        return 100
      
    def servo_rotate(self,position):
        print("servo_rotate")
      
    def stop(self):
        print("stop")
    
    def offset_motor_encoder(self, port, offset):
        """
        Fixe l'offset des moteurs (en degres) (permet par exemple de reinitialiser a 0 l'etat 
        du moteur gauche avec offset_motor_encode(self.MOTOR_LEFT,self.read_encoders()[0])
        
        :port: un des deux moteurs MOTOR_LEFT ou MOTOR_RIGHT (ou les deux avec +)
        :offset: l'offset de decalage en degre.
        Zero the encoder by offsetting it by the current position
        """
    
    def get_motor_position(self):
        """
        Lit les etats des moteurs en degre.
        :return: couple du  degre de rotation des moteurs
        """
        return (1,2)
      
    def get_image(self):
        return 10

    def read_encoders(self):
        return (0,0)