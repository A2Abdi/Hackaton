import cv2
import os

def user():
    face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    first = input("Enter your first name: ")

    last = input("Enter your last name: ")

    full_name = first + ' ' + last

    path = os.path.join('C:\\Users\\Ali\\OneDrive - Wayne State University\\Desktop\\Hackaton', full_name)

    os.mkdir(path)

    video_input = input("please input video directory: ")

    webcam = cv2.VideoCapture(video_input)

    while True:

        (read_succesful, frame) = webcam.read()

        n = 0
    
        grey_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        face_coordinates = face_data.detectMultiScale(grey_img)
    
        for (x,y,w,h) in (face_coordinates):
    
            cv2.rectangle( frame ,(x,y), (x+w, y+h), (0,255,0), 5 )

            cv2.imwrite('C:\\Users\Ali\\OneDrive - Wayne State University\\Desktop\\Hackaton\\'+ full_name + '\\picture'+ str(n) +'.png', frame)

        cv2.imshow("Face ", frame)

    
        key = cv2.waitKey(1)
    
        if key ==81 or key == 113:
        
            break

    webcam.release()

    print("code completed")


