from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("butterfly.jpg")
img_resize = cv2.resize(img,(800,400))
cv2.imshow("img",img_resize)
img_gray = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale image', img_gray)
histrogram = cv2.calcHist([img_gray],[0],None,[256],[0,256])
plt.plot(histrogram)
plt.show()
cv2.waitKey(0)
