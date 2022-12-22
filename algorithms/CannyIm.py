
import cv2 
import glob
import time

image_list = []
folder_dir = 'images/DirtyNoisy'

for images in glob.iglob(f'{folder_dir}/*'):
    if(images.endswith(".jpg")):
        image_list.append(images)

def otsu_canny(image, lowrate=0.7):
    if len(image.shape) > 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Otsu's thresholding
    ret, _ = cv2.threshold(image, thresh=0, maxval=255, type=(cv2.THRESH_BINARY + cv2.THRESH_OTSU))
    edged = cv2.Canny(image, threshold1=(ret * lowrate), threshold2=ret)

    # return the edged image
    return edged

# loop which will run and write output of a collection of images using Canny
sum = 0.0
for i in range(len(image_list)):
    txt = 'testgridCanny_tyre'
    type = '.jpg'
    file = f'{txt}{i}{type}'

    img = cv2.imread('images/LowContrast/contrast.jpg')
    edged = otsu_canny(img)

    cv2.imwrite(file, edged)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

