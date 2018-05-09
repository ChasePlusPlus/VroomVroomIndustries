#!/usr/bin/env python

import rospy
import math
from sensor_msgs.msg import LaserScan
from race.msg import pid_input

# Some useful variable declarations.
angle_range = 24  # sensor angle range of the lidar
car_length = 1.5  # distance (in m) that we project the car forward for correcting the error. You may want to play with this.
desired_trajectory = .5  # can change to .5	# distance from the wall (left or right - we cad define..but this is defined for right)
vel = 15
error = 0.0

pub = rospy.Publisher('error', pid_input, queue_size=10)

#	Input: 	data: Lidar scan data
#			theta: The angle at which the distance is requried
#	OUTPUT: distance of scan at angle theta
def getRange(data, theta):
    # Find the index of the arary that corresponds to angle theta.
    # Return the lidar scan value at that index
    # Do some error checking for NaN and ubsurd values
    # Your code goes here
    index = int((theta + 45) / .25)
    # index = (30 + theta) * (len(data.ranges)/240)
    val = data.ranges[index]
    if math.isnan(val):
        return 50
    else:
        return val

def callback(data):
    theta = 50  # might want to change this
    omega = 90
    a = getRange(data, theta)
    b = getRange(data, 0)
    print(b)
    swing = math.radians(theta)


    alpha = math.atan2(a * math.cos(swing) - b, a * math.sin(swing))
    AB = b * math.cos(alpha)
    AC = .5
    CD = AB + AC * math.sin(alpha)
    error = CD -  0.5
    # alpha = math.atan2(a * math.cos(swing) - b, a * math.sin(swing))
    # aTob = b * math.cos(alpha)

    # aToc = 1
    # cTod = aTob + aToc * math.sin(alpha)

    # error = cTod - desired_trajectory
    # print(error)

    msg = pid_input()
    msg.pid_error = error
    msg.pid_vel = vel
    pub.publish(msg)




if __name__ == '__main__':
    print("Laser node started")
    rospy.init_node('dist_finder', anonymous=True)
    rospy.Subscriber("scan", LaserScan, callback)
    rospy.spin()
