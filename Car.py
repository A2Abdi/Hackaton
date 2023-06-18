import cv2

def car(x):
    car_data = cv2.CascadeClassifier('cars.xml')

    webcam = cv2.VideoCapture(x)
    
    while True:

        show_car, frame = webcam.read()

        if show_car:

            car_grey =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        else:
            break

        car_coordinates = car_data.detectMultiScale(car_grey)

        for (x,y,w,h) in (car_coordinates):
    
            cv2.rectangle( frame ,(x,y), (x+w, y+h), (0,255,0), 2 )


        cv2.imshow('show car', frame)
        key = cv2.waitKey(1)

        if key ==81 or key == 113:
        
            break
car('tesla2.mp4')