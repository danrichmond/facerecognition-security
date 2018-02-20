from urllib2 import Request, urlopen
from picamera import PiCamera
from time import sleep
import base64
import json
import os
import logging
import logging.handlers
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def SendMail(ImgFileName):
  img_data = open(ImgFileName, 'rb').read()
  msg = MIMEMultipart()
  msg['Subject'] = 'Some Subject'
  msg['From'] = 'SOMEEMAIL@SOMEDOMAIN'
  msg['To'] = 'YOUREMAIL@YOURDOMAIN'

  text = MIMEText("")
  msg.attach(text)
  image = MIMEImage(img_data, name = os.path.basename(ImgFileName))
  msg.attach(image)
  
  # To get your providers server info, reference: https://stackoverflow.com/questions/45210824/connection-error-to-a-smtp-server-with-python
  s = smtplib.SMTP('smtp.gmail.com', 587)
  s.ehlo()
  s.starttls()
  s.ehlo()
  s.login('YOUREMAIL@YOURDOMAIN', 'YOUREMAILPASSWORD')
  s.sendmail('YOUREMAIL@YOURDOMAIN', 'RECIPIENTSEMAIL@RECIPIENTSDOMAIN', msg.as_string())
  s.quit()

camera = PiCamera()
camera.resolution = (500, 500)

count = 0
while True:
  camera.start_preview()
  sleep(5)
  imageName = "image" + str(count) + ".jpg"
  imagePath = os.getcwd() + "/UnidentifiedPeople/" + imageName
  camera.capture(imagePath)
  count += 1
  with open(imagePath, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

  values = """
    {
      "image": """ + '"' + encoded_string + '"' + """,
      "gallery_name" : "Gallery",
      "threshold": "0.40"
    }
  """

  headers = {
    'Content-Type': 'application/json',
    'app_id': 'YOURAPPID',
    'app_key': 'YOURAPPKEY'
  }
  request = Request('https://api.kairos.com/recognize', data=values, headers=headers)
  response = urlopen(request).read()
  
  data = json.loads(response)

  print(response)
  
  ID_LOG_FILE = './logs/RecognitionLog.log'
  logging.basicConfig(filename = ID_LOG_FILE, filemode = 'w', level = logging.INFO, format = '%(asctime)s - %(levelname)s: %(message)s', datefmt = '%m/%d/%Y %I:%M:%S %p' )

  try:
    logging.info("Found " + data["images"][0]["candidates"][0]["subject_id"])
    #print >> log, dateTime + ": Found " + data["images"][0]["candidates"][0]["subject_id"]
    print("Found " + data["images"][0]["candidates"][0]["subject_id"])
    os.remove(imagePath)
  except:
    try:
      tmp = data["images"]
      logging.info("Unidentifiable person in frame. Image: " + imageName)
      print("Unidentifiable person in frame. Image: " + imageName + " - see image in the UnidentifiedPeople directory.")
      SendMail(imagePath)
    except:
      tmpp = data["Errors"]
      os.remove(imagePath)
