# VroomVroomIndustries
Vroom Vroom Industries code for F1/10 Autonomous Racing

# Team Effort:
We all coded together off of two laptops. 

# Keyboard Control: 
This assignment took us a few days to get functioning properly. After about three hours, we achieved code that we thought should be working. We decided to take the code to the TA's office hours the next day, but found from another classmate that there was an error in the given number for PWM conversion. Once we fixed that value, it worked for assignment. 

The demo did not go over as well because our battery died. We have a couple videos of our car working in the classroom from a few days prior to the assignment being due. 
VIDEO HERE
	
Talker.py:
We implemented the talker using the formula given to convert the output to PWM values and code similar to that of the TurtleBot. 

Keyboard.py:
We implemented the keyboard file by using a series of if/elif statements. Using the curses library offered by Python, we detected which key was being pressed and incrementally changed the values of forward to gradually go forwards or backwards (positive for forwards and negative for backwards). The same logic was used to change left or right. We also added a reset key for the PC and a reset value for the Mac. We had the ability to change the the increment as well, since as we were testing we wanted to find the optimal value of the increment as we were running the code on the car.
		
# Vroom Vroom Industries Goes Autonomous:

Control.py: 
Our biggest issue was testing the kd, kp, and theta values to calculate the error properly. We spent a while testing and changing the values to avoid overcompensation and avoid swerving a lot when the car was supposed to be going straight.  The main issue we had was overcompensating to the right. To remedy this, we tried changing the viewing window (by changing theta).  
Eventually we were able to get the car to make two laps consecutively before crashing. After fiddling with the values more we were able to get the car to get a single lap time of 8 seconds and a run of 7 continuous laps without stopping. We locked in two separate configurations for kd, kp, and velocity that give us solid lap results (one more conservative than the other configuration).
		
Dist_Finder.py:
We wrote this node primarily using formulas that we were given. We utilized theta values of 60, 0 (for car localization/error calculation) and 90 (for collision avoidance). 

Collision Detection:
We implemented this pretty easily. The car stopped if it was a certain distance (1 meter) from an obstacle (velocity was set to 0). This had a compound effect of preventing crashes during misjudged turns.  When the car came into a turn too fast, collision avoidance would quickly slow the car, allowing a greater time for steering to correct and the car to continue.

Launch File:
We created this. 

Velocity PID:
We implemented this by adding conditionals based on the angle in control.py. We then gradually changed the values of velocity depending on the condition - when the wheels are straightening out, we boost velocity by almost double. We also implemented a slight boost to velocity when we are turning at full stop to hold a better line and overcome some of the slowing that is expereinced during a turn with a constant velocity. 

# Results:
Here is a video of DAVIS (Driving Autonomous Vehicle in Style) doing a laps around the track with one lap time being under 8 seconds:

Gif: [Sub-8 Run](https://i.imgur.com/0NghbBr.gifv)
Video:
[![Sub-8 Run](https://youtu.be/_lQ3kTyml7E.jpg)](https://youtu.be/_lQ3kTyml7E)

After we got collision avoidance to work, the car avoided crashes for the rest of testing. If the car was going to run into the wall, it would stop. Please see the video link above for examples of laps where this functionality is demonstrated.

Working deep into the early morning of race day (5am) to continue pushing our car/algorithms to put down consistent, quick laps, we discovered that the steering controls no longer responded to program or remote input. After talking to the TA in the morning, we found out that there was an issue with our servo for steering control.  

