# from sense_hat import SenseHat
# from picamera import PiCamera
import ephem
import math

# sense = SenseHat()
# camera = PiCamera()
# sense.show_message("Hello")

day = False

def commastart():
    pass

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
main()