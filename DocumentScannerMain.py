import cv2
import numpy as np
import utils

################################################
webCamFeed = True
pathImg = 'doc.jpg'
cap = cv2.VideoCapture(1)
cap.set(10,160) # brightness of cam
heightImg = 640
widthImg = 480
################################################

utils.initializeTrackbar()
count = 0

while True:
    # blank image
    imgBlank = np.zeros((heightImg,widthImg,3, np.uint8))

    if webCamFeed: success, img = cap.read()
    else: img = cv2.imread(pathImg)
    img = cv2.resize(img,(widthImg, heightImg))
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1)
    thres = utils.valTrackbars()
    imgThreshold = cv2.Canny(imgBlur,thres[0],thres[1])
    kernel = np.ones((5,5))
    imgDial = cv2.dilate(imgThreshold, kernel, iterations=2)
    imgThreshold = cv2.erode(imgDial, kernel, iterations=1)
    
