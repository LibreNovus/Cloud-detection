#from sense_hat import SenseHat
# from picamera import PiCamera
import ephem
import math
import random
from time import sleep
#sense = SenseHat()
# camera = PiCamera()
# sense.show_message("Hello")

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
	
	ddr = (255, 0, 0)
	ddk = (0, 0, 0)
	ddy = (255, 255, 0)  # pika yellow
	ddc = (0, 255, 255)  # pika cyan
	ddg = (0, 255, 0)  # pika green
	ddo = (184, 103, 22) # pika orange
	dlo = (255, 143, 0) # pika ligt orange
	ddk = (97, 97, 97)   # pika gray
	
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
	        w, w, w, w, w, w, w, w,
	        w, w, w, w, w, w, w, w,
	        w, w, w, r, r, w, w, w,
	        w, w, w, r, r, w, w, w,
	        w, w, w, w, r, w, w, w,
	        w, w, w, r, w, w, w, w,
	        w, w, w, w, w, w, w, w,
	        w, w, w, w, w, w, w, w
	        ]
	        
	denmark = [
	        r, r, w, w, r, r, r, r,
	        r, r, w, w, r, r, r, r,
	        r, r, w, w, r, r, r, r,
	        w, w, w, w, w, w, w, w,
	        w, w, w, w, w, w, w, w,
	        r, r, w, w, r, r, r, r,
	        r, r, w, w, r, r, r, r,
	        r, r, w, w, r, r, r, r
	        ]
	
	pika = [
	        ddc, ddg, ddg, ddc, ddc, ddc, ddc, ddg,
	        ddc, ddc, ddy, dlo, ddc, ddc, ddc, ddy,
	        ddc, ddc, ddc, ddy, ddy, ddy, ddy, ddy,
	        dlo, dlo, ddc, ddy, ddk, ddy, ddy, ddk,
	        dlo, dlo, ddc, ddr, ddy, ddy, ddy, ddy,
	        ddc, ddo, ddc, ddy, dlo, dlo, dlo, ddc,
	        ddc, ddo, ddy, dlo, ddy, dlo, ddy, ddc,
	        ddg, ddg, ddy, dlo, ddo, ddo, dlo, ddg
	        ]
	
	sense.clear()
	sense.set_pixels(denmark)
	sleep(3)
	
	for y in range(8):
	    colour = w
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
	for t in range(6):
	    r1 = random.randint(0, 1) 
	    sense.clear()
	    sleep(0.3)
	    sense.set_pixels(comma_red)
	    if r1 >= 0.5:
	        sense.flip_v()
	    else:
	        sense.flip_h()
	    sleep(0.3)
	 
	sense.show_message("Team Comma", text_colour = r, back_colour = w)
	sleep(2)
	main()

def getLocation():
	pass
def isDay():
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
		return False
	else:
		return True

def main():
	if isDay() == True:
		print('Daytime comma starting')
		commastart()
	elif isDay() == False:
		print('Nighttime comma waiting')

if __name__ == '__main__':
	main()