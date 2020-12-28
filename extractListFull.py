import sys
import os
import numpy as np
import glob
import cv2

def thirdpoint(x1,y1,x2,y2):
	y1=-y1
	y2=-y2
	xm=0.5*(x1+x2)
	ym=0.5*(y1+y2)
	xd=0.5*(x2-x1)
	yd=0.5*(y2-y1)
	x3=xm+yd
	y3=ym-xd
	y3=-y3
	return (x3,y3)

def transformation(x1,y1,x2,y2):
	(x3,y3)=thirdpoint(x1,y1,x2,y2)
	(a3,b3)=thirdpoint(9,9,22,9)
	pts1 = np.float32([[x1,y1],[x2,y2],[x3,y3]])
	pts2 = np.float32([[9,9],[22,9],[a3,b3]])
	return cv2.getAffineTransform(pts1,pts2)

# flow:
# lees frgc meta data
f = open("data.txt", "r")
lines=f.readlines()
f.close()
lines=[line.split(" ") for line in lines]
print(lines[0])
lines2=[]
#counter=0
for line in lines:
	if line[5]=='C' and line[6]=='N':
		if os.path.isfile('/media/chris/Data/data/frgctxt/datacn/'+line[0]):
			lines2.append([line[0], line[8], line[9], line[10], line[11]])
counter=0
for line in lines2:
	x1=float(line[3])
	y1=float(line[4])
	x2=float(line[1])
	y2=float(line[2])
	
	# read image as grayscale
	img=cv2.imread('/media/chris/Data/data/frgctxt/datacn/'+line[0], cv2.IMREAD_GRAYSCALE)
	
	# find transformation
	M=transformation(x1,y1,x2,y2)
	dst=cv2.warpAffine(img,M,(32,32))
	
	# save as png
	i=line[0].rindex(".")
	l=line[0][:i]
	
	cv2.imwrite('/home/chris/frgc32x32/'+l+'.png', dst)
		
	counter=counter+1
	if counter%100==0:
		print(counter)


