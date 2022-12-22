import numpy as np
import cv2 as cv
import time

def CircularHT(file):

    # array for storing coordinate values
    coordinate = []
    
    # import image file from path images/... folder 
    img = cv.imread(file,0)
    # obtain the size of the image and calculate a scaling factor for X and Y 
    size = img.shape
    Y_ratio = 20.6/size[0]
    X_ratio = 29.3/size[1]

    # Binarize image and compute Hough Circle Transform using pre determinded values for min/max radius 
    cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
    circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20,param1=100,param2=30,minRadius=0, maxRadius=30)
    circles = np.uint16(np.around(circles))

    # annotate the image with the highlighted circles and centre points
    for i in circles[0,:]:
        # draw the outer circle
        cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
        # append the coordinates of each circles centre point and scale
        coordinate.append((round(i[0]*Y_ratio,1),round(i[1]*X_ratio,1)))

    print(coordinate)

    # write the resulting image to a file and close all windows 
    cv.imwrite('testgridDexRESULT.jpg',cimg)
    cv.waitKey(0)
    cv.destroyAllWindows()

start = time.perf_counter()
CircularHT('tyre6.png')
end = time.perf_counter()
print(end)