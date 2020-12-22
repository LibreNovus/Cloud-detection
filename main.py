from sense_hat import SenseHat
from picamera import PiCamera
sense = SenseHat()
camera = PiCamera()
sense.show_message("Hello")

def commastart():
    pass

camera.capture("picture.jpg")