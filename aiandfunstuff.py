import cv2
import numpy as np

# 500 x 250
# img1 = cv2.imread('3D-Matplotlib.png')
# img2 = cv2.imread('mainsvmimage.png')

# img1 = cv2.imread('modern.jpg')
# img2 = cv2.imread('ok.jpg')

'''add = img1+img2

cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
img=cv2.imread('bookpage.jpg')
retval,threshold=cv2.threshold(img,12,255,cv2.THRESH_BINARY)
graysclaed=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2,threshold2=cv2.threshold(graysclaed,12,255,cv2.THRESH_BINARY)
guas=cv2.adaptiveThreshold(graysclaed,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

cv2.imshow('original',img)

cv2.imshow('threshold',threshold)

cv2.imshow('threshold',threshold2)
cv2.imshow('threshold',guas)
cv2.waitKey(0)
cv2.destroyAllWindows()