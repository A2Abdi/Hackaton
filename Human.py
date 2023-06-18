import cv2

def human(x):
    human_data = cv2.CascadeClassifier('haarcascade_fullbody.xml')

    webcam = cv2.VideoCapture(x)
    
    while True:

        show_human, frame = webcam.read()

        if show_human:

            human_grey =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        else:
            break

        human_coordinates = human_data.detectMultiScale(human_grey)

        for (x,y,w,h) in (human_coordinates):
    
            cv2.rectangle( frame ,(x,y), (x+w, y+h), (0,255,0), 2 )


        cv2.imshow('Show ', frame)
        cv2.waitKey(1)