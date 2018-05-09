# VroomVroomIndustries
Vroom Vroom Industries code for F1/10 Autonomous Racing

# Team Effort:
We all coded together off of two laptops. We coded remotely off the car and pushed to Github when we felt it was ready to test. 
	
# Building the car: 
First we started by building the car in class. We've compiled a video of a couple of pictures describing the process. 
VIDEO HERE

# Keyboard Control: 
This assignment took us a few days to get functioning properly. After about three hours, we achieved code that we thought should be working. We decided to take the code to the TA's office hours the next day, but found from another classmate that there was an error in the given number for PWM conversion. Once we fixed that value, it worked for assignment. 

The demo did not go over as well because our battery died. We have a couple videos of our car working in the classroom from a few days prior to the assignment being due. 
VIDEO HERE
	
Talker.py:
We implemented the talker using the formula given to convert the output to PWM values and code similar to that of the TurtleBot. 

Keyboard.py:
We implemented the keyboard file by using a series of if/elif statements. Using the curses library offered by Python, we detected which key was being pressed and incrementally changed the values of forward to gradually go forwards or backwards (positive for forwards and negative for backwards). The same logic was used to change left or right. We also added a reset key for the PC and a reset value for the Mac. We had the ability to change the the increment as well, since as we were testing we wanted to find the optimal value of the increment as we were running the code on the car.
		
# Vroom Vroom Industries Goes Autonomous. 
We started this assignment a bit late because of everyone's finals, theses, and end of semester projects. After starting it on May 7th, we made a lot of progress before the assignment was due. 
VIDEO HERE

Control.py: 
Our biggest issue was testing the kd, kp, and theta values. We spent a while testing and changing the values to avoid overcompensation and avoid swerving a lot when the car was supposed to be going straight. We didn't get this to perfectly work, especially at the point in the track where the track dips in on the other side of the finish line. The main issue we had was overcompensating to the right. To remedy this, we tried changing the viewing window (by changing theta).  
		
Dist_Finder.py:
We wrote this node primarily using formulas that we were given. 

# Results:
Here is a video of DAVIS (Driving Autonomous Vehicle in Style) doing a laps around the track with one lap time being under 8 seconds:

<a href="https://i.imgur.com/0NghbBr.gif"><img src="https://i.imgur.com/0NghbBr.gif"/></a>

