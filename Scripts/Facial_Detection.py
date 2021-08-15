import cv2
import numpy as np 

# The number '0' stands for the WebCam input [ie. if you have multiple webcams pluged-in then select a camera by entering the number]  
cap = cv2.VideoCapture(0)

# Use the 'haarcascade_frontalfaces.xml' haarcascade to detect faces in each Frame 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Use the 'haarcascade_eye.xml' haarcascade to detect faces in each Frame 
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
while(True):
    # Get each frame from the camera 
    ret,frame = cap.read()

    # Convert the Frames from 'Color' to 'Grayscale' and display the Frames
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect any Faces(upto 5 faces) in the Frame with a probability of '1.3'
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        print(x,y,w,h)
        # Draw a rectangle over the 'Face/Faces'
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

        #Range of Interest
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Detects the eyes in the Frames
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            # Draw a rectangle over the eyes
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    
    # Display the Frames
    cv2.imshow('Frame',frame)

    # If user enters 'q' then exit the loop and close the window 
    if(cv2.waitKey(1) == ord('q')):
        break
    
    

# Close the Camera 
cap.release()
cv2.destroyAllWindows()
