import cwiid, time

import rospy
from std_msgs.msg import String 
rospy.init_node('wmcontrol', anonymous=True)
pub = rospy.Publisher('control', String, queue_size=10)

button_delay = 0.1

print 'Please press buttons 1 + 2 on your Wiimote now ...'
time.sleep(1)

try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Cannot connect to your Wiimote. Run again and make sure you are holding buttons 1 + 2!"
  quit()

print 'Wiimote connection established!\n'
print 'Go ahead and press some buttons\n'
print 'Press PLUS and MINUS together to disconnect and quit.\n'

time.sleep(3)

wii.rpt_mode = cwiid.RPT_BTN

while True:

  buttons = wii.state['buttons']

  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print '\nClosing connection ...'
    pub.publish('Done')
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)

  if (buttons & cwiid.BTN_LEFT):
    print 'Left pressed'
    pub.publish('Left')
    time.sleep(button_delay)

  if(buttons & cwiid.BTN_RIGHT):
    print 'Right pressed'
    pub.publish('Right')
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_UP):
    pub.publish('Forward')
    print 'Up pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_DOWN):
    pub.publish('Backward')
    print 'Down pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_1):
    pub.publish('Conveyor')
    print 'Button 1 pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_2):
    print 'Button 2 pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_A):
    print 'Button A pressed'
    pub.publish('A')
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_B):
    pub.publish('B')
    print 'Button B pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_HOME):
    wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
    check = 0
    while check == 0:
      print(wii.state['acc'])
      time.sleep(0.01)
      check = (buttons & cwiid.BTN_HOME)
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_MINUS):
    print 'Minus Button pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_PLUS):
    print 'Plus Button pressed'
    time.sleep(button_delay)
