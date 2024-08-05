import random

import cv2
import numpy as np


# img = cv2.imread('colorcolor.jpg')
# img = cv2.resize(img,(0,0), fx=0.5, fy=0.5)
# cv2.imshow('img', img)
# cv2.waitKey(0)


# cap = cv2.VideoCapture('thumb.mp4')
# while True:
#     ret, frame = cap.read()
#
#     if ret:
#         frame = cv2.resize(frame, (0, 0), fx=0.4, fy=0.4)
#         cv2.imshow('video', frame)
#     else:
#         break
#     if cv2.waitKey(10) == ord('q'):
#         break


# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#
#     if ret:
#         frame = cv2.resize(frame, (0, 0), fx=1.2, fy=1.2)
#         cv2.imshow('video', frame)
#     else:
#         break
#     if cv2.waitKey(10) == ord('q'):
#         break


# img = cv2.imread('colorcolor.jpg')
# print(img)
# print(type(img))
# print(img.shape)


# img = np.empty((300, 300, 3), np.uint8)
# for row in range(300):
#     for col in range(300):
#         b = random.randint(0, 255)
#         g= random.randint(0, 255)
#         r= random.randint(0, 255)
#         img[row][col] = [b, g, r]
# cv2.imshow('img', img)
# cv2.waitKey(0)


# img = cv2.imread('colorcolor.jpg')
# for row in range(300):
#     for col in range(img.shape[1]):
#         b = random.randint(0, 255)
#         g= random.randint(0, 255)
#         r= random.randint(0, 255)
#         img[row][col] = [b, g, r]
# cv2.imshow('img', img)
# cv2.waitKey(0)


# img = cv2.imread('colorcolor.jpg')
# newImg = img[:150, 200:400]
# cv2.imshow('img', img)
# cv2.imshow('newImg', newImg)
# cv2.waitKey(0)


# img = cv2.imread('colorcolor.jpg')
# img = cv2.resize(img,(0,0), fx=0.5, fy=0.5)
# cv2.imshow('img',img)
#
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray',gray)
#
# blur = cv2.GaussianBlur(img,(15,15),10)
# cv2.imshow('blur',blur)
#
# canny = cv2.Canny(img, 100, 250)
# cv2.imshow('canny',canny)
#
# kernel = np.ones((10,10), np.uint8)
# dilate = cv2.dilate(canny, kernel, iterations=1)
# cv2.imshow('dilate',dilate)
#
# kernel1 = np.ones((10,10), np.uint8)
# erode = cv2.erode(dilate,kernel1,iterations=1)
# cv2.imshow('erode',erode)
# cv2.waitKey(0)


# img = np.zeros((600, 600, 3), np.uint8)
# cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 2)
# cv2.rectangle(img, (0,0), (400, 300), (0, 0, 255), cv2.FILLED)
# cv2.circle(img, (300, 400), 30, (255, 0, 0), cv2.FILLED)
# cv2.putText(img, 'hello', (100, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (150,150,150), 2)
# cv2.imshow('img', img)
# cv2.waitKey(0)


# def empty():
#     return 0
#
# img = cv2.imread('XiWinnie.jpg')
# img = cv2.resize(img,(0,0), fx=0.5, fy=0.5)
#
# cv2.namedWindow('TrackBar')
# cv2.resizeWindow('TrackBar', 640, 320)
# cv2.createTrackbar('Hue Min', 'TrackBar', 0, 179, empty)
# cv2.createTrackbar('Hue Max', 'TrackBar', 179, 179, empty)
# cv2.createTrackbar('Sat Min', 'TrackBar', 0, 255, empty)
# cv2.createTrackbar('Sat Max', 'TrackBar', 255, 255, empty)
# cv2.createTrackbar('Val Min', 'TrackBar', 0, 255, empty)
# cv2.createTrackbar('Val Max', 'TrackBar', 255, 255, empty)
#
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# while True:
#     h_min = cv2.getTrackbarPos('Hue Min', 'TrackBar')
#     h_max = cv2.getTrackbarPos('Hue Max', 'TrackBar')
#     s_min = cv2.getTrackbarPos('Sat Min', 'TrackBar')
#     s_max = cv2.getTrackbarPos('Sat Max', 'TrackBar')
#     v_min = cv2.getTrackbarPos('Val Min', 'TrackBar')
#     v_max = cv2.getTrackbarPos('Val Max', 'TrackBar')
#
#     lower = np.array([h_min, s_min, v_min])
#     upper = np.array([h_max, s_max, v_max])
#     mask = cv2.inRange(hsv, lower, upper)
#     result = cv2.bitwise_and(img, img, mask=mask)
#
#     cv2.imshow('img', img)
#     cv2.imshow('hsv',hsv)
#     cv2.imshow('mask',mask)
#     cv2.imshow('result',result)
#     cv2.waitKey(1)


# img = cv2.imread('shape.jpg')
# imgContour = img.copy()
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# canny = cv2.Canny(img, 150, 200)
# contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#
# for cnt in contours:
#     cv2.drawContours(imgContour, cnt, -1, (0, 255, 0), 4)
#     area = cv2.contourArea(cnt)
#     if area > 500:
#         peri = cv2.arcLength(cnt, True)
#         vertices = cv2.approxPolyDP(cnt, peri * 0.02, True)
#         corners = len(vertices)
#         x, y ,w , h = cv2.boundingRect(vertices)
#         cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 0, 255), 2)
#         if corners == 3:
#             cv2.putText(imgContour, 'triangle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#         elif corners == 4:
#             cv2.putText(imgContour, 'rectangle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#         elif corners == 5:
#             cv2.putText(imgContour, 'pentagon', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#         elif corners >= 6:
#             cv2.putText(imgContour, 'circle', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#
# cv2.imshow('img', img)
# cv2.imshow('canny', canny)
# cv2.imshow('contours', imgContour)
# cv2.waitKey(0)


# img = cv2.imread('lenna.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# faceRect = faceCascade.detectMultiScale(gray, 1.1, 3)
# for (x,y,w,h) in faceRect:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
# cv2.imshow('img', img)
# cv2.waitKey(0)


