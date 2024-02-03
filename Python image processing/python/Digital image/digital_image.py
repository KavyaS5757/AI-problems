import cv2
from skimage.filters import sobel

img = cv2.imread("E:/courses/projects ml/digital image/Screenshot (211).png",0)
img1 = sobel(img)

cv2.imshow("pic", img)
cv2.imshow("edge", img1)
print(img.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()