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
We started this assignment a bit late because of everyone's finals, theses, and end of semester projects. After starting it on May 7th, we made a lot of progress before the assignment was due. 

Control.py: 
Our biggest issue was testing the kd, kp, and theta values to calculate the error properly. We spent a while testing and changing the values to avoid overcompensation and avoid swerving a lot when the car was supposed to be going straight.  The main issue we had was overcompensating to the right. To remedy this, we tried changing the viewing window (by changing theta).  
Eventually we were able to get the car to make two laps consecutively before crashing. After fiddling with the values more we were able to get the car to get a single lap time of 8 seconds. 
		
Dist_Finder.py:
We wrote this node primarily using formulas that we were given. 

Collision Detection:
We implemented this pretty easily. The car stopped if it was a certain distance from an obstacle (velocity was set to 0). 

# Results:
Here is a video of DAVIS (Driving Autonomous Vehicle in Style) doing a laps around the track with one lap time being under 8 seconds:

![Under 8 secs!](https://giphy.com/gifs/lcEAQXV1fxHvYMh2yt/html5)

<a href="https://giphy.com/gifs/lcEAQXV1fxHvYMh2yt/html5"><img src="https://giphy.com/gifs/lcEAQXV1fxHvYMh2yt/html5" title="Under 8 secs!!"/></a>

<iframe src="https://giphy.com/embed/lcEAQXV1fxHvYMh2yt" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/lcEAQXV1fxHvYMh2yt">via GIPHY</a></p>


