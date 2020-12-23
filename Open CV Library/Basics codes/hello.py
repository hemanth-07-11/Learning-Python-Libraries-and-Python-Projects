

import numpy as np 
import cv2 
import matplotlib.pyplot as plt 
img = cv2.imread('D:\Hemanth\MIT ACADEMICS\VS CODE\pythprog\opencv\index.png',1)
rows,cols = image.shape[:2] 
#(col/2,rows/2) is the center of rotation for the image 
# M is the cordinates of the center 
M = cv2.getRotationMatrix2D((cols/2,rows/2),180,1) 
dst = cv2.warpAffine(image,M,(cols,rows)) 
plt.imshow(dst)