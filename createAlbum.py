from picamera import PiCamera
from time import sleep
import os

camera = PiCamera()
camera.resolution = (500, 500)

subjectDirectory = raw_input("\nEnter subject's first and last name with no spaces: ")
print "Scanning... please rotate it around the camera"

try:
  os.mkdir(os.getcwd() + "/" + subjectDirectory)
except:
  print "Subject already has an album. Adding new images to existing album..."
  # In this exception, could the number of files in the existing directory then
  # set count to that number so it does not overwrite existing images.

count = 1
while count < 15:
  imageName = "/" + subjectDirectory + "/image" + str(count) + ".jpg"
  imagePath = os.getcwd() + imageName
  camera.capture(imagePath)
  count += 1
  sleep(1)

print "Images have been loaded into " + os.getcwd() + "/" + subjectDirectory + "\n"
