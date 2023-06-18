import cv2
import intro
import Mongo
import os
from pynput import keyboard
name,age, country = intro.Introduction()

Mongo.updateMogoUserCollection(name,age,country)
name_input = "Input video name or press enter if u want to use camera " + name + " : "
print("There is test videos in 'test' file if you want to use test instead of camera please input complete path")
User = input(name_input)

n = 0

car_data = cv2.CascadeClassifier('cars.xml')

human_data = cv2.CascadeClassifier('haarcascade_fullbody.xml')

face_data = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

Human_upper_data = cv2.CascadeClassifier('haarcascade_upperbody.xml')

if User == "":
    webcam = cv2.VideoCapture(0)
else:
    extension = input("Please input the correct video extension : ")
    
    webcam = cv2.VideoCapture( User + "." + extension )
    
    print("\n\nThe program will start now but remember the only way to close the window is by\n\
          either clicking on the space bar or the Esc button.\n\n\
          THANK YOU and ENJOY!!\n\n")
while True:

    show, frame = webcam.read()

    if show:

        car_grey =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        human_grey =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        Human_upper_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
    else:
        break

    car_coordinates = car_data.detectMultiScale(car_grey)

    human_coordinates = human_data.detectMultiScale(human_grey)

    face_coordinates = face_data.detectMultiScale(face_img)

    Human_upper_coordinates = Human_upper_data.detectMultiScale(Human_upper_grey)

    for (x,y,w,h) in (car_coordinates):
    
        cv2.rectangle( frame ,(x,y), (x+w, y+h), (0,255,0), 2 )

        car_path = './pictures/Car_pictures'

        if n % 20 == 0:

            cv2.imwrite(os.path.join(car_path,'Car_picture'+str(n)+'.jpg'),frame)

    for (x,y,w,h) in (human_coordinates):
    
        cv2.rectangle( frame ,(x,y), (x+w, y+h), (0,0,255), 2 )

        Fullbody_path = './pictures/Fulllbody_pictures'

        if n % 20 == 0:

            cv2.imwrite(os.path.join(Fullbody_path,'body_picture'+str(n)+'.jpg'),frame)

    for (x,y,w,h) in (Human_upper_coordinates):
    
        cv2.rectangle( frame ,(x,y), (x+w, y+h), (0,0,255), 2 )

        Upperbody_path = './pictures/Upperbody_pictures'

        if n % 20 == 0:

            cv2.imwrite(os.path.join(Upperbody_path,'body1_picture'+str(n)+'.jpg'),frame)

    for (x,y,w,h) in (face_coordinates):
    
        cv2.rectangle( frame ,(x,y), (x+w, y+h), (255,0,255), 2 )

        Faces_path = './pictures/Face_pictures'

        if n % 20 == 0:

            cv2.imwrite(os.path.join(Faces_path,'Face_picture'+str(n)+'.jpg'),frame)

    n = n + 1
    cv2.imshow('show ', frame)
    
    key = cv2.waitKey(1) & 0xFF

    if key == ord(' ') or key == 27:
        
          break
        
webcam.release()
cv2.destroyAllWindows()
