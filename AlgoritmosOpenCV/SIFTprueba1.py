# Artificial Intelligence SIFT algorithm
# Original author: docs.opencv.org
# Used for the proyect of Image Recognition by Ximena Cervates Díaz

# For execution time testing, is necessary to have a measure of time, this library gave us the necessary method
import time

start_time = time.time()
 
# Implement the library of OpenCV
import cv2
# Using pandas and numpy libraries 
import pandas as pd
import numpy as np
# Import the matplotlib library 
import matplotlib.pyplot as plt
from scipy.misc.pilutil import imread, imresize


pd.set_option('display.max_rows', 5)
image_file = 'uaslp5.jpeg'
 
img = cv2.imread(image_file)
plt.imshow(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray)
# Create a SIFT Object
sift = cv2.xfeatures2d.SIFT_create(50)
 
# Get the Key Points from the 'gray' image, this returns a numpy array
kp, des = sift.detectAndCompute(gray,None)
print( len(kp) )
 
# Now we drawn the gray image and overlay the Key Points (kp)
img2 = cv2.drawKeypoints(gray, kp, None, (255,0,0),4)
 

print("--- %s seconds ---" % (time.time() - start_time))

# Plot it to the screen, looks a little small
plt.imshow(img2),plt.show()


