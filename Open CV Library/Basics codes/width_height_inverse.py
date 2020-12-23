import numpy as np
import cv2

hems = cv2.imread('D:\ALL BACKUPS\Hemanth.jpeg', cv2.IMREAD_COLOR)
# width, height
# column, row
# its inveresed 
hems= cv2.resize(hems, (480, 640))
head = hems[150:350, 100:300]
hems[0:200, 0:200] = head
hems[0:200, 200:400] = head
hems[200:400, 100:300] = head
hems[400:600, 100:300] = head
cv2.namedWindow('HEMANTH', cv2.WINDOW_AUTOSIZE)
cv2.imshow('HEMANTH N', hems)
