#!/usr/bin/env python
import rospy
from race.msg import drive_param
from race.msg import pid_input

kp = 14.0
kd = 0.09
servo_offset = 11
prev_error = 0.0
vel_input = 25.0
velo = 0
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
    pid_err = data.pid_error * 10
    error = pid_err * kp
    errordot = kd * (prev_error - pid_err)

    angle = servo_offset + (error + errordot)
    if data.pid_vel == 0:
	velo = 0
    else: 
	velo = vel_input 

    if angle < -99:
        angle = -99
    elif angle > 99:
        angle = 99
    elif angle < 10 and angle > -10:
	velo = vel_input + 10
    elif angle > 80 and angle < -80:
	velo = vel_input + 5

    prev_error = pid_err

    angle = angle

    print("angle: ", angle)
    msg = drive_param()
    msg.velocity = velo
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
