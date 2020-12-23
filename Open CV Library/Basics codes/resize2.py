import cv2
img=cv2.imread("D:\Hemanth\MIT ACADEMICS\VS CODE\pythprog\opencv\index.png",0)
print(img.shape)

resized_image = cv2.resize(img, (650,500))
cv2.imshow("image",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()