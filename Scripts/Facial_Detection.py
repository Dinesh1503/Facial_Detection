import cv2
import numpy as np 

# The number '0' stands for the WebCam input [ie. if you have multiple webcams pluged-in then select a camera by entering the number]  
cap = cv2.VideoCapture(0)
while(True):
    #Get each frame from the camera 
    ret,frame = cap.read()
    cv2.imshow('Frame',frame)
    # If user enters 'q' then exit the loop and close the window 
    if(cv2.waitKey(0) == ord('q')):
        break

# Close the Camera 
cap.release()
cv2.destroyAllWindows()
