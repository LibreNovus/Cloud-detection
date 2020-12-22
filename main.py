from sense_hat import SenseHat
# from picamera import PiCamera
import ephem
import math
import random
from time import sleep
sense = SenseHat()
# camera = PiCamera()
# sense.show_message("Hello")

day = False

def commastart():	
	r = (255, 0, 0)     # red
	o = (255, 128, 0)   # orange
	y = (255, 255, 0)   # yellow
	g = (0, 255, 0)     # green
	c = (0, 255, 255)   # cyan
	b = (0, 0, 255)     # blue
	p = (255, 0, 255)   # purple
	n = (255, 128, 128) # pink
	w =(255, 255, 255)  # white
	k = (0, 0, 0)       # blank
	
	#rainbow = [r, o, y, g, c, b, p, n]
	
	comma = [
	        k, k, k, k, k, k, k, k,
	        k, k, k, k, k, k, k, k,
	        k, k, k, g, g, k, k, k,
	        k, k, k, g, g, k, k, k,
	        k, k, k, k, g, k, k, k,
	        k, k, k, g, k, k, k, k,
	        k, k, k, k, k, k, k, k,
	        k, k, k, k, k, k, k, k
	        ]
	
	comma_red = [
	        g, g, g, g, g, g, g, g,
	        g, g, g, g, g, g, g, g,
	        g, g, g, r, r, g, g, g,
	        g, g, g, r, r, g, g, g,
	        g, g, g, g, r, g, g, g,
	        g, g, g, r, g, g, g, g,
	        g, g, g, g, g, g, g, g,
	        g, g, g, g, g, g, g, g
	        ]
	
	while True:
	    sense.clear()
	
	    sense.set_pixels(comma)
	    sleep(3)
	    
	    for y in range(8):
	        colour = g
	        for x in range(8):
	            if x == 3 and y == 5:
	                sense.set_pixel(3, 5 , r)
	            elif x == 4 and y == 4:
	                sense.set_pixel(4, 4 , r)
	            elif x == 4 and y == 3:
	                sense.set_pixel(4, 3 , r)
	            elif x == 4 and y == 2:
	                sense.set_pixel(4, 2 , r)
	            elif x == 3 and y == 2:
	                sense.set_pixel(3, 2 , r)
	            elif x == 3 and y == 3:
	                sense.set_pixel(3, 3 , r)
	            else:
	                sense.set_pixel(x, y, colour)
	        sleep(0.20)
	    sleep(1.5)
	    for t in range(18):
	        r1 = random.randint(0, 1) 
	        sense.clear()
	        sleep(0.1)
	        sense.set_pixels(comma_red)
	        if r1 >= 0.5:
	            sense.flip_v()
	        else:
	            sense.flip_h()
	        sleep(0.05)
	     
	    sense.show_message("Team Comma", text_colour = g, back_colour = k)


def getLocation():

def isDay():
	day = False
	name = "ISS (ZARYA)"
	line1 = "1 25544U 98067A   20299.39644679  .00001347  00000-0  32240-4 0  9990"
	line2 = "2 25544  51.6450  64.1844 0001663  59.0364 352.4687 15.49332070252203"
	
	iss = ephem.readtle(name, line1, line2)
	iss.compute()
	
	sun = ephem.Sun()
	sun.compute()
	
	moon = ephem.Moon()
	moon.compute()
	
	vinkel = float(repr(iss.ra))-float(repr(sun.ra))
	
	abs_vinkel = abs(vinkel)
	
	if 3/2*math.pi > abs_vinkel > math.pi/2:
		day = False
		return day
	else:
		day = True
		return day

def main():
	if isDay() == True:
		print('Daytime')
	elif isDay() == False:
		print('Nighttime')

if __name__ == '__main__':
	main()