#!/usr/bin/env python

import rospy
from race.msg import drive_param # import the custom message
import curses

forward = 0;
turn = 0;
increment = 0.1

n = raw_input("Change increment? ")
if n == "":
   print "default set to 0.1", "\r"
else:
   increment = int(n)
   print "increment set to: ", increment, "\r"


stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)
rospy.init_node('keyboard_talker', anonymous=True)
pub = rospy.Publisher('drive_parameters', drive_param, queue_size=10)



stdscr.refresh()

key = ''
forward = 0 #positive is forward, negative is backwards
turn = 0 #positive is right, negative is left



	
while key != ord('q'):
	key = stdscr.getch()
	stdscr.refresh()
        

        # fill in the conditions to increment/decrement throttle/steer
	
	
	if key == curses.KEY_UP:
	    if forward <= 100 and forward + increment <= 100:
		forward += increment
		print "Throttle up: ", forward, "\r" 
	    else:
		print "MAX THROTTLE", "\r"
    
	elif key == curses.KEY_DOWN:
	    if forward >= -100 and forward - increment >= -100:
                forward -= increment
	        print "Throttle down: ", forward, "\r"
	    else:
	        print "MAX REVERSE", "\r"

	if key == curses.KEY_LEFT:
	    if turn >= -100 and turn - increment >= -100:
            	turn -= increment
	    	print "LEFT: ", turn, "\r"
	    else:
		print "MAX LEFT", "\r"

	elif key == curses.KEY_RIGHT:
            if turn <= 100 and turn + increment <= 100:
            	turn += increment
	    	print "RIGHT: ", turn, "\r"
	    else:
		print "MAX RIGHT", "\r"

        elif key == curses.KEY_DC:
            # this key will center the steer and throttle
            forward = 0
	    turn = 0
	    print "THROTTLE/STEER RESET!", "\r"

	elif key == ord('r'):   #reset key for mac users
	    forward = 0
            turn = 0
	    print "THROTTLE/STEER RESET!", "\r"

	msg = drive_param()
	msg.velocity = forward
	msg.angle = turn
	pub.publish(msg)

curses.endwin()
