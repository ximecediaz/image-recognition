# Artificial Intelligence SURF algorithm
# Original author: docs.opencv.org
# Used for the proyect of Image Recognition by Ximena Cervates Díaz

# For execution time testing, is necessary to have a measure of time, this library gave us the necessary method
import time

start_time = time.time()

# Implement the library of OpenCV and mathplotlib
import cv2 as cv
import matplotlib.pyplot as plt

#Here the program reads the image file and put it in a variable
img = cv.imread('uaslp15.jpeg',0)

# Variable of Hessian Threeshold
hess = 20000

# Create SURF object
# Is important to set the Hessian in values between 30 000 and 1 000

surf = cv.xfeatures2d.SURF_create(hess)
# Find keypoints and descriptors directly
kp, des = surf.detectAndCompute(img,None)

len(kp)
print( len(kp) )
# Check present Hessian threshold
print( surf.getHessianThreshold() )

if len(kp) > 50:
	while(len(kp) > 50):
		hess += 3000
		surf.setHessianThreshold(hess)
		kp, des = surf.detectAndCompute(img,None)

elif len(kp) < 20:
	while(len(kp) < 20):
		hess -= 3000
		surf.setHessianThreshold(hess)
		kp, des = surf.detectAndCompute(img,None)

print( surf.getHessianThreshold() )
# Again compute keypoints and check its number.
print( len(kp) )

#Each keypoint is a coordinate "x, y". The keypoints are a matrix of coordinates

img2 = cv.drawKeypoints(img,kp,None,(255,0,0),4)

print("--- %s seconds ---" % (time.time() - start_time))

#plt.imshow(img2),plt.show()


