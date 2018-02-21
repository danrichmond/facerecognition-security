# facerecognition-security



-- Introduction ---

Using the Kairos Face API to detect unknown faces.

Note: This prototype relys on a RaspberryPi with a camera modual. 

This project is a security system prototype with advanced features. It is being developed on a RaspberryPi with a camera    modual contained within an internal network. It currently utilizes the Kairos Face Recognition API to perform its facial recognition tasks. When an unknown face is found, the system sends you an email with the image of the unknown suspect. Current face recognition threshold is set to 0.40 - this should be higher but I was getting inaccurate results.

Below you will find information regarding each python program in the repo.

--- createAlbum.py ---
Running createAlbum.py will ask for the subjects name then take a bunch of pictures of the subject as they rotate their head around the camera. It then throws those images into a directory which is named after the subject. Now that we have an album containing several photos of the subject, we can enroll that album via enroll.py so the subject will be recognized by the facial recognition API. Alternativly, you may create your own album in the subjects directory then place your own photos in there. Note: If you are adding your own images, make sure the extension type is included.

--- enroll.py ---
Running enroll.py begins by asking for the subjects directory name - this is the name of the directory created while running createAlbum.py - or your personally created directory. The enroll.py program will enter the subject's directory and sequentially add each photo to the subjects album through the API.

--- startCamera.py ---
This is the heart of the prototype. It initiates the camera modual which takes a photo every two seconds - this is expensive in terms of API calls so I would like it to only take photos when motion is detected. It then sends each image to the Kairos API and analyzes the results. If a face is detected and recognized, the subjects name is printed out and appended to the RecognitionLog.log file in the logs directory. If a face is detected and not recognized by the API, the program immediately sends you an email with the unknown subjects image. The email is sent through a simple SMPT protocol client - smtplib. Information is also printed and appended to the RecognitionLog.log file. When no face is detected, no actions are taken.
