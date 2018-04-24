#!/usr/bin/env python

import rospy
from race.msg import drive_values
from race.msg import drive_param
from std_msgs.msg import Bool
velocity, turn = 0, 0

"""
What you should do:
 1. Subscribe to the keyboard messages (If you use the default keyboard.py, you must subcribe to "drive_paramters" which is publishing messages of "drive_param")
 2. Map the incoming values to the needed PWM values
 3. Publish the calculated PWM values on topic "drive_pwm" using custom message drive_values
"""

def params_callback(data):
    global velocity, turn
    velocity = data.velocity
    turn = data.angle


class Talker():

    def __init__(self):
        global velocity, turn

        rospy.init_node('Talker', anonymous=False)

        rospy.loginfo('Press CTRL+c to stop keyboard control')

        rospy.on_shutdown(self.shutdown)

        rospy.loginfo('HERE')
        self.params = rospy.Subscriber('drive_parameters', drive_param,
                                       params_callback)

        rospy.loginfo('HERE')
        self.pwm = rospy.Publisher('drive_pwm', drive_values, queue_size=10)

        rospy.loginfo('HERE')
        rate = rospy.Rate(10)

        rospy.loginfo('Set rate 10Hz')

        pwm_values = drive_values()

        while not rospy.is_shutdown():
            rospy.loginfo('Velocity: {}'.format(velocity))
            pwm_drive = 9831 + int(32.77 * velocity)
            pwm_values.pwm_drive = pwm_drive
            rospy.loginfo('Velocity PWM: {}'.format(pwm_values.pwm_drive))
            rospy.loginfo('Angle: {}'.format(turn))
            pwm_values.pwm_angle = 9831 + int(32.77 * turn)
            rospy.loginfo('Angle PWM: {}'.format(pwm_values.pwm_angle))
            self.pwm.publish(pwm_values)
            rate.sleep()

    def shutdown(self):
        rospy.loginfo('Stopping the turtle')

        self.pwm.publish(drive_values())

        rospy.sleep(1)


if __name__ == '__main__':

    try:
        Talker()
    except:
        rospy.loginfo('Goodnight car')
