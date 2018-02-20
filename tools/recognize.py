from urllib2 import Request, urlopen
import base64
import json
import os

testImg = raw_input("Enter name of image including extension: ")
directory = os.getcwd() + "/" + testImg

with open(directory, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

values = """
  {
    "image": """ + '"' + encoded_string + '"' + """,
    "gallery_name": "PhotoGallery",
    "threshold": "0.33"
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

try:
  print("Found " + data["images"][0]["candidates"][0]["subject_id"])
except:
  try:
    tmp = data["images"]
    print("Unidentifiable person in frame.")
  except:
    tmpp = data["Errors"]
