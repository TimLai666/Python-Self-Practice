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

img = cv2.imread('colorcolor.jpg')
newImg = img[:150, 200:400]
cv2.imshow('img', img)
cv2.imshow('newImg', newImg)
cv2.waitKey(0)