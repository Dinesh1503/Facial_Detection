import cv2
import numpy as np 

# The number '0' stands for the WebCam input [ie. if you have multiple webcams pluged-in then select a camera by entering the number]  
cap = cv2.VideoCapture(0)
while(True):
    # Get each frame from the camera 
    ret,frame = cap.read()
    # Display the Frames
    cv2.imshow('Frame',frame)

    # Convert the Frames from 'Color' to 'Grayscale' and display the Frames
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale',gray)

    # If user enters 'q' then exit the loop and close the window 
    if(cv2.waitKey(1) == ord('q')):
        break

# Close the Camera 
cap.release()
cv2.destroyAllWindows()
