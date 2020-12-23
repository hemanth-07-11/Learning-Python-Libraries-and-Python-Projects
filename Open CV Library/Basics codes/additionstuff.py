import cv2
# addition stuff
# cv2 add goes to 255 and saturates
# numpy add tho goes further than 255 reseting to 0
# the formula for weighted add
# dst = α·img1 + β ·img2 + γ

hems = cv2.imread('D:\ALL BACKUPS\Hemanth.jpeg')
hemsh = cv2.imread('D:\ALL BACKUPS\Hemanth.jpeg')
hems = cv2.resize(hems, (600, 400))
hemsh = cv2.resize(hemsh, (600, 400))
print(hems.shape, hemsh.shape)
numpy_add = hems + hemsh
cv_add = cv2.add(hems, hemsh)
cv2.imshow('np_add', numpy_add)
cv2.imshow('cv_add', cv_add)

