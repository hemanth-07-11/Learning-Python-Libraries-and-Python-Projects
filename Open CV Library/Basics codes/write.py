import numpy as np
import cv2
img = np.zeros((700,1024,3), np.uint8)


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'HEMANTH N',(10,256), font, 4,(0,0,255), 8, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
