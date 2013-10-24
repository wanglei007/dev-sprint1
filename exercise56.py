#Exercise5.6 Koch Curve
# Lei Wang

from swampy.TurtleWorld import *

World= TurtleWorld()
bob = Turtle()
bob.delay = 0.1
print bob

def koch(t, x):

	if (x<3):
		fd(t, x)
		return

	angle = 60
	koch(t, x/3)
	lt(t, angle)
	koch(t, x/3)
	rt(t, 2 * angle)
	koch(t, x/3)
	lt(t, angle)
	koch(t, x/3)

def snowflake(t, x, n):

	angle = 360/n

	for i in range(n):
		koch(t, x)
		rt(t, angle)
	
snowflake(bob, 60, 3)
bob.die()

wait_for_user()

