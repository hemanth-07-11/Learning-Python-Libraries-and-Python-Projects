import numpy as np
import cv2
import copy

# Reading frames from webcam
cap = cv2.VideoCapture(0)
# Initial frame is stored as prevFrame
ret1, prevframe = cap.read()
while(1):
    # Current frame is stored as currFrame
    ret2, currframe = cap.read()
    # Absolute difference between prevFrame and currFrame is computed
    diff = cv2.absdiff(prevframe, currframe)
    # Difference image is converted to grayscale
    gray_color = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    # Gaussian Blur is computued
    gauss = cv2.GaussianBlur(gray_color, (5, 5), 0)
    # Threshold is calculated using THRESH_BINARY Method
    _, mask = cv2.threshold(gauss, 35, 255, cv2.THRESH_BINARY)
    cv2.imshow('Original', prevframe)
    cv2.imshow('intermediate output', mask)

    # Defining a kernel  
    kernel = np.ones((5,5), np.uint8)
    # The 'erode' morphology method is used
    transFrame = cv2.erode(mask, kernel, iterations = 1)
    # The value in currFrame is cloned to 'flag' variable using deepcopy method
    flag = copy.deepcopy(currframe)
    # Contours are found in transFrame
    c, h = cv2.findContours(transFrame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Contours are drawn in flag
    cv2.drawContours(flag, c, -1, (0, 21, 255), 2)
    cv2.imshow('output', flag)
    # PrevFrame is updated with currFrame and this is continued until the loop is exited  
    prevframe = currframe
    
    
    k = cv2.waitKey(5) & 0xFF                                   
    if k == 27:                                                 
        break                                                   
cv2.destroyAllWindows()                                         
cap.release()         
