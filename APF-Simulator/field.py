import math
import numpy as np

def att_field(px,py,mx,my):
	res = np.zeros((mx,my))
	for x in range(mx):
		for y in range(my):
			t = 20
			d = math.sqrt((x-px)**2 + (y-py)**2)
			if(d>t):
				res[x,y] = t*d-0.5*(t**2)
			else:
				res[x,y] = 0.5*(d**2)
			res[x,y] = 0.000001*res[x,y]
	return res
   	
def rep_field(px,py,sx,sy,mx,my):
	res = np.zeros((mx,my))
	for x in range(mx):
		for y in range(my):
			thr= 5
			d = ( (x-px)**2 )/sx**2 +( (y-py)**2 )/sy**2 
			d = math.sqrt(d)
			if(d < 1 and d!=0 ):
				res[x,y] = min( (1 - 1/d)**2 ,thr)
				res[x,y] =res[x,y]*0.001
			else:
				res[x,y]=0
	return res
    
def guassian(px,py,sx,sy,mx,my): 
	res = np.zeros((mx,my))
	for x in range(mx):
		for y in range(my):
			d = ( (x-px)**2 )/sx**2 +( (y-py)**2 )/sy**2 
			d *= -0.5
			amp = 1/(2*(math.pi)*sx*sy)
			res[x,y] = 200*amp*math.exp(d)
	return res
