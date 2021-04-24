import numpy as np
import cv2

def filter_waypoint(A,Map,mx,my):
	m=len(A)
	img =  np.zeros((mx,my,3),np.uint8)
	cv2.namedWindow('filtered path',cv2.WINDOW_NORMAL)
	cv2.imshow('filtered path',img)
	while(True):
		count=0
		for i in range (0,m-2):
			mid=[round( (A[i][0]+A[i+2][0])/2 ),round( (A[i][1]+A[i+2][1])/2 )]
			if(Map[mid[0],mid[1],2] < Map[A[i+1][0],A[i+1][1],2] ) :
				A[i+1][0]=mid[0]
				A[i+1][1]=mid[1]
				count+=1
			elif( Map[mid[0],mid[1],2] == Map[A[i+1][0],A[i+1][1],2] ) :
				if( mid[0] != A[i+1][0] or mid[1] != A[i+1][1] ):
					A[i+1][0]=mid[0]
					A[i+1][1]=mid[1]
					count+=1
		img=Map*15
		for i in range(0,m):
			img=draw(img,A[i][0],A[i][1],1)
		cv2.imshow('filtered path',img)
		cv2.waitKey(20)
		if(count < m/10):
			break
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	return

def draw(img,x,y,n):
	x = int(round(x))
	y = int(round(y))
	for i in range (x,x+6):
		for j in range (y,y+6):
			img[i,j,n]=255
	return img	

