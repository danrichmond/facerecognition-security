from urllib2 import Request, urlopen
import base64
import os
import datetime
import time
import logging
import logging.handlers

dir = raw_input("Enter subjects directory name: ")
directory = os.getcwd() + "/subjects/" + dir + "/"
print("\nEnrolling images from: " + directory + "\n")

for filename in os.listdir(directory):
    fileDir = directory + filename
    with open(fileDir, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    values = """
      {
        "image": """ + '"' + encoded_string + '"' + """,
        "subject_id": """ + '"' + dir + '"' + """,
        "gallery_name": "YOUR-GALLERY-NAME"
      }
    """

    headers = {
      'Content-Type': 'application/json',
      'app_id': 'YOUR-APP-ID',
      'app_key': 'YOUR-APP-KEY'
    }
    request = Request('https://api.kairos.com/enroll', data=values, headers=headers)

    response_body = urlopen(request).read()
    LOG_FILE = './logs/EnrollLog.log'
    logging.basicConfig(filename = LOG_FILE, filemode = 'w', level = logging.INFO, format = '%(asctime)s - %(levelname)s: %(message)s', datefmt = '%m/%d/%Y %I:%M:%S %p' )
    logging.info(response_body + "\n")

    print response_body + "\n"
print "\nFinished enrolling. See log for details (" + os.getcwd() + "/logs/EnrollLog.log)\n"
