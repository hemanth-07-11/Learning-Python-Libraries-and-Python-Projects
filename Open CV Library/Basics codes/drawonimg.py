
import cv2
import numpy as np

img = cv2.imread('D:\Hemanth\MIT ACADEMICS\VS CODE\pythprog\opencv\index.png',1)

#              start    end       b,g,r         pixel no.
cv2.line(img, (0,0) , (50,75) , (255,255,255) , 5)
cv2.rectangle(img , (20,20) , (100,150) , (0,255,0) , 5)
cv2.circle(img , (40,50) , 30 , (255,0,0), -2)            

cv2.imshow('image' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()