import numpy as np
import cv2
img = cv2.imread('D:\ALL BACKUPS\hemanth.jpeg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27: # wait for ESC key to exit
    print('Quitting without saving..')
    cv2.destroyAllWindows()
elif k == ord('s'): #press 's' key to save and exit
    print('Saving the gray image..')
    cv2.imwrite('hemanthgray.jpeg',img)
    cv2.destroyAllWindows()
