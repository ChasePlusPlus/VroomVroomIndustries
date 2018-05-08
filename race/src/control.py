#!/usr/bin/env python
from math import isnan

import rospy
from race.msg import drive_param
from race.msg import pid_input

kp = 14.0
kd = 0.09
servo_offset = 18.5 	# zero correction offset in case servo is misaligned.
prev_error = 0.0
vel_input = 25.0

pub = rospy.Publisher('drive_parameters', drive_param, queue_size=1)

def control(data):
    global prev_error
    global vel_input
    global kp
    global kd

    # Your code goes here
    # 1. Scale the error
    # 2. Apply the PID equation on error
    # 3. Make sure the error is within bounds
    pid_err = data.pid_error
    error = pid_err * kp
    errordot = kd * (prev_error - pid_err)

    angle = error + errordot


    if angle < -100:
        angle = -100
    elif angle > 100:
        angle = 100
    elif isnan(angle):
        angle = 0


    prev_error = pid_err

    print "KP: ", kp, " KD: ", kd, "\r"

    msg = drive_param()
    msg.velocity = vel_input
    msg.angle = angle
    pub.publish(msg)


if __name__ == '__main__':
    global kp
    global kd
    global vel_input
    print("Listening to error for PID")
    kp = input("Enter Kp Value: ")
    kd = input("Enter Kd Value: ")
    vel_input = input("Enter Velocity: ")
    rospy.init_node('pid_controller', anonymous=True)
    rospy.Subscriber("error", pid_input, control)
    rospy.spin()