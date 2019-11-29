#Artificial Inteligence algorithm 
#Saving data of all the image processing
# Used for the proyect of Image Recognition by Ximena Cervates Díaz

# Implement the library of OpenCV, os and mathplotlib
import cv2 as cv
import matplotlib.pyplot as plt
import os

#To save all the files directory in a variable
folder = './T/'

#Get the list of files on that folder
images = os.listdir(folder)

#Sort the list of elements in alphabetical order
images.sort()

#Create a new text file to save all the information which the algorithm trows
archdes = open("Pruebadescriptors.txt", "w")
#archkey = open("keypoints.txt", "w")
#arch = open("files.txt", "w")


#This loop is to make the algorithm to all of the file list, in this case, all the images at the folder
for filename in images:

	#If this algorithm works, there is not an error message
	try:	
		#Here the program reads the image file and put it in a variable
		img = cv.imread(os.path.join(folder, filename)) 

		#To know the filename of the image for testing
		#print (filename)

		# Variable of Hessian Threeshold
		hess = 20000

		surf = cv.xfeatures2d.SURF_create(hess)
		# Find keypoints and descriptors directly
		kp, des = surf.detectAndCompute(img,None)

		len(kp)
		#print( len(kp) )

		# Check present Hessian threshold and make an heuristic
		#print( surf.getHessianThreshold() )

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

		#print( surf.getHessianThreshold() )

		# Again compute keypoints and check its number.
		#print( len(kp) )

		# Write the name of the image at the text file
		#arch.write(filename + '\n')
			

		# Loop where for each descriptor matrix
		#for i in range(len(des[0])):
			#for j in range(len(des)):
			#	archdes.write(str(des[j][i]) + ' ')
			#archdes.write('\n')

		for i in range(len(des)):
			for j in range(len(des[0])):
				archdes.write(str(des[i][j]) + ',')

			archdes.write('\n')
		print (len(des))

	
		#for i in range(len(kp)):
			#archkey.write(str(kp[i].pt) + '\n')

		#archkey.write('\n')
		archdes.write('\n')		

		#Each keypoint is a coordinate "x, y". The keypoints are a matrix of coordinates

		img2 = cv.drawKeypoints(img,kp,None,(255,0,0),4)
	# If the algorithm is not sucessful, the program print an error message at the screen
	except:
		print('Cant import ' + filename)

#Close the file
#arch.close()
#archkey.close()
archdes.close()
