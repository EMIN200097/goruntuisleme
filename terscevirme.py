import numpy as np
import cv2 as cv
from matplotlib import pyplot as plot
import math

img = cv.imread('hand.jpg')

plot.figure(1)
plot.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plot.title('Orjinal Fotograf', fontweight="bold")


def renkisleme(img, funcao):
    (imgB, imgG, imgR) = cv.split(img)
    imageB = funcao(imgB)
    imageG = funcao(imgG)
    imageR = funcao(imgR)
    image = cv.merge((imageR, imageG, imageB))
    return image
def negativ(img):
    satir = np.size(img, 0)
    sutun = np.size(img, 1)
    image = np.zeros((satir, sutun), dtype='uint8')
    for l in range(satir):
        for c in range(sutun):
            image[l, c] = 255 - img[l, c]
    return image


(imgB, imgG, imgR) = cv.split(img)
imageB = negativ(imgB)
imageG = negativ(imgG)
imageR = negativ(imgR)
image = cv.merge((imageR, imageG, imageB))
plot.figure(2)
plot.imshow(image)
plot.title('Negatif Goruntu', fontweight="bold")

plot.show()