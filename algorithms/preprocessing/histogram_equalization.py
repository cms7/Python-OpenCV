import cv2 as cv
from cv2 import imread
from cv2 import imshow
import cv2 as cv
from cv2 import imwrite
import numpy as np

# histogram equalization for use on darker images

img = cv.imread('images/dark_wheel.jpg',0)

scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)

equ = cv.equalizeHist(resized)

cv.imwrite('images/contrast.jpg', equ)
cv.waitKey(0)
cv.destroyAllWindows()

