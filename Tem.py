# -*- coding: utf-8 -*-
"""
Created on Tue May 23 19:43:50 2023

@author: zhao
"""

import numpy as np
import cv2


if __name__ == "__main__":
    '''
    Main function
    '''
    
    #read camera
    cap = cv2.VideoCapture(0)
     
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
     
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     
        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
     
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    