xfrom Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import rospy
from std_msgs.msg import String, Float32
from sensor_msgs.msg import Image
import time


class Boat():
    def __init__(self):#, Lmotor, Rmotor):
        mot = Adafruit_MotorHAT(addr=0x60)
        self.Mmotor = mot.getMotor(3)
        self.Lmotor = mot.getMotor(1)
        self.Rmotor = mot.getMotor(4)
        self.Cmotor = mot.getMotor(2)
	self.cStatus = False
	self.status = None

    def cleanup():
        self.stop()
        self.Cmotor.run(Adafruit_MotorHAT.RELEASE)

    def forward(self, speed=200):
        self.stop()
        print ("Forward")
        time.sleep(0.01)
        self.Lmotor.run(Adafruit_MotorHAT.FORWARD)
        self.Rmotor.run(Adafruit_MotorHAT.FORWARD)
        self.Mmotor.run(Adafruit_MotorHAT.FORWARD)
        self.Lmotor.setSpeed(i)
        self.Mmotor.setSpeed(i)
        self.Rmotor.setSpeed(i)
        self.status = 'forward'

    def backwards(self, speed=200):
        self.stop()
        time.sleep(0.01)
        self.Lmotor.run(Adafruit_MotorHAT.BACKWARD)
        self.Rmotor.run(Adafruit_MotorHAT.BACKWARD)
        self.Mmotor.run(Adafruit_MotorHAT.BACKWARD)
        self.Lmotor.setSpeed(i-5)
        self.Mmotor.setSpeed(i)
        self.Rmotor.setSpeed(i+5)
        self.status = 'backwards'

    def right(self, speed=150, times=0.1):
        self.stop()
        time.sleep(0.01)
        self.Rmotor.run(Adafruit_MotorHAT.BACKWARD)
        self.Lmotor.run(Adafruit_MotorHAT.FORWARD)
        self.Lmotor.setSpeed(i)
        self.Rmotor.setSpeed(i)
        time.sleep(times)
        self.status = 'right'

    def left(self, speed=150, times=0.1):
        self.stop()
        time.sleep(0.01)
        self.Lmotor.run(Adafruit_MotorHAT.BACKWARD)
        self.Rmotor.run(Adafruit_MotorHAT.FORWARD)
        self.Lmotor.setSpeed(i)
        self.Rmotor.setSpeed(i)
        time.sleep(times)
        self.status = 'left'

    def stop(self):
        self.Lmotor.run(Adafruit_MotorHAT.RELEASE)  
        self.Rmotor.run(Adafruit_MotorHAT.RELEASE) 
        self.Mmotor.run(Adafruit_MotorHAT.RELEASE) 
        self.status = 'stopped'

    def conveyor(self):
	if self.cStatus:
	    self.Cmotor.run(Adafruit_MotorHAT.RELEASE)
	    self.cStatus = False
	else:
	    self.Cmotor.setSpeed(255)
	    self.Cmotor.run(Adafruit_MotorHAT.FORWARD)
	    self.cStatus = True

    def callback(self,data):
     rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
     if data.data == 'Forward':
           self.forward()
     if data.data == 'Backward':
           self.backwards()
     if data.data == 'Left':
           self.left()
     if data.data == 'Right':
           self.right()
     if data.data == 'B':
           self.stop()
     if data.data == 'Done':
           self.cleanup()

def ros_control(Boat):
    rospy.init_node('control_listener', anonymous=True)

    rospy.Subscriber("control", String, Boat.callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == "__main__":
	EBB = Boat()
	ros_control(EBB)
