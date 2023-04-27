import cv2
from datetime import datetime
import csv

date = datetime.now()
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')
data_list = [ [" Bonjour voila les résultat pour aujourdhui ", str(date) ],
              ]
with open('faces_data.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data_list)

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    i=0
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        i=i+1
    # Display
    cv2.imshow('img', img)
    data_list2 = [ [" NB_VISAGES ", str(i),"DATE_HEURE(par ms)" ,str(date) ]]
    with open('faces_data.csv', 'a', newline='') as file:
     writer = csv.writer(file, delimiter='|')
     writer.writerows(data_list2)
    
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()