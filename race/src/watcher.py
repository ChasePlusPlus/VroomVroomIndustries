!#/usr/bin/env python

import rospy
from race.msg import drive_param # import the custom message
import os

rospy.init_node('watcher', anonymous=True)
pub = rospy.Publisher('drive_parameters', drive_param, queue_size=10)


while(True):
	if os.system("ping -c 1 192.168.50.25") == 0:
		print "Connection OKAY", "\r"
	else:
		print "Connection dropped!", "\r"
		msg = drive_param()
		msg.velocity = 0
		msg.angle = 0
		pub.publish(msg)

